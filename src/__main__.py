import os
import re
import requests
import zipfile
from tqdm import tqdm
import questionary


MANGADEX_API = "https://api.mangadex.org"

LANGS_MAP = {
    "ar": "Arabic",
    "de": "German",
    "en": "English",
    "es": "Spanish",
    "es-la": "Spanish (Latin America)",
    "fr": "French",
    "id": "Indonesian",
    "it": "Italian",
    "ko": "Korean",
    "pt": "Portuguese (Portugal)",
    "pt-br": "Portuguese (Brazil)",
    "ru": "Russian",
    "tr": "Turkish",
    "uk": "Ukrainian",
    "vi": "Vietnamese",
    "zh": "Chinese"
}


def safe_filename(name: str) -> str:
    return re.sub(r'[\\/*?:"<>|]', "_", name)


def is_chapter_number(val: str) -> bool:
    return bool(re.match(r'^\d+(\.\d+)?$', str(val)))


def check_api_error(resp_json, context="Request"):
    if resp_json.get("result") == "error":
        err = resp_json.get("errors", [{}])[0]
        print(f"✗ {context} Failed: {err.get('title', 'Unknown Error...')} - {err.get('detail', 'No Detail...')}")
        return True
    return False


def download_chapter(chapter_id: str, zip_filename: str = None, chapter_num: str = None, lang_code: str = None):
    if chapter_num is None or lang_code is None:
        meta_url = f"{MANGADEX_API}/chapter/{chapter_id}"
        meta = requests.get(meta_url).json()
        if check_api_error(meta, "Fetch Chapter Metadata"):
            return
        attrs = meta["data"]["attributes"]
        chapter_num = attrs.get("chapter") or attrs.get("title") or "Untitled"
        lang_code = attrs.get("translatedLanguage", "xx")

    url = f"{MANGADEX_API}/at-home/server/{chapter_id}"
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()

    base_url = data["baseUrl"]
    hash_code = data["chapter"]["hash"]
    pages = data["chapter"]["data"]
    quality = "data"

    if zip_filename is None:
        safe_name = safe_filename(str(chapter_num))
        if is_chapter_number(chapter_num):
            zip_filename = f"chapter-{chapter_num}-{lang_code}.zip"
        else:
            zip_filename = f"{safe_name}-{lang_code}.zip"

    with zipfile.ZipFile(zip_filename, "w") as zipf:
        for i, page in enumerate(
            tqdm(pages, desc=f"✦ Processing {chapter_num}", bar_format="{l_bar}{bar} {n_fmt}/{total_fmt}"), 1):
            img_url = f"{base_url}/{quality}/{hash_code}/{page}"
            img_data = requests.get(img_url).content

            ext = os.path.splitext(page)[1]
            short_name = f"{i:03d}{ext}"
            zipf.writestr(short_name, img_data)

    print("✓ Downloaded & Saved")


def bulk_download(manga_id: str):
    SUPPORTED_LANGS = list(LANGS_MAP.keys())
    lang_params = "&".join([f"translatedLanguage[]={lang}" for lang in SUPPORTED_LANGS])

    url = (
        f"{MANGADEX_API}/manga/{manga_id}/feed?"
        f"limit=500&order[chapter]=asc&includeExternalUrl=0&{lang_params}"
    )
    r = requests.get(url)
    r.raise_for_status()
    feed = r.json()["data"]

    chapters = []
    chapter_map = {}
    chapter_nums = {}
    chapter_langs = {}
    for ch in feed:
        ch_id = ch["id"]
        attrs = ch["attributes"]
        ch_number = attrs.get("chapter")
        lang_code = attrs.get("translatedLanguage")
        language = LANGS_MAP.get(lang_code, lang_code)
        title = attrs.get("title") or "Oneshot"

        if ch_number:
            display_name = f"Chapter {ch_number} [{language}]"
        else:
            display_name = f"{title} [{language}]"

        chapters.append(display_name)
        chapter_map[display_name] = ch_id
        chapter_nums[ch_id] = ch_number or title
        chapter_langs[ch_id] = lang_code

    selected = questionary.checkbox(
        "Select Chapters To Download:",
        choices=chapters
    ).ask()

    if not selected:
        print("✗ No Chapters Selected...")
        return

    os.makedirs(manga_id, exist_ok=True)

    for sel in selected:
        chap_id = chapter_map[sel]
        chap_num = chapter_nums[chap_id]
        chap_lang = chapter_langs[chap_id]

        if is_chapter_number(chap_num):
            zip_filename = os.path.join(manga_id, f"chapter-{chap_num}-{chap_lang}.zip")
        else:
            zip_filename = os.path.join(manga_id, f"{safe_filename(str(chap_num))}-{chap_lang}.zip")

        zip_filename = zip_filename.lower()
        download_chapter(chap_id, zip_filename, chap_num, chap_lang)


def main():
    print("✦ Mangadex Downloader ✦")
    mode = questionary.select(
        "Choose Mode:",
        choices=["Solo", "Bulk"]
    ).ask()

    if mode == "Solo":
        chap_id = questionary.text("Enter Chapter ID:").ask()
        download_chapter(chap_id)
    else:
        manga_id = questionary.text("Enter Manga ID:").ask()
        bulk_download(manga_id)


if __name__ == "__main__":
    main()