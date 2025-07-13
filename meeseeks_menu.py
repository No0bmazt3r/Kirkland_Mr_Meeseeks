import os
import time
import sys
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_terminal_size():
    try:
        columns, rows = os.get_terminal_size()
        return columns, rows
    except:
        return 80, 24

def print_centered(text, width, color_code="37"):
    padding = (width - len(text)) // 2
    print(f"\033[{color_code}m{' ' * padding}{text}\033[0m")

def print_loading_art():
    width, _ = get_terminal_size()
    meeseeks_art = [
        "    oooooooooo    ",
        "   o          o   ",
        "  o  ◉      ◉  o  ",
        " o      ___      o ",
        " o     \\___/     o ",
        " o              o  ",
        "  o            o   ",
        "   oooooooooooo    ",
        "       |  |        ",
        "    ___||||___     ",
        "   |          |    ",
        "   |   LOOK   |    ",
        "   |    AT    |    ",
        "   |    ME!   |    ",
        "   |__________|    "
    ]
    loading_chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    for frame in range(50):
        clear_screen()
        print("\n" * 3)
        print_centered("=" * 40, width, "36")
        print_centered("KIRKLAND MR. MEESEEKS SYSTEM", width, "33")
        print_centered("=" * 40, width, "36")
        print("\n" * 2)
        for line in meeseeks_art:
            print_centered(line, width, "32")
        print("\n" * 2)
        progress = frame * 2
        if progress > 100: progress = 100
        bar_length, filled_length = 30, int(30 * progress // 100)
        bar = '█' * filled_length + '░' * (bar_length - filled_length)
        print_centered(f"Loading... {progress}%", width, "35")
        print_centered(f"[{bar}]", width, "34")
        print_centered(f"{loading_chars[frame % len(loading_chars)]} Initializing Meeseeks Protocol...", width, "37")
        time.sleep(0.1)
    clear_screen()
    print("\n" * 8)
    print_centered("SYSTEM LOADED SUCCESSFULLY!", width, "32")
    print_centered("Welcome to Kirkland Mr. Meeseeks Terminal", width, "33")
    print("\n" * 2)
    print_centered("Press ENTER to continue...", width, "36")
    input()

def get_key():
    try:
        import msvcrt
        return msvcrt.getch().decode('utf-8')
    except ImportError:
        import tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def display_menu(options):
    width, _ = get_terminal_size()
    selected = 0
    while True:
        clear_screen()
        print("\n" * 2)
        print_centered("╔" + "═" * 38 + "╗", width, "36")
        print_centered("║     KIRKLAND MR. MEESEEKS MENU     ║", width, "36")
        print_centered("╚" + "═" * 38 + "╝", width, "36")
        print("\n" * 3)
        for i, option in enumerate(options):
            if i == selected:
                print_centered(f"< {option.upper()} >", width, "93")
            else:
                print_centered(f"  {option}  ", width, "37")
            print()
        print("\n" * 3)
        print_centered("Use ↑/↓ (W/S) to navigate, ENTER to select, Q to quit", width, "35")
        try:
            key = get_key()
        except:
            key = input("Enter command (w/s/enter/q): ").lower()
            if key == 'w': key = 'w'
            elif key == 's': key = 's'
            elif key == 'q': key = 'q'
            elif key == '': key = '\r'
        if key.lower() == 'w' or key == '\x1b[A':
            selected = (selected - 1) % len(options)
        elif key.lower() == 's' or key == '\x1b[B':
            selected = (selected + 1) % len(options)
        elif key == '\r' or key == '\n':
            return selected
        elif key.lower() == 'q':
            return -1

def execute_option(option_text):
    width, _ = get_terminal_size()
    clear_screen()
    print("\n" * 5)
    if option_text.lower() == "exit program":
        print_centered("👋 GOODBYE!", width, "31")
        print_centered("Thanks for using Kirkland Mr. Meeseeks!", width, "37")
        time.sleep(2)
        return False
    elif option_text.lower() == "start new session":
        print_centered("🚀 STARTING NEW SESSION...", width, "32")
        print_centered("Initializing Meeseeks Protocol...", width, "37")
        time.sleep(2)
        print_centered("Ready to help! I'm Mr. Meeseeks, look at me!", width, "33")
    elif option_text.lower() == "load previous data":
        print_centered("📁 LOADING PREVIOUS DATA...", width, "34")
        print_centered("Scanning for previous sessions...", width, "37")
        time.sleep(2)
        print_centered("No previous data found. Starting fresh!", width, "33")
    elif option_text.lower() == "system settings":
        print_centered("⚙️ SYSTEM SETTINGS", width, "35")
        print_centered("Configuration menu would go here...", width, "37")
        time.sleep(2)
        print_centered("Settings saved successfully!", width, "32")
    else:
        print_centered(f"🔹 {option_text}", width, "36")
        print_centered("This feature is under construction!", width, "37")
    print("\n" * 2)
    print_centered("Press ENTER to return to menu...", width, "36")
    input()
    return True

def run_meeseeks_menu(options):
    """Main entry point for external use"""
    try:
        print_loading_art()
        while True:
            selected = display_menu(options)
            if selected == -1:
                break
            if not execute_option(options[selected]):
                break
        clear_screen()
    except KeyboardInterrupt:
        clear_screen()
        print("\n\nProgram interrupted by user. Goodbye!")
        sys.exit(0)
