import os
import sys
# os.system('cmd /c "Your Command Prompt Command"')

os.makedirs("logs", exist_ok=True)

for i in range(1,sys.argv[0]+1):
    for (dirpath, dirnames, filenames) in os.walk("settings"):
        for (dirpath, dirnames, filenames) in os.walk("maps"):
            for (dirpath, dirnames, filenames) in os.walk("clients"):
