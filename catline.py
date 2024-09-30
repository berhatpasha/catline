# Libraries
import colorama
from colorama import Fore
colorama.init(autoreset=True)
import time
import getpass
import subprocess
from engine.kernel.pasword import crypter, uncrypter

# Theme
from theme import color_1, color_2, color_3, color_4, color_5, color_6, color_7, color_8

# system information
import sys
import os
import cpuinfo
import GPUtil
os_name = os.name
gpus = GPUtil.getGPUs()
cpu_info = cpuinfo.get_cpu_info()

os.system('clear')

if os_name == 'nt':
    pass
elif os_name == 'posix':
    print(f"{Fore.LIGHTYELLOW_EX}Catline was developed for windows only. See the github page for details")
    #sys.exit()
else:
    print(f"{Fore.LIGHTYELLOW_EX}Catline was developed for windows only. See the github page for details")
    #sys.exit()

for gpu in gpus:
    Gpu = gpu.name

print(f'''{color_2}
{color_5}GPU : {Gpu.split()[2]} {Gpu.split()[3]}{color_2} 
{color_5}CPU : {cpu_info['brand_raw'].split()[1]} {cpu_info['brand_raw'].split()[2]} {cpu_info['brand_raw'].split()[3]}{color_2}
{color_5}

{color_5}▓▓▓{color_6}▓▓▓{color_7}▓▓▓{color_8}▓▓▓{color_2}
{color_1}▓▓▓{color_2}▓▓▓{color_3}▓▓▓{color_4}▓▓▓{color_2}
        ''')



while True: ## main loop
    try: ## pass bugs


        def user():
            while True:
                userInput = input(f"{color_6}user-$ {color_8}").lower()
        
                if userInput.split()[0] == "sudo":
                    userInput = getpass.getpass(f"{color_6}PASWORD for ROOT : {color_7}")
                    if userInput == uncrypter():
                        print(f"{color_6}✓")
                        root()
                    else:
                        print(f"{color_4}x")
                elif userInput.split()[0] == "clear":
                    os.system('clear')
                elif userInput.split()[0] == "resetpass":
                    print(f"{color_3}You must have root authorization to change the password ")
                elif userInput.split()[0] == "ls":
                    os.system('ls')
                elif userInput.split()[0] == "cd":
                    os.chdir(userInput.split()[1])
                else:
                    try:
                        os.system(f'{userInput.split()[0]} {userInput.split()[1]} {userInput.split()[2]}')
                    except:
                        try:
                            os.system(f'{userInput.split()[0]} {userInput.split()[0]}')
                        except:
                            os.system(f'{userInput.split()[0]}')
        


        def root():
            while True:
                userInput = input(f"{color_6}root-$ {color_8}").lower()

                if userInput.split()[0] == "sudo":
                    print(f"{color_2} You are already a root user")
                elif userInput.split()[0] == "clear":
                    os.system('clear')
                elif userInput.split()[0] == "ls":
                    os.system('ls')
                elif userInput.split()[0] == "cd":
                    os.chdir(userInput.split()[1])
                else:
                    try:
                        os.system(f'{userInput.split()[0]} {userInput.split()[1]} {userInput.split()[3]}')
                    except:
                        try:
                            os.system(f'{userInput.split()[0]} {userInput.split()[1]}')
                        except:
                            os.system(f'{userInput.split()[0]}')
                    


        user()
    except:
        pass
