import cv2
import os
import time

# ASCII characters used to build the output text
ASCII_CHARS = "@%#*+=-:. "

# Resize the image according to the aspect ratio
def resize_image(image, new_width=100):
    height, width = image.shape
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.35)
    resized_image = cv2.resize(image, (new_width, new_height))
    return resized_image

# Convert grayscale image to ASCII string
def gray_to_ascii(image):
    ascii_str = ""
    for row in image:
        for pixel in row:
            ascii_str += ASCII_CHARS[pixel // 32]
        ascii_str += "\n"
    return ascii_str

# Main function
def play_ascii_video(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            resized_gray = resize_image(gray, new_width=100)
            ascii_frame = gray_to_ascii(resized_gray)

            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal
            print(ascii_frame)
            time.sleep(1 / 30)  # Adjust to match the video's FPS

    except KeyboardInterrupt:
        print("Stopped.")
    finally:
        cap.release()

video_path = "aura_farming.mp4" # Replace with your actual video file path
play_ascii_video(video_path)
