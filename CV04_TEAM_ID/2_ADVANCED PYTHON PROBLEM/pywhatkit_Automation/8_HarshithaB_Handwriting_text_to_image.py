import pywhatkit

# Convert text to handwriting and save to image
pywhatkit.text_to_handwriting(
    "Hello Harshitha, this is handwriting text using pywhatkit!",
    save_to="Handwriting_output2.png"
)

print("✅ Handwriting image saved as handwriting_output.png")
