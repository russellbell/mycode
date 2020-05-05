import shutil
import os

os.chdir("H:\CodeRepo\mycode\\")

shutil.move("raynor.obj", 'lab15\ceph_storage')

xname = input('What is the new name of kerrigan.obj ')

shutil.move('lab15\kerrigan.obj', 'lab15\ceph_storage\\' + xname)
