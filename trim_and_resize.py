import os
from PIL import Image

def trim_and_resize(source_path, output_base):
    if not os.path.exists(source_path):
        print(f"Source {source_path} not found")
        return

    # Open the image
    img = Image.open(source_path)
    if img.mode != 'RGBA':
        img = img.convert('RGBA')

    # Trim transparency
    # find bbox
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
    
    # Square it up (keep aspect ratio and center if necessary, but here we expect a square-ish logo)
    width, height = img.size
    max_dim = max(width, height)
    new_img = Image.new('RGBA', (max_dim, max_dim), (0, 0, 0, 0))
    # Paste centered
    new_img.paste(img, ((max_dim - width) // 2, (max_dim - height) // 2))
    img = new_img

    # Sizes for Android
    # mipmap-mdpi: 48x48
    # mipmap-hdpi: 72x72
    # mipmap-xhdpi: 96x96
    # mipmap-xxhdpi: 144x144
    # mipmap-xxxhdpi: 192x192
    sizes = {
        "mipmap-mdpi": 48,
        "mipmap-hdpi": 72,
        "mipmap-xhdpi": 96,
        "mipmap-xxhdpi": 144,
        "mipmap-xxxhdpi": 192,
        "mipmap-ldpi": 36 # Bonus
    }

    for folder, size in sizes.items():
        folder_path = os.path.join(output_base, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path, exist_ok=True)
        
        target_path = os.path.join(folder_path, "ic_launcher.png")
        # Resize using Lanczos for high quality
        resized = img.resize((size, size), Image.Resampling.LANCZOS)
        resized.save(target_path, "PNG")
        print(f"Generated: {target_path}")

    # iOS Icon
    ios_output = "d:/prio copy/ios/App/App/Assets.xcassets/AppIcon.appiconset"
    if os.path.exists(ios_output):
        ios_target = os.path.join(ios_output, "AppIcon-512@2x.png")
        resized_ios = img.resize((1024, 1024), Image.Resampling.LANCZOS)
        resized_ios.save(ios_target, "PNG")
        print(f"Generated iOS: {ios_target}")

if __name__ == "__main__":
    source = "d:/prio copy/prio_logo.png"
    output = "d:/prio copy/android/app/src/main/res"
    trim_and_resize(source, output)
