import subprocess
import time

def get_idle_time():
    try:
        # Run the xprintidle command and capture the output
        output = subprocess.check_output(['xprintidle']).decode('utf-8').strip()
        # Convert the output to seconds
        idle_time_ms = int(output)
        idle_time_sec = idle_time_ms / 1000.0
        return idle_time_sec
    except subprocess.CalledProcessError as e:
        print(f"Error running xprintidle: {e}")
        return None

# Example usage
while True:
    idle_time = get_idle_time()
    if idle_time is not None:
        print(f"Idle time: {idle_time} seconds")
        if idle_time < 300:
            print("Screen is active")
        else:
            print("Screen is idle")
    time.sleep(5)
