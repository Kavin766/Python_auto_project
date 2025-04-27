import os
import time

def open_apps():
    # Paths to your applications (update these paths according to your system)
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    notepad_path = r"C:\Windows\System32\notepad.exe"
    vscode_path = r"C:\Users\YourUsername\AppData\Local\Programs\Microsoft VS Code\Code.exe"

    # Open apps one by one
    os.startfile(chrome_path)
    time.sleep(2)  # Wait for 2 seconds

    os.startfile(notepad_path)
    time.sleep(2)

    os.startfile(vscode_path)
    time.sleep(2)

    print("All apps have been opened successfully!")

if __name__ == "__main__":
    open_apps()  
