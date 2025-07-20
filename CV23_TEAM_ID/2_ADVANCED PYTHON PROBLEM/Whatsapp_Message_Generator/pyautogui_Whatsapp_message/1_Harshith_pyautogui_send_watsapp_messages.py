# Importing the required module
import pyautogui as pg
import time

# Giving Dealy to run program
print("program will run after 5 second")
time.sleep(5)
print("running")

# Note : after running the program immediately open whatsapp web then open the persons chat you want to send messages

#Adding a name
name="Harshith"

# For loop
for i in range(1):
    # writing the messages
    pg.write(f"Hi {name}, We appreciate to purchase many books. Happy Learning!!")
    time.sleep(0.5) 
    # Seding the messages by pressing enter
    pg.press("Enter")
    
