import random

# List of possible message templates
message_templates = [
    "Hello {name}, how are you today?",
    "Good morning {name}! Have a great day!",
    "Hey {name}, just checking in. Let's catch up soon!",
    "Hi there {name}, hope you're doing well!",
    "Greetings {name}! Hope your day is going smoothly."
]

# Function to generate a random message
def generate_random_message(name):
    message_template = random.choice(message_templates)
    return message_template.format(name=name)

# Example usage
name = "Nidhi"
random_message = generate_random_message(name)
print(random_message)
