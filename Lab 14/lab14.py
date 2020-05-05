import shutil
import os

# move into the working directory

os.chdir('H:\CodeRepo\mycode\Lab 14')

shutil.copy("filetocopy.txt", 'H:\CodeRepo\mycode\Lab 14\copyto\\filetocopy.txt')

# shutil.copytree("copyto", "copyto.backup")
