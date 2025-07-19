import random

# List of possible message templates
message_templates = [
    "Hello {name}, how are you today?",
    "Good morning {name}! Have a great day!",
    "Hey {name}, Welcome back to the world of coding!",
    "Hi there {name}, hope your day well spent!",
    "Greetings {name}! May all your wishes come true on this auspicious day."
]

# Function to generate a random message
def generate_random_message(name):
    message_template = random.choice(message_templates)
    return message_template.format(name=name)

# Example usage
name = "Harshith"
random_message = generate_random_message(name)
print(random_message)