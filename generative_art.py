import os
import time
import sys
import random

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_terminal_size():
    """Get terminal dimensions"""
    try:
        columns, rows = os.get_terminal_size()
        return columns, rows
    except:
        return 80, 24

def print_centered(text, width, color_code="37"):
    """Print text centered with color"""
    padding = (width - len(text)) // 2
    print(f"\033[{color_code}m{' ' * padding}{text}\033[0m")

def print_loading_art():
    """Display loading screen with ASCII art"""
    width, height = get_terminal_size()
    
    # Mr. Meeseeks ASCII art
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
    
    # Loading animation
    loading_chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    
    for frame in range(50):  # Loading animation frames
        clear_screen()
        
        # Print title
        print("\n" * 3)
        print_centered("=" * 40, width, "36")
        print_centered("KIRKLAND MR. MEESEEKS SYSTEM", width, "33")
        print_centered("=" * 40, width, "36")
        print("\n" * 2)
        
        # Print ASCII art
        for line in meeseeks_art:
            print_centered(line, width, "32")
        
        print("\n" * 2)
        
        # Loading bar
        progress = frame * 2
        if progress > 100:
            progress = 100
            
        bar_length = 30
        filled_length = int(bar_length * progress // 100)
        bar = '█' * filled_length + '░' * (bar_length - filled_length)
        
        print_centered(f"Loading... {progress}%", width, "35")
        print_centered(f"[{bar}]", width, "34")
        print_centered(f"{loading_chars[frame % len(loading_chars)]} Initializing Meeseeks Protocol...", width, "37")
        
        time.sleep(0.1)
    
    # Final loading message
    clear_screen()
    print("\n" * 8)
    print_centered("SYSTEM LOADED SUCCESSFULLY!", width, "32")
    print_centered("Welcome to Kirkland Mr. Meeseeks Terminal", width, "33")
    print("\n" * 2)
    print_centered("Press ENTER to continue...", width, "36")
    input()

def get_key():
    """Get single key press (cross-platform)"""
    try:
        import msvcrt
        return msvcrt.getch().decode('utf-8')
    except ImportError:
        import tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            key = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return key

def display_menu():
    """Display interactive menu"""
    width, height = get_terminal_size()
    
    options = [
        "Start New Session",
        "Load Previous Data", 
        "System Settings",
        "Exit Program"
    ]
    
    selected = 0
    
    while True:
        clear_screen()
        
        # Header
        print("\n" * 2)
        print_centered("╔" + "═" * 38 + "╗", width, "36")
        print_centered("║     KIRKLAND MR. MEESEEKS MENU     ║", width, "36")
        print_centered("╚" + "═" * 38 + "╝", width, "36")
        print("\n" * 3)
        
        # Menu options
        for i, option in enumerate(options):
            if i == selected:
                # Selected option with bright color and brackets
                print_centered(f"< {option.upper()} >", width, "93")  # Bright yellow text
            else:
                # Normal option
                print_centered(f"  {option}  ", width, "37")  # White text
            print()
        
        print("\n" * 3)
        print_centered("Use ↑/↓ (W/S) to navigate, ENTER to select, Q to quit", width, "35")
        
        # Get user input
        try:
            key = get_key()
        except:
            # Fallback for systems where get_key() doesn't work
            key = input("\nEnter command (w/s/enter/q): ").lower()
            if key == 'w':
                key = 'w'
            elif key == 's':
                key = 's'
            elif key == 'q':
                key = 'q'
            elif key == '':
                key = '\r'
        
        # Handle input
        if key.lower() == 'w' or key == '\x1b[A':  # Up arrow or W
            selected = (selected - 1) % len(options)
        elif key.lower() == 's' or key == '\x1b[B':  # Down arrow or S
            selected = (selected + 1) % len(options)
        elif key == '\r' or key == '\n':  # Enter
            return selected
        elif key.lower() == 'q':  # Quit
            return -1

def execute_option(option_index):
    """Execute selected option"""
    width, height = get_terminal_size()
    
    options = [
        "Start New Session",
        "Load Previous Data", 
        "System Settings",
        "Exit Program"
    ]
    
    clear_screen()
    print("\n" * 5)
    
    if option_index == 0:
        print_centered("🚀 STARTING NEW SESSION...", width, "32")
        print_centered("Initializing Meeseeks Protocol...", width, "37")
        time.sleep(2)
        print_centered("Ready to help! I'm Mr. Meeseeks, look at me!", width, "33")
        
    elif option_index == 1:
        print_centered("📁 LOADING PREVIOUS DATA...", width, "34")
        print_centered("Scanning for previous sessions...", width, "37")
        time.sleep(2)
        print_centered("No previous data found. Starting fresh!", width, "33")
        
    elif option_index == 2:
        print_centered("⚙️ SYSTEM SETTINGS", width, "35")
        print_centered("Configuration menu would go here...", width, "37")
        time.sleep(2)
        print_centered("Settings saved successfully!", width, "32")
        
    elif option_index == 3:
        print_centered("👋 GOODBYE!", width, "31")
        print_centered("Thanks for using Kirkland Mr. Meeseeks!", width, "37")
        time.sleep(2)
        return False
    
    print("\n" * 2)
    print_centered("Press ENTER to return to menu...", width, "36")
    input()
    return True

def main():
    """Main program function"""
    try:
        # Show loading screen
        print_loading_art()
        
        # Main menu loop
        while True:
            selected_option = display_menu()
            
            if selected_option == -1:  # Quit
                break
                
            if not execute_option(selected_option):  # Exit program
                break
                
    except KeyboardInterrupt:
        clear_screen()
        print("\n\nProgram interrupted by user. Goodbye!")
        sys.exit(0)

if __name__ == "__main__":
    main()