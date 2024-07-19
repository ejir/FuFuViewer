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


#区块浏览，将gird图分割成多个小块，每个小块都是一个独立的图像
def block_browse(image_path, block_size):
    image = ft.imread(image_path)
    image_height, image_width = image.shape[:2]
    block_height, block_width = block_size
    for y in range(0, image_height, block_height):
        for x in range(0, image_width, block_width):
            block = image[y:y + block_height, x:x + block_width]
            yield block, (x, y, block_width, block_height)
