# 在项目根目录运行此脚本：检测 ./img 下的新图片，自动转换为 WebP、调整尺寸并增量重命名
import os
from PIL import Image

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_DIR = os.path.join(SCRIPT_DIR, 'img')
QUALITY = 80 
MAX_WIDTH = 1600
FILE_PREFIX = "photo_"

def main():
    if not os.path.exists(SOURCE_DIR):
        print(f"Error: Directory {SOURCE_DIR} not found.")
        return

    files = sorted([f for f in os.listdir(SOURCE_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])

    if not files:
        print("All images are already in WebP format.")
        return

    existing_indexes = []
    for f in os.listdir(SOURCE_DIR):
        if f.startswith(FILE_PREFIX) and f.endswith(".webp"):
            try:
                num_part = f[len(FILE_PREFIX):-5]
                existing_indexes.append(int(num_part))
            except ValueError:
                continue
    
    current_index = max(existing_indexes) + 1 if existing_indexes else 1
    print(f"start index: {current_index}")

    for filename in files:
        file_path = os.path.join(SOURCE_DIR, filename)
        new_filename = f"{FILE_PREFIX}{current_index}.webp"
        output_path = os.path.join(SOURCE_DIR, new_filename)

        try:
            with Image.open(file_path) as img:
                if img.width > MAX_WIDTH:
                    ratio = MAX_WIDTH / img.width
                    new_height = int(img.height * ratio)
                    img = img.resize((MAX_WIDTH, new_height), Image.Resampling.LANCZOS)

                img.save(output_path, 'WEBP', quality=QUALITY)

            if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
                if os.path.abspath(file_path) != os.path.abspath(output_path):
                    os.remove(file_path)
                print(f"Processed: {filename} -> {new_filename}")
                current_index += 1
            
        except Exception as e:
            print(f"Error: {filename} - {e}")

if __name__ == '__main__':
    main()