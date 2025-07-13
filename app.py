from meeseeks_menu import run_meeseeks_menu
from web_scrapping import run_web_scraping
import sys

# ========== Callback Functions ==========

def start_new_session():
    print("[*] Starting web scraping session...\n")
    run_web_scraping()

def load_previous_data():
    print("[*] Loading previous data... (Feature not implemented yet)")

def system_settings():
    print("[*] Accessing system settings... (Feature not implemented yet)")

def easter_egg():
    print("[*] 👀 Welcome to the hidden Meeseeks dimension! (Feature not implemented yet)")

def exit_program():
    print("[*] Exiting program... Goodbye!")
    sys.exit()

# ========== Menu Setup ==========

if __name__ == "__main__":
    options = [
        "Scrape BOTH Website",
        "Load Previous Data",
        "System Settings",
        "System Settingsksdhjf",
        "Exit Program"
    ]

    # Map lowercase version of options to functions
    option_callbacks = {
        "start new session": start_new_session,
        "load previous data": load_previous_data,
        "system settings": system_settings,
        "system settingsksdhjf": easter_egg,
        "exit program": exit_program
    }

    # Launch menu
    run_meeseeks_menu(options, option_callbacks)
