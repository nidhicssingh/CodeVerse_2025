from datetime import datetime

# Title
print("📩 Message Generator")

# Input
sender = input("Enter sender's name: ")
receiver = input("Enter receiver's name: ")
message = input("Type the message: ")
emoji = input("Optional: Add emoji(s): ")

# Generate Message
print("\nGenerated Message:\n")
print("📱 WhatsApp Message\n")
print(f"{receiver}, you have a new message from {sender}:\n")
print(f"💬 {message} {emoji}")
print("\n🕒 Sent at:", datetime.now().strftime("%I:%M %p"))