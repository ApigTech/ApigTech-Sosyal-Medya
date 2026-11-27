"""Özel günlerde Instagram story paylaşan bot.

Her çalıştığında bugünün tarihini (Türkiye saati) özel günler listesinde arar.
Bugün bir özel günse ilgili görseli Instagram Graph API ile story olarak paylaşır,
değilse hiçbir şey yapmadan çıkar.

Sadece Python standart kütüphanesini kullanır; ek paket kurmaya gerek yoktur.

Gerekli ortam değişkenleri (gerçek paylaşım için):
    IG_USER_ID        Instagram profesyonel hesabının kullanıcı kimliği
    IG_ACCESS_TOKEN   Meta erişim anahtarı (GitHub Secrets'ta saklanır, koda yazılmaz)
    IMAGE_BASE_URL    Storyler klasörünün herkese açık adresi
                      (ör. https://raw.githubusercontent.com/KULLANICI/REPO/main/Storyler)

İsteğe bağlı ortam değişkenleri:
    POSTING_ENABLED     "true" değilse bot sadece deneme modunda çalışır
    GRAPH_HOST          Varsayılan: graph.facebook.com
    GRAPH_API_VERSION   Varsayılan: v23.0

Örnekler:
    python bot/post_story.py --date 2027-05-19 --dry-run
    python bot/post_story.py            # bugünün tarihiyle
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DATA = REPO_ROOT / "data" / "ozel_gunler_2027_2031.csv"
STORY_DIR = REPO_ROOT / "Storyler"

# Türkiye 2016'dan beri yaz saati uygulamıyor, sabit UTC+3.
TURKEY_TZ = timezone(timedelta(hours=3), name="Europe/Istanbul")


def log(message: str) -> None:
    print(message, flush=True)


def today_in_turkey() -> date:
    return datetime.now(TURKEY_TZ).date()


def load_days(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def find_days(rows: list[dict[str, str]], target: date) -> list[dict[str, str]]:
    key = target.isoformat()
    return [row for row in rows if row.get("tarih") == key]


def graph_request(url: str, params: dict[str, str] | None = None, method: str = "GET") -> dict:
    """Graph API'ye istek atar. Hata mesajlarında erişim anahtarı asla yazdırılmaz."""
    data = None
    if params is not None and method == "POST":
        data = urllib.parse.urlencode(params).encode("utf-8")
    elif params is not None:
        url = f"{url}?{urllib.parse.urlencode(params)}"
    request = urllib.request.Request(url, data=data, method=method)
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        try:
            detail = json.loads(body).get("error", {}).get("message", body)
        except json.JSONDecodeError:
            detail = body
        raise RuntimeError(f"Graph API hatası ({error.code}): {detail}") from None


def publish_story(image_url: str, user_id: str, token: str, host: str, version: str) -> str:
    base = f"https://{host}/{version}"

    container = graph_request(
        f"{base}/{user_id}/media",
        {"image_url": image_url, "media_type": "STORIES", "access_token": token},
        method="POST",
    )
    creation_id = container.get("id")
    if not creation_id:
        raise RuntimeError(f"Medya kapsayıcısı oluşturulamadı: {container}")
    log(f"  Medya kapsayıcısı oluşturuldu: {creation_id}")

    # Instagram görseli işlerken bir süre bekle.
    for _ in range(20):
        status = graph_request(
            f"{base}/{creation_id}",
            {"fields": "status_code", "access_token": token},
        ).get("status_code")
        if status == "FINISHED":
            break
        if status in {"ERROR", "EXPIRED"}:
            raise RuntimeError(f"Instagram görseli işleyemedi (durum: {status}).")
        time.sleep(3)
    else:
        raise RuntimeError("Instagram görseli zamanında işleyemedi.")

    published = graph_request(
        f"{base}/{user_id}/media_publish",
        {"creation_id": creation_id, "access_token": token},
        method="POST",
    )
    media_id = published.get("id")
    if not media_id:
        raise RuntimeError(f"Story yayımlanamadı: {published}")
    return media_id


def main(argv: list[str] | None = None) -> int:
    # Windows terminalinde Türkçe karakterler ve oklar sorun çıkarmasın.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Özel günlerde Instagram story paylaşır.")
    parser.add_argument("--date", help="Denemek için tarih (YYYY-AA-GG). Verilmezse bugün kullanılır.")
    parser.add_argument("--dry-run", action="store_true", help="Paylaşmadan sadece ne yapılacağını gösterir.")
    parser.add_argument("--data", default=str(DEFAULT_DATA), help="Özel günler CSV dosyası.")
    args = parser.parse_args(argv)

    target = date.fromisoformat(args.date) if args.date else today_in_turkey()
    rows = load_days(Path(args.data))
    years = sorted({row["tarih"][:4] for row in rows if row.get("tarih")})
    log(f"Tarih: {target.isoformat()} (listedeki yıllar: {years[0]}–{years[-1]})")

    if str(target.year) > years[-1]:
        log("UYARI: Bu tarih özel günler listesinin kapsadığı yılların dışında. Listeyi güncelleyin.")

    todays = find_days(rows, target)
    if not todays:
        log("Bugün özel bir gün değil, paylaşım yapılmayacak.")
        return 0

    posting_enabled = os.environ.get("POSTING_ENABLED", "").strip().lower() == "true"
    dry_run = args.dry_run or not posting_enabled
    base_url = os.environ.get("IMAGE_BASE_URL", "").rstrip("/")

    errors = 0
    for day in todays:
        filename = (day.get("gorsel") or "").strip()
        log(f"Özel gün: {day['ozel_gun']} → {filename or '(görsel tanımlı değil)'}")
        if not filename:
            log("  HATA: Bu gün için görsel tanımlanmamış (gorsel sütunu boş).")
            errors += 1
            continue
        if not (STORY_DIR / filename).is_file():
            log(f"  HATA: Storyler/{filename} bulunamadı.")
            errors += 1
            continue

        image_url = f"{base_url}/{urllib.parse.quote(filename)}" if base_url else f"(IMAGE_BASE_URL)/{filename}"
        if dry_run:
            reason = "--dry-run verildi" if args.dry_run else "POSTING_ENABLED=true ayarlı değil"
            log(f"  DENEME MODU ({reason}): {image_url} paylaşılırdı.")
            continue

        user_id = os.environ.get("IG_USER_ID", "").strip()
        token = os.environ.get("IG_ACCESS_TOKEN", "").strip()
        if not user_id or not token or not base_url:
            log("  HATA: IG_USER_ID, IG_ACCESS_TOKEN ve IMAGE_BASE_URL tanımlı olmalı.")
            errors += 1
            continue

        try:
            media_id = publish_story(
                image_url,
                user_id,
                token,
                os.environ.get("GRAPH_HOST", "graph.facebook.com"),
                os.environ.get("GRAPH_API_VERSION", "v23.0"),
            )
            log(f"  Story paylaşıldı (medya kimliği: {media_id}).")
        except RuntimeError as error:
            log(f"  HATA: {error}")
            errors += 1

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
