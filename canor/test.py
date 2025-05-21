from PIL import Image
import sys
import os

def crop_transparent(image_path, save_path=None):
    image = Image.open(image_path).convert("RGBA")
    alpha = image.split()[-1]  # Get alpha channel
    bbox = alpha.getbbox()  # Bounding box of non-zero alpha pixels

    if bbox:
        cropped = image.crop(bbox)
        if save_path:
            cropped.save(save_path)
        else:
            base, ext = os.path.splitext(image_path)
            cropped.save(f"{base}_cropped{ext}")
        print(f"Cropped image saved to: {save_path or base + '_cropped' + ext}")
    else:
        print("No non-transparent pixels found. Image unchanged.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python crop_alpha.py input.png [output.png]")
    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2] if len(sys.argv) > 2 else None
        crop_transparent(input_path, output_path)
