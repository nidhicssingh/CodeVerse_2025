import pywhatkit

# Convert text to handwriting and save to image
pywhatkit.text_to_handwriting(
    "Hello Nidhi, this is handwriting text using pywhatkit!",
    save_to="handwriting_output.png"
)

print("✅ Handwriting image saved as handwriting_output.png")
