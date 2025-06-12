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
```

```💻 Usage
Import and call the function in your script:

from your_script_filename import extract_images_from_unsplash

extract_images_from_unsplash("YOUR_SEARCH_KEYWORD")
```

```Example
extract_images_from_unsplash("water")
This will:

Search Unsplash for the term "water"

Download up to 20 non-premium, full-size images

Save them as .png files in a folder named water in your current working directory
```

```Structure
📂 water
├── a1b2c3d4e5.png
├── f6g7h8i9j0.png
└── ...
```
## 🤝 Contributions
Pull requests and suggestions are welcome!
If you find an issue or have an improvement idea, feel free to open an issue or submit a PR.

Let me know if you'd like to add:
- Screenshot of output folders
- CLI arguments support
- Version info
- Link to a hosted example or demo

I can help you structure those too!

