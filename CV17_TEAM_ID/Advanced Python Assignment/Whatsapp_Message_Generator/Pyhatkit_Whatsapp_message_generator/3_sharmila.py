from datetime import datetime, timedelta

now = datetime.now()
# Add 2 minutes from now (gives WhatsApp Web time to load)
future_time = now + timedelta(minutes=2)

hour = future_time.hour
minute = future_time.minute

import random
import pywhatkit
from datetime import datetime, timedelta

# Message templates
message_templates = [
    "Hello {name}, how are you today?",
    "Good morning {name}! Have a great day!",
    "Hey {name}, just checking in. Let's catch up soon!",
    "Hi there {name}, hope you're doing well!",
    "Greetings {name}! Hope your day is going smoothly."
]

# Generate a random message
def generate_random_message(name):
    message_template = random.choice(message_templates)
    return message_template.format(name=name)

# Input
name = "Tanushree"
phone_number = "+919902956084"
random_message = generate_random_message(name)

# Get time 2 minutes from now
now = datetime.now()
future_time = now + timedelta(minutes=2)
hour = future_time.hour
minute = future_time.minute

# Send the message
pywhatkit.sendwhatmsg(phone_number, random_message, hour, minute)

print(f"Message scheduled for {name} at {hour}:{minute} → \"{random_message}\"")