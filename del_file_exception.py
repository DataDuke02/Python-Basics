import os
import shutil

path= "floder"

try:
    #os.remove(path)     #delete a file
    #os.rmdir(path)      #delete an empty directory
    shutil.rmtree(path)  #delete a directory containing file
except FileNotFoundError:
    print("The file is not there")
except PermissionError:
    print("You do not have permission to delete that")
except OSError: #used for oserror when show up del a directory that have a file
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")
