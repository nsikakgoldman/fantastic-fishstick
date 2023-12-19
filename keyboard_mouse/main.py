from evdev import InputDevice
from select import select

# Find the path to your keyboard device (use 'ls /dev/input/' to list input devices)
keyboard_path = '/dev/input/event4'  # Replace 'X' with the appropriate event number

# Open the input device
keyboard = InputDevice(keyboard_path)

print(f"Monitoring keyboard events on {keyboard_path}")

# Monitor keyboard events
while True:
    r, w, x = select([keyboard], [], [])
    for event in keyboard.read():
        print(event)
