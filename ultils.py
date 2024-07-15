import os
import flet as ft


def get_image_paths(folder_path):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.jiff']
    image_paths = []
    for item in os.listdir(folder_path):
        if any(item.lower().endswith(ext) for ext in image_extensions):
            image_paths.append(os.path.join(folder_path, item))
    return image_paths


def hot_key(e: ft.KeyboardEvent):
    if e.ctrlKey and e.key == "o":
        print("ctrl pressed!")
