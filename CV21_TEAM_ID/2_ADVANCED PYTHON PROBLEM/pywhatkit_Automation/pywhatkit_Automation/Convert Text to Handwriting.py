from PIL import ImageDraw, ImageFont, Image

def text_to_handwriting_offline(text, save_to="output.png"):
    img = Image.new("RGB", (800, 400), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Load default font (you can customize this)
    font = ImageFont.load_default()

    # Write the text on image
    draw.text((10, 10), text, fill=(0, 0, 0), font=font)
    img.save(save_to)

    # NO emojis or special characters here
    print("Offline handwriting image saved:", save_to)

# Call the function
text_to_handwriting_offline("Hello Priyanka | This is handwriting text", save_to="output1.png")