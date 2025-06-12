import requests
import io
from PIL import Image
from pathlib import Path
import hashlib

def extract_images_from_unsplash(word):
    # Create a directory with the same name as the word
    output_dir = Path(word)
    output_dir.mkdir(parents=True, exist_ok=True)  # Create the directory if it doesn't exist

    url = f"https://unsplash.com/napi/search/photos?page=1&per_page=20&query={word}&xp=plus-offset%3Aexperiment-variant-2"

    querystring = {"page": "1", "per_page": "20", "query": word , "xp": "plus-offset:experiment-variant-2"}

    payload = "page=2&per_page=20&query=water&xp=plus-offset%3Aexperiment-variant-2"
    headers = {
        "^client-geo-region": "global^",
        "^sec-ch-ua-platform": "^\^Windows^^^",
        "^Referer": "https://unsplash.com/s/photos/water^",
        "^accept-language": "en-US^",
        "^sec-ch-ua": "^\^Brave^^;v=^\^137^^, ^\^Chromium^^;v=^\^137^^, ^\^Not/ABrand^^;v=^\^24^^^",
        "^User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36^",
        "^sec-ch-ua-mobile": "?0^",
        "Content-Type": "application/json"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    data = response.json()
    images = []

    for item in data["results"]:
        if not item["plus"]:
            images.append(item["urls"].get("full"))
    
    print(f"Found {len(images)} images for the word '{word}'.")

    for image_url in images:
        # Download the image content
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            image_file = io.BytesIO(image_response.content)  # Use the image content
            image = Image.open(image_file).convert("RGB")

            # Generate a unique file name using a hash
            file_path = output_dir / (hashlib.sha1(image_response.content).hexdigest()[:10] + ".png")
            image.save(file_path, "PNG", quality=100)
        else:
            print(f"Failed to download image: {image_url}")

    print("Done Extractting...")

extract_images_from_unsplash("GTA")