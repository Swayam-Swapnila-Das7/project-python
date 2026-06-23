try:
    import os
    import platform
    import subprocess
    import sys
    from datetime import datetime

    if platform.system() == "Windows" or sys.platform == "win32":
        os.system("color")
      
except ImportError:
    print('''
  [!] Critical Error: Core modules failed to import.
  Please verify your Python environment and dependencies.
        ''')
    exit()
except Exception as e:
    print(f'[!] Unexpected Initialization Error: {e}')
    exit()

banner = r'''
  /$$$$$$  /$$$$$$$  /$$   /$$             /$$$$$$$  /$$$$$$$$ /$$$$$$$$ /$$$$$$  /$$$$$$ /$$        /$$$$$$ 
 /$$__  $$| $$__  $$| $$  | $$            | $$__  $$| $$_____/|__  $$__//$$__  $$|_  $$_/| $$       /$$__  $$
| $$  \__/| $$  \ $$| $$  | $$            | $$  \ $$| $$         | $$  | $$  \ $$  | $$  | $$      | $$  \__/
| $$      | $$$$$$$/| $$  | $$            | $$  | $$| $$$$$      | $$  | $$$$$$$$  | $$  | $$      |  $$$$$$ 
| $$      | $$____/ | $$  | $$            | $$  | $$| $$__/      | $$  | $$__  $$  | $$  | $$       \____  $$
| $$    $$| $$      | $$  | $$            | $$  | $$| $$         | $$  | $$  | $$  | $$  | $$       /$$  \ $$
|  $$$$$$/| $$      |  $$$$$$/            | $$$$$$$/| $$$$$$$$   | $$  | $$  | $$ /$$$$$$| $$$$$$$$|  $$$$$$/
 \______/ |__/       \______/             |_______/ |________/   |__/  |__/  |__/|______/|________/ \______/ 
                                                                                                             
'''

# Terminal Color Codes
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
PURPLE = "\033[0;35m"
RESET = "\033[0m"

# Print Header & developer details
print(PURPLE + banner + RESET)
print(YELLOW + "    [Developer : Swayam]")
print(YELLOW + "    [LinkedIn  : https://www.linkedin.com/in/swayam-swapnila-das]")
print('\n' + '='*55 + '\n')


def check_os():
    """Validates if the current Operating System supports the tool's requirements."""
    current_os = platform.system()
    if current_os in ['Linux', 'Android']:
        return True
    else:
        print(RED + f'\n[-] Compatibility Error: This tool is unsupported on {current_os}.' + RESET)
        print(YELLOW + '[!] Requirement: Linux or Android environment is required.' + RESET)
        return False 


def cpu_details():
    """Executes the system call to retrieve CPU hardware specifications."""
    try: 
        command = subprocess.run(
            ['lscpu'],
            capture_output=True,
            text=True
        )
        if command.returncode == 0:
            return command.stdout
        else:
            print(RED + "\n[-] Dependency Error: 'lscpu' utility is missing or failed to execute." + RESET)
            print(BLUE + "[*] Suggestion: Install 'lscpu' via your system package manager." + RESET)
            return None
    except Exception as e:
        print(RED + f'\n[-] Execution Error: {e}' + RESET)
        return None


def get_info():
    """Fetches and displays CPU metrics directly inside the terminal window."""
    if check_os():
        print(BLUE + "\n[*] Fetching system hardware metrics..." + RESET)
        details = cpu_details()
        if details:
            print("\n" + GREEN + "-"*40 + "\n[ SYSTEM CPU SPECIFICATIONS ]\n" + "-"*40 + RESET)
            print(details)
            print(GREEN + "-"*40 + RESET)


def export_report():
    """Generates a text-based hardware report asset and alerts the user."""
    if check_os():
        details = cpu_details()
        if not details:
            return

        now = datetime.now()
        filename = 'cpu_details.txt'

        try:
            with open(filename, 'w') as file:
                file.write('='*45 + '\n')
                file.write(f'          HARDWARE INVENTORY REPORT          \n')
                file.write(f'  Generated On : {now.strftime("%d %b %Y")} | {now.strftime("%I:%M %p")}\n')
                file.write('='*45 + '\n\n')
                file.write(details)
                file.write('\n' + '='*45 + '\n')
                file.write('                End of Report                \n')
                file.write('='*45 + '\n')
            
            # Success messages consolidated directly inside the execution step
            print(GREEN + "\n[+] Success: Hardware diagnostic report generated successfully!" + RESET)
            print(BLUE + "[*] Saved File: 'cpu_details.txt'" + RESET)
            
        except Exception as e:
            print(RED + f'\n[-] File System Error: Unable to write data: {e}' + RESET)


# Main Interactive CLI Loop
while True:
    print(PURPLE + '\n[ MAIN INTERFACE ]' + RESET)
    print(BLUE + '  [1] Print CPU Details to Terminal' + RESET)
    print(BLUE + '  [2] Export CPU Details to Text File' + RESET)
    print(BLUE + '  [3] Terminate Program' + RESET)
    
    choice = input('\nSelect option ID (1-3): ').strip()
    
    match choice:
        case '1':
            get_info()
        case '2':
            export_report()
        case '3':
            print(GREEN + "\n[+] Session closed safely !" + RESET)
            break 
        case _:
            print(RED + '\n[-] Invalid Input: Please specify a choice between available valid options !' + RESET)
