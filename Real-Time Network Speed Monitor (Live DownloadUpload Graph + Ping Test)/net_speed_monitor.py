import os
import time
import threading
import statistics
import shutil
import subprocess

# For speed test (install if missing)
# pip install speedtest-cli
try:
    import importlib
    speedtest = importlib.import_module("speedtest")
    SPEEDTEST_AVAILABLE = True
except Exception:
    SPEEDTEST_AVAILABLE = False

def clear():
    os.system("cls" if os.name == "nt" else "clear")

history_down = []
history_up = []
history_ping = []
RUNNING = True

def get_ping():
    try:
        cmd = ["ping", "-n", "1", "8.8.8.8"] if os.name == "nt" else ["ping", "-c", "1", "8.8.8.8"]
        output = subprocess.check_output(cmd).decode()
        for line in output.split("\n"):
            if "time=" in line.lower():
                return float(line.split("time=")[1].split("ms")[0].replace("<", ""))
    except:
        return None

def speed_test_loop():
    global RUNNING
    while RUNNING:
        if SPEEDTEST_AVAILABLE:
            st = speedtest.Speedtest()
            down = st.download() / 1_000_000
            up = st.upload() / 1_000_000
        else:
            down = up = 0

        ping = get_ping()

        history_down.append(down)
        history_up.append(up)
        history_ping.append(ping)

        if len(history_down) > 40:
            history_down.pop(0)
            history_up.pop(0)
            history_ping.pop(0)

        time.sleep(1)

def bar(value, max_val=100, width=40):
    filled = int((value / max_val) * width)
    return "█" * filled + "-" * (width - filled)

def main():
    global RUNNING
    clear()
    print("🌐 Real-Time Network Speed Monitor — Day 58\n")

    t = threading.Thread(target=speed_test_loop)
    t.start()

    try:
        while True:
            clear()
            print("🌐 Real-Time Network Speed Monitor\n")
            if history_down:
                current_down = history_down[-1]
                current_up = history_up[-1]
                current_ping = history_ping[-1]

                print(f"📡 Download: {current_down:.2f} Mbps")
                print(bar(current_down, max_val=200))
                print(f"\n📤 Upload: {current_up:.2f} Mbps")
                print(bar(current_up, max_val=100))
                print(f"\n🏓 Ping: {current_ping} ms")
                print(bar(current_ping, max_val=200))

                print("\n📊 History (last 40s)")
                print("Down ↓:", [round(v, 1) for v in history_down])
                print("Up ↑:  ", [round(v, 1) for v in history_up])
            else:
                print("Running speed test...")

            print("\n🔴 Press CTRL + C to stop.")
            time.sleep(1)

    except KeyboardInterrupt:
        RUNNING = False
        print("\nExiting...")

if __name__ == "__main__":
    main()
