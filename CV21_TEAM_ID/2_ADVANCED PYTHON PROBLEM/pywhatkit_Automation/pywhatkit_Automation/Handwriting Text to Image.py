from PIL import ImageDraw, ImageFont, Image
import sys

# Fix encoding to support Unicode (✅ etc.)
sys.stdout.reconfigure(encoding='utf-8')

def text_to_handwriting_offline(text, save_to="output.png"):
    img = Image.new("RGB", (800, 400), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    font = ImageFont.load_default()  # Use default font
    draw.text((10, 10), text, fill=(0, 0, 0), font=font)

    img.save(save_to)
    print("✅ Offline handwriting image saved:", save_to)

# Call function with your text
text_to_handwriting_offline("Hello, this is Priyanka's handwriting simulation!", save_to="output.png")