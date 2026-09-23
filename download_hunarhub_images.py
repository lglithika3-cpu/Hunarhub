import os
import re
import time
import urllib.parse
import urllib.request
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "frontend" / "images"

CATEGORIES = {
    "tailor": {
        "count": 20,
        "queries": [
            "tailor sewing clothes",
            "dressmaker sewing",
            "sewing machine clothes",
            "clothing tailor"
        ]
    },
    "potter": {
        "count": 20,
        "queries": [
            "pottery maker clay",
            "potter making pottery",
            "clay pots handmade",
            "terracotta pottery"
        ]
    },
    "cobbler": {
        "count": 15,
        "queries": [
            "cobbler shoemaker",
            "shoe making leather",
            "leather shoes handmade",
            "leather footwear crafts"
        ]
    },
    "artisan": {
        "count": 20,
        "queries": [
            "artisan handicraft",
            "traditional handicraft",
            "wood craft artisan",
            "bamboo handicraft"
        ]
    },
    "handmade": {
        "count": 15,
        "queries": [
            "handmade products",
            "handmade crafts",
            "handmade gifts",
            "handmade jewelry"
        ]
    },
    "local-vendor": {
        "count": 15,
        "queries": [
            "local market vendor",
            "fruit market vendor",
            "vegetable market vendor",
            "local shop market"
        ]
    }
}

ALLOWED_LICENSES = [
    "cc0",
    "public domain",
    "cc by",
    "cc by-sa",
    "cc-by",
    "cc-by-sa"
]

USER_AGENT = "HunarHub-ImageDownloader/1.0"

def search_commons(query, limit=50):
    params = {
        "action": "query",
        "format": "json",
        "generator": "search",
        "gsrnamespace": "6",
        "gsrsearch": query,
        "gsrlimit": str(limit),
        "prop": "imageinfo",
        "iiprop": "url|mime|extmetadata",
        "iiurlwidth": "900"
    }

    url = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(params)

    request = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT}
    )

    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))

def get_license(page):
    imageinfo = page.get("imageinfo", [{}])[0]
    metadata = imageinfo.get("extmetadata", {})

    license_name = metadata.get("LicenseShortName", {})
    usage_terms = metadata.get("UsageTerms", {})

    license_text = str(
        license_name.get("value", "") if isinstance(license_name, dict)
        else license_name
    )

    usage_text = str(
        usage_terms.get("value", "") if isinstance(usage_terms, dict)
        else usage_terms
    )

    return (license_text + " " + usage_text).lower()

def is_allowed_license(page):
    license_text = get_license(page)

    return any(
        allowed in license_text
        for allowed in ALLOWED_LICENSES
    )

def safe_extension(mime, url):
    mime = (mime or "").lower()

    if "jpeg" in mime or "jpg" in mime:
        return ".jpg"

    if "png" in mime:
        return ".png"

    if "webp" in mime:
        return ".webp"

    path = urllib.parse.urlparse(url).path.lower()

    if path.endswith(".png"):
        return ".png"

    if path.endswith(".webp"):
        return ".webp"

    return ".jpg"

def download_file(url, destination):
    request = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT}
    )

    with urllib.request.urlopen(request, timeout=60) as response:
        data = response.read()

    if len(data) < 5000:
        raise ValueError("Downloaded file is too small")

    with open(destination, "wb") as file:
        file.write(data)

def main():
    print()
    print("=" * 60)
    print("HUNARHUB - AUTOMATIC IMAGE DOWNLOADER")
    print("=" * 60)
    print()

    total_downloaded = 0

    for category, config in CATEGORIES.items():

        folder = IMAGE_DIR / category
        folder.mkdir(parents=True, exist_ok=True)

        required = config["count"]

        existing = [
            p for p in folder.iterdir()
            if p.is_file() and p.suffix.lower() in
            {".jpg", ".jpeg", ".png", ".webp"}
        ]

        print(f"{category}: {len(existing)} existing images")

        if len(existing) >= required:
            print(f"{category}: already has {required} images")
            print()
            continue

        downloaded = len(existing)
        used_urls = set()

        for query in config["queries"]:

            if downloaded >= required:
                break

            print(f"Searching: {query}")

            try:
                result = search_commons(query, 50)
            except Exception as error:
                print(f"Search failed: {error}")
                continue

            pages = result.get("query", {}).get("pages", {})

            for page in pages.values():

                if downloaded >= required:
                    break

                if not is_allowed_license(page):
                    continue

                imageinfo = page.get("imageinfo", [{}])[0]

                url = imageinfo.get("thumburl") or imageinfo.get("url")
                mime = imageinfo.get("mime", "")

                if not url:
                    continue

                if url in used_urls:
                    continue

                if not mime.startswith("image/"):
                    continue

                used_urls.add(url)

                downloaded += 1

                extension = safe_extension(mime, url)

                filename = f"{category}{downloaded:02d}{extension}"
                destination = folder / filename

                try:
                    print(
                        f"Downloading {downloaded}/{required}: "
                        f"{filename}"
                    )

                    download_file(url, destination)

                    total_downloaded += 1

                    time.sleep(0.3)

                except Exception as error:
                    downloaded -= 1

                    if destination.exists():
                        destination.unlink()

                    print(f"Download failed: {error}")

        final_count = len([
            p for p in folder.iterdir()
            if p.is_file() and p.suffix.lower() in
            {".jpg", ".jpeg", ".png", ".webp"}
        ])

        print(
            f"{category}: {final_count}/{required} images"
        )

        if final_count < required:
            print(
                f"WARNING: Could not obtain enough licensed images "
                f"for {category}."
            )

        print()

    print("=" * 60)
    print("IMAGE DOWNLOAD FINISHED")
    print(f"New images downloaded: {total_downloaded}")
    print("=" * 60)
    print()

    print("Final image counts:")

    grand_total = 0

    for category, config in CATEGORIES.items():

        folder = IMAGE_DIR / category

        count = len([
            p for p in folder.iterdir()
            if p.is_file() and p.suffix.lower() in
            {".jpg", ".jpeg", ".png", ".webp"}
        ])

        grand_total += count

        print(
            f"{category:15} {count:3}/{config['count']}"
        )

    print("-" * 30)
    print(f"{'TOTAL':15} {grand_total:3}/105")
    print()

if __name__ == "__main__":
    main()
