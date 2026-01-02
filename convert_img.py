# 将此脚本放在项目根目录 (与 img 文件夹同级) 运行，自动转换为webp格式并清理原图
import os
from PIL import Image

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_DIR = os.path.join(SCRIPT_DIR, 'img')
QUALITY = 80 
MAX_WIDTH = 1600

def convert_to_webp():
    if not os.path.exists(SOURCE_DIR):
        print(f"Error: Directory {SOURCE_DIR} not found.")
        return

    for filename in os.listdir(SOURCE_DIR):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            file_path = os.path.join(SOURCE_DIR, filename)
            file_name_no_ext = os.path.splitext(filename)[0]
            output_path = os.path.join(SOURCE_DIR, f"{file_name_no_ext}.webp")

            try:
                with Image.open(file_path) as img:
                    if img.width > MAX_WIDTH:
                        ratio = MAX_WIDTH / img.width
                        new_height = int(img.height * ratio)
                        img = img.resize((MAX_WIDTH, new_height), Image.Resampling.LANCZOS)

                    img.save(output_path, 'WEBP', quality=QUALITY)

                if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
                    os.remove(file_path)
                    print(f"Processed: {filename}")
            
            except Exception as e:
                print(f"Error: {filename} - {e}")

if __name__ == '__main__':
    convert_to_webp()