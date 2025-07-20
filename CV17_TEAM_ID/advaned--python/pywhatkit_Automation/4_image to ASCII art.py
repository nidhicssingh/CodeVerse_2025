import pywhatkit

# Convert image to ASCII art
pywhatkit.image_to_ascii_art("FLOWER.JPG", "flower_ascii")

# Print the output from the generated text file
with open("flower_ascii.txt", "r") as file:
    print(file.read())