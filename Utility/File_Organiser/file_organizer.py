import os
import shutil
from pathlib import Path

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

cwd = os.getcwd()
script_name = Path(__file__).name

def organize_file() :
  # Create directories if they do not exist
  for extension in set(format.values()) :
    if (not os.path.exists(extension)) :
      os.mkdir(extension)
      
  if (not os.path.exists('Miscellaneous')) :
    os.mkdir('Miscellaneous')

  # Scan the current working directory
  with os.scandir('.') as entries :
    for entry in entries :
      # Moving the current script may break the code or raise an error, so avoid moving it
      if entry.name == script_name :
        continue
      file_path = Path(entry)
      # Move them to their respective folders, except for the current script file
      if file_path.suffix.lower() in [*format]:
        shutil.move(file_path,f'{cwd}/{format[file_path.suffix.lower()]}')
        
      ## Move all other files to the Miscellaneous directory
      elif entry.is_file() :
        shutil.move(file_path,f'{cwd}/Miscellaneous')

  # print after file organised
  print('All files are organized')

if __name__ == '__main__' :
  organize_file()

'''
NOTE :
    This script only works on files,
    not directories (folders). 
    They will remain untouched.
'''
