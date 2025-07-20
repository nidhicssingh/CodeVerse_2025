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
<<<<<<<< HEAD:CV09_TEAM_ID/2_ADVANCED PYTHON PROBLEM/Whatsapp_Message_Generator/Pywhatkit_Whatsapp_message_generator/rakshawhatsapp.py
name = "Nidhi"
phone_number = "+919483858750"
========
name = "Nithya"
phone_number = "+919353674193"
>>>>>>>> 07ca9d69afb79eca54ba73ecfc7d1305e1f20a53:CV06_TEAM_ID/2_ADVANCED PYTHON PROBLEM/Whatsapp_Message_Generator/Nithya_2_random message.py
random_message = generate_random_message(name)

# Get time 2 minutes from now
now = datetime.now()
future_time = now + timedelta(minutes=2)
hour = future_time.hour
minute = future_time.minute

# Send the message
pywhatkit.sendwhatmsg(phone_number, random_message, hour, minute)

<<<<<<<< HEAD:CV09_TEAM_ID/2_ADVANCED PYTHON PROBLEM/Whatsapp_Message_Generator/Pywhatkit_Whatsapp_message_generator/rakshawhatsapp.py
print(f"Message scheduled for {name} at {hour}:{minute} → \"{random_message}\"")
========
print(f"Message scheduled for {name} at {hour}:{minute} → \"{random_message}\"")
>>>>>>>> 07ca9d69afb79eca54ba73ecfc7d1305e1f20a53:CV06_TEAM_ID/2_ADVANCED PYTHON PROBLEM/Whatsapp_Message_Generator/Nithya_2_random message.py
