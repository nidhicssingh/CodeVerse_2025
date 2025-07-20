from datetime import datetime

def generate_message(sender, receiver, message, emoji="", time=None):
    if not time:
        time = datetime.now().strftime("%I:%M %p")

    formatted = f"""
WhatsApp Message

{receiver}, you have a new message from {sender}:

Message: {message} {emoji}

Sent at: {time}
"""
    return formatted.strip()

# Example usage
if _name_ == "_main_":
    print("Message Generator")
    sender = input("Enter sender's name: ")
    receiver = input("Enter receiver's name: ")
    message = input("Type the message: ")
    emoji = input("Optional: Add emoji(s): ")

    result = generate_message(sender, receiver, message, emoji)
    print("\nGenerated Message:\n")
    print(result)