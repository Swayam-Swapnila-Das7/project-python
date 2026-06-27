try :
    import os
    import shutil
    import platform
    from pathlib import Path
    import sys
    import time
  
    if platform.system() == "Windows" or sys.platform == "win32":
        os.system("color")

except ImportError :
    print('''
  [!] Critical Error: Core modules failed to import.
  Please verify your Python environment and dependencies.
        ''')
    exit()
except Exception as e:
    print(f'[!] Unexpected Initialization Error: {e}')
    exit()

  
Banner = r'''
888888 88 88     888888      dP"Yb  88""Yb  dP""b8    db    88b 88 88 8888P 888888 88""Yb 
88__   88 88     88__       dP   Yb 88__dP dP   `"   dPYb   88Yb88 88   dP  88__   88__dP 
88""   88 88  .o 88""       Yb   dP 88"Yb  Yb  "88  dP__Yb  88 Y88 88  dP   88""   88"Yb  
88     88 88ood8 888888      YbodP  88  Yb  YboodP dP""""Yb 88  Y8 88 d8888 888888 88  Yb 
'''

# Terminal Color Codes
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
PURPLE = "\033[0;35m"
RESET = "\033[0m"

format = {
      #Documents
      ".pdf" : "Documents",
      ".txt" : "Documents",
      ".xlsx" : "Documents",
      ".pptx" : "Documents",
      ".doc" : "Documents",
      ".docx" : "Documents",
      ".csv" : "Documents",

      #images
      ".jpeg" : "Images",
      ".png" : "Images",
      ".jpg" : "Images",
      ".gif" : "Images",
      ".svg" : "Images",
      ".webp" : "Images",
  
      #audio
      ".mp3" : "Audio",
      ".opus" : "Audio",
      ".m4a" : "Audio",

      #video
      ".mp4" : "Video",
      ".mkv" : "Video",

      #archive
      ".zip" : "Archive",

      #code
      ".py" : "Code",
      ".c" : "Code",
      ".html" : "Code",
      ".css" : "Code",
      ".js" : "Code",
      ".rs" : "Code"
}

current_directory = str(os.getcwd())
script_name = Path(__file__).name

# Print Header & developer details
print(PURPLE + Banner + RESET)
print(YELLOW + "    [Developer : Swayam]" + RESET)
print(YELLOW + "    [LinkedIn  : https://www.linkedin.com/in/swayam-swapnila-das]" + RESET)
print(YELLOW + "    [GitHub    : https://github.com/Swayam-Swapnila-Das7]" + RESET)
print('\n' + '='*55 + '\n')

def count_before() :

    file_count = 0
    dir_count = 0

    try :
        # os.scandir yields lightweight DirEntry objects
        for entry in os.scandir('.'):
            
            if entry.is_file(follow_symlinks=False):
                file_count += 1
            elif entry.is_dir(follow_symlinks=False):
                dir_count += 1

        print(
    PURPLE + 'File counts in Selected Directory : \n' + RESET +
            BLUE + f'''
    [!]Total: {file_count + dir_count}
    [!]Files: {file_count} 
    [!]Dirs: {dir_count}''' + RESET
    )
    except Exception as e :
        print(RED + f'[-]Error : {e} ' + RESET)
        return


def count_after() :

    try :
        print(PURPLE + 'Counting files moved in each folder : ' + RESET)
        for folder in set(format.values()) :
            total_files = len(os.listdir(folder))
            print( BLUE +
            f'''
        {folder}  :  {total_files}
            ''' + RESET
            )
    except Exception as e :
        print(RED + f'[-]Error : {e} ' + RESET)
        return
            

def organize() :
    count_before()
     # Create directories if they do not exist
    try : 
        print(YELLOW + 'Checking  for folders (Creating if not exist ).....\n'+RESET)
        for extension in set(format.values()) :
            if (not os.path.exists(extension)) :
                os.mkdir(extension)
      
            if (not os.path.exists('Miscellaneous')) :
                os.mkdir('Miscellaneous')
    except Exception as e :
        print(RED + f'[-]Error : {e}' + RESET)
        return
    print(GREEN + '[+] Folder checking completed .\n'+ RESET)
                
    try : 
        print(YELLOW + 'Start moving files.....\n' + RESET)
        # Scan the current working directory
        for entry in os.scandir('.') :
            # Moving the current script may break the code or raise an error, so avoid moving it
            if entry.name == script_name :
                continue
            file_path = Path(entry)
            # Move them to their respective folders, except for the current script file
            if file_path.suffix.lower() in format:
                shutil.move(file_path,f'{my_directory}/{format[file_path.suffix.lower()]}')
        
            # Move all other files to the Miscellaneous directory
            elif entry.is_file() :
                shutil.move(file_path,f'{my_directory}/Miscellaneous')
        print(GREEN + '[+] Task Completed' + RESET)
    except Exception as e :
        print(RED + f'[-]Error : {e} ' + RESET)
        return
    count_after()


def list_dir() :
    try :
        ls = os.listdir('.')
        print(PURPLE + f'     [*]Total {len(ls)} items found' + RESET)
        for data in ls :
            print(BLUE + f'     [@]{data}' + RESET)
    except Exception as e :
        print(RED + f'[-]Error : {e}' + RESET)
        return

def change_dir(my_directory) :
    try :
        os.chdir(my_directory)
        print(GREEN + f'     [*]Working Directory Change successfully' + RESET)
    except Exception as e :
        print(RED + f'[-]Error : {e}' + RESET)
        return


# Main Interactive CLI Loop
while True:
    print(PURPLE + '\n[ MAIN INTERFACE ]' + RESET)
    print(BLUE + '  [1] Change the working directory' + RESET)
    print(BLUE + '  [2] Show all files present in this directory' + RESET)
    print(BLUE + '  [3] Count the number of files and folders in the directory' + RESET)
    print(BLUE + '  [4] Organize Files' + RESET)
    print(BLUE + '  [5] Terminate Program' + RESET)
    
    choice = input('\nSelect option ID (1-5): ').strip() # strip function is use to remove leading and trailing spaces from input
    
    match choice:
        case '1':
            my_directory = input(PURPLE + 'Enter the directory Path you want to move : ' + RESET)
            change_dir(my_directory)
        case '2':
            list_dir()
        case '3' :
            count_before()
        case '4' :
            my_opp = input(PURPLE + ' Did you want to proced with current working directory(y/n) : ' + RESET).strip().lower()
            if my_opp == 'y' :
                organize()
            elif my_opp == 'n' :
                my_directory = input(PURPLE + 'Input your targeted directory path : '+ RESET)
                change_dir(my_directory)
                organize()
            else :
                print(RED + '\n[-] Invalid Input: Please specify a choice between available valid options !' + RESET)
        case '5':
            print(GREEN + "\n[+] Session closed safely !" + RESET)
            break 
        case _:
            print(RED + '\n[-] Invalid Input: Please specify a choice between available valid options !' + RESET)
