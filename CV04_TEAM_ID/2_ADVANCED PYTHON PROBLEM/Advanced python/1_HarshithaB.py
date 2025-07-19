import random

# List of possible message templates
message_templates = [
    "Hello {name}, Nice to meet you!",
    "Good morning {name}! Have a great day!",
    "Hey {name}, good morning!",
    "Hi  {name}, hope you're doing well!",
    "Greetings {name}! Hope your day is going smoothly."
]

# Function to generate a random message
def generate_random_message(name):
    message_template = random.choice(message_templates)
    return message_template.format(name=name)

# Example usage
name = "Harshitha.B"
random_message = generate_random_message(name)
print(random_message)
