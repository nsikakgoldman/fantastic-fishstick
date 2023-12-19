import subprocess
#import pyautogui
import time


def take_screenshot(file_path="screenshot/screenshot.png"):
    # Wait for a moment to ensure the window is active
    time.sleep(2)

    # Get the screen resolution
    screen_width, screen_height = pyautogui.size()

    # capture the entire screen
    screenshot = pyautogui.screenshot()

    # Save the screenshot to the specified file path
    screenshot.save(file_path)
    print(f"Screenshot saved to {file_path}")

def is_screen_active():
    try:
        # Run loginctl to get user session status
        loginctl_output = subprocess.check_output(['loginctl', 'user-status']).decode('utf-8')
        
        # Check if there is an active session
        return 'State: active' in loginctl_output

    except subprocess.CalledProcessError as e:
        print(f"Error running loginctl: {e}")
        return None

# Example usage
while True:
    screen_active = is_screen_active()
    if screen_active is not None:
        if screen_active:
            print("Screen is active, taking screen shot...")
            #take_screenshot()
        else:
            print("Screen is idle")
    time.sleep(5)
