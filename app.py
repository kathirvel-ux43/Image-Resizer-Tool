import os
from PIL import Image
from pathlib import Path
import sys

def batch_resize_images():
    """
    Simple batch image resizer for beginners
    """
    print("🖼️  Image Resizer Tool")
    print("=" * 40)
    
    # Define folders
    input_folder = "input_images"
    output_folder = "resized_images"
    
    # Create folders if they don't exist
    Path(input_folder).mkdir(exist_ok=True)
    Path(output_folder).mkdir(exist_ok=True)
    
    # Supported image formats
    supported_formats = ['*.jpg', '*.jpeg', '*.png', '*.bmp', '*.webp']
    
    # Find all images
    image_files = []
    for format in supported_formats:
        image_files.extend(Path(input_folder).glob(format))
        image_files.extend(Path(input_folder).glob(format.upper()))
    
    if not image_files:
        print(f"❌ No images found in '{input_folder}' folder!")
        print(f"💡 Please add some images to the '{input_folder}' folder and run again.")
        return
    
    print(f"📁 Found {len(image_files)} image(s) to process:")
    for img in image_files:
        print(f"   - {img.name}")
    
    # Resize settings
    new_width = 800  # You can change this
    new_height = 600  # You can change this
    
    print(f"\n⚙️  Resize settings: {new_width}x{new_height} pixels")
    print("🔄 Processing images...")
    print("-" * 40)
    
    success_count = 0
    
    for image_path in image_files:
        try:
            with Image.open(image_path) as img:
                # Get original dimensions
                original_width, original_height = img.size
                
                # Resize image
                resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                
                # Create output filename
                output_filename = f"resized_{image_path.stem}{image_path.suffix}"
                output_path = Path(output_folder) / output_filename
                
                # Save resized image
                resized_img.save(output_path)
                
                print(f"✅ Resized: {image_path.name}")
                print(f"   📐 {original_width}x{original_height} → {new_width}x{new_height}")
                print(f"   💾 Saved as: {output_filename}")
                
                success_count += 1
                
        except Exception as e:
            print(f"❌ Error processing {image_path.name}: {str(e)}")
    
    print("-" * 40)
    print(f"🎉 Successfully processed {success_count}/{len(image_files)} images!")
    print(f"📂 Output folder: {output_folder}")
    
    # Show what to do next
    if success_count > 0:
        print(f"\n🎯 Next steps:")
        print(f"   1. Check the '{output_folder}' folder for your resized images")
        print(f"   2. Add more images to '{input_folder}' folder and run again")
        print(f"   3. Modify the width/height values in the code to change resize dimensions")

def check_folder_structure():
    """
    Check if the project structure is correct
    """
    print("🔍 Checking project structure...")
    
    folders = ['input_images', 'resized_images']
    for folder in folders:
        if Path(folder).exists():
            print(f"✅ {folder}/ folder exists")
        else:
            print(f"📁 Creating {folder}/ folder...")
            Path(folder).mkdir(exist_ok=True)
    
    # Check for images
    image_extensions = ['*.jpg', '*.jpeg', '*.png']
    image_count = 0
    
    for ext in image_extensions:
        image_count += len(list(Path('input_images').glob(ext)))
    
    if image_count == 0:
        print("\n💡 Tip: Add some images to the 'input_images' folder and run the script again!")
    else:
        print(f"📷 Found {image_count} image(s) in 'input_images' folder")

if __name__ == "__main__":
    check_folder_structure()
    print()
    batch_resize_images()