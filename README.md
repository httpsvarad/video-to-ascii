# 🖥️ Video-to-ASCII

A minimal Python project that plays the viral **Aura Farming** dance video - or any 1:1 (square) video - as animated ASCII art in your terminal. It reads each video frame, converts it to grayscale, maps pixel brightness to ASCII characters, and prints the result in real time, creating a live text-based animation with no GUI required.

---

## 🚀 How to Run

### 1. Clone this Repo

```bash
git clone https://github.com/httpsvarad/video-to-ascii.git
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Your Video

* Place your **1:1 video** in the root directory.

### 4. Run the Script

```bash
python play_ascii_video.py
```

---

## 🎯 Tips for Best Experience

* **Zoom Out** your terminal (`Ctrl + -`) to fit more ASCII characters.
* **Use Fullscreen Terminal** for smooth animation.
* Adjust `width` in `play_ascii_video.py` to change resolution.
* Use a **monospaced terminal** (e.g., VS Code Terminal, Ubuntu Terminal, CMD, macOS Terminal).

---

## 🎥 Use a Different Video?

Change this line in `play_ascii_video.py`:

```python
video_path = "aura_farming.mp4"
```

To your custom file:

```python
video_path = "your_video.mp4"
```

Make sure it's square (1:1 aspect ratio).

---

## 📦 Requirements

File: `requirements.txt`

```txt
opencv-python
numpy
```

Install with:

```bash
pip install -r requirements.txt
```

---

## ⭐ Credits

Runs the viral **Aura Farming** video as terminal ASCII art.
Project made for fun and learning!

