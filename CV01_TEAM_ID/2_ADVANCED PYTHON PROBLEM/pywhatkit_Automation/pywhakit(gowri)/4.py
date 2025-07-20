82% of storage used … If you run out of space, you can't save to Drive, back up Google Photos, or use Gmail. Get 30 GB of storage for ₹59.00 ₹15.00/month for 2 months.
from datetime import datetime

def generate_message(sender, receiver, message, emoji="", time=None):
    if not time:
        time = datetime.now().strftime("%I:%M %p")

    formatted = f"""
📱 WhatsApp Message

{receiver}, you have a new message from {sender}:

💬 {message} {emoji}

🕒 Sent at: {time}
"""
    return formatted.strip()

# Example usage
if __name__ == "__main__":
    print("📲 Message Generator")
    sender = input("Enter sender's name: ")
    receiver = input("Enter receiver's name: ")
    message = input("Type the message: ")
    emoji = input("Optional: Add emoji(s): ")

    result = generate_message(sender, receiver, message, emoji)
    print("\nGenerated Message:\n")
    print(result)