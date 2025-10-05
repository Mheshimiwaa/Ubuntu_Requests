import requests
import os
from urllib.parse import urlparse

def fetch_image(url, save_dir="Fetched_Images"):
    # Create  folder
    os.makedirs(save_dir, exist_ok=True)

    try:
        # Get  image data
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Get filename from  URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path) or "downloaded_image.jpg"

        # Save  image
        path = os.path.join(save_dir, filename)
        with open(path, "wb") as file:
            file.write(response.content)

        print(f"Image saved successfully as {path}")

    except requests.exceptions.RequestException as e:
        print("Error downloading image:", e)

if __name__ == "__main__":
    image_url = input("Enter the image URL: ").strip()
    fetch_image(image_url)
