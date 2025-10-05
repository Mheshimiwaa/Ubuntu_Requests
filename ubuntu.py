import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Ask user for multiple URLs
    urls = input("Enter one or more image URLs (separated by space): ").split()

    # Create directory if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)

    downloaded = set()  # keep track of downloaded filenames

    for url in urls:
        print(f"\nFetching: {url}")
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # raise error for failed response

            # Check if response is actually an image
            content_type = response.headers.get("Content-Type", "")
            if not content_type.startswith("image/"):
                print("This URL does not point to an image.")
                continue

            # Extract filename from URL
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)

            if not filename:
                filename = "downloaded_image.jpg"

            # Prevent duplicates
            if filename in downloaded:
                print("Duplicate detected.")
                continue

            filepath = os.path.join("Fetched_Images", filename)

            with open(filepath, "wb") as f:
                f.write(response.content)

            downloaded.add(filename)

            # Display success messages
            print(f"Successfully fetched: {filename}")
            print(f"Image saved to {filepath}")

        except requests.exceptions.RequestException as e:
            print(f" Connection error: {e}")
        except Exception as e:
            print(f" Unexpected error: {e}")

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
