#code by chatgpt to scrape images

import os
import requests
from ddgs import DDGS
import time

# ----------------------------
# FILTER: remove illustrations, vector signs, PNG icons etc.
# ----------------------------
def is_real_photo(result):
    url = result.get("image", "").lower()
    title = result.get("title", "").lower()

    # block SVG / vector / clipart / icons
    bad_keywords = ["svg", "vector", "clipart", "icon", "illustration", "drawing"]
    if any(k in url for k in bad_keywords):
        return False
    if any(k in title for k in bad_keywords):
        return False

    # PNGs are usually icons (not always, but safest to skip)
    if url.endswith(".png"):
        return False

    return True


# ----------------------------
# DOWNLOAD FUNCTION
# ----------------------------
def download_images(query, folder, n=10):
    os.makedirs(folder, exist_ok=True)
    saved = 0

    with DDGS() as ddgs:
        results = ddgs.images(
            query,           # correct positional argument
            safesearch="off",
            max_results=60   # overshoot for filtering
        )

        for i, r in enumerate(results):
            if saved >= n:
                break

            if not is_real_photo(r):
                continue

            img_url = r.get("image")
            if not img_url:
                continue

            try:
                response = requests.get(img_url, timeout=6)
                if response.status_code != 200:
                    continue

                with open(f"{folder}/{saved}.jpg", "wb") as f:
                    f.write(response.content)

                saved += 1

            except:
                pass

            # small sleep to avoid rate-limit
            if i % 5 == 0:
                time.sleep(1)

    print(f"{query}: saved {saved}/{n} images")


# ----------------------------
# UK-SPECIFIC TRAFFIC SIGN QUERIES
# ----------------------------
classes = {
    "stop sign": "UK stop sign real street photo",
    "give way sign": "UK give way sign real street photo triangle",
    "no parking sign": "UK no parking sign real street photo",
    "no stopping sign": "UK clearway no stopping sign UK real street photo",
    "no entry sign": "UK no entry sign real street photo",
    "no U turn sign": "UK no U turn sign real street photo",
    "speed limit sign": "UK speed limit sign real street photo",
    "road work sign": "UK roadworks sign real street photo triangle",
    "pedestrian crossing sign": "UK pedestrian crossing sign zebra crossing UK real street photo",
    "school zone sign": "UK school keep clear sign real street photo",
    "roundabout sign": "UK roundabout sign real street photo triangle",
    "sharp turn warning sign": "UK sharp bend warning sign triangle real street photo"
}


# ----------------------------
# RUN DOWNLOADER FOR EACH CLASS
# ----------------------------
for class_name, query in classes.items():
    folder = f"dataset/{class_name.replace(' ', '_')}"
    download_images(query, folder, n=10)
