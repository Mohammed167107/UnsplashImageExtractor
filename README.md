# 🖼️ Unsplash Image Extractor

A simple Python script that downloads high-resolution images from [Unsplash](https://unsplash.com/) based on a search keyword. The images are saved locally in a folder named after the keyword.

## 📌 Features

- Sends a query to the Unsplash search API.
- Extracts direct image URLs from the search results.
- Downloads and saves only free (non-Plus) full-size images.
- Automatically creates a local directory for each keyword.
- Saves images as `.png` files with unique names based on SHA1 hash.

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.x
- `requests` library
- `Pillow` (PIL fork)

Install the required packages:

```bash
pip install requests pillow
