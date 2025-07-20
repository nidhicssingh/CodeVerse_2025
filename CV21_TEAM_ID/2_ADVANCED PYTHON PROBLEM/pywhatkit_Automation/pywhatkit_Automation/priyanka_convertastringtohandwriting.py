from PIL import ImageDraw, ImageFont, Image

def text_to_handwriting_offline(text, save_to="handwriting.png"):
    # Create a blank white image
    img = Image.new("RGB", (800, 440), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Use default font or install a handwriting font
    font = ImageFont.load_default()
    
    # Draw the text on the image
    draw.text((10, 10), text, fill=(0, 0, 0), font=font)
    img.save(save_to)
    print("✅ Handwriting image saved as:", save_to)

# Run this
text_to_handwriting_offline("Hello PRIYANKA!  This is  Python  magic!")