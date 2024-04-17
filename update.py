import os
import sys
from time import sleep
from zipfile import ZipFile

import requests


class Update():
    def __init__(self):
        self.version = '1.5.8'
        self.github = 'https://github.com/Vxlkz/rblx-xml-bypass-2024/tree/main'
        self.zipfile = 'https://github.com/Vxlkz/rblx-xml-bypass-2024/archive/refs/heads/main.zip'
        self.update_checker()

    def update_checker(self):
        code = requests.get(self.github).text
        if "self.version = '1.5.8'" in code:
            print('This version is up to date!')
            sleep(1)
            print('u can now open .png to run the builder!')
            sleep(1)
            print('Exiting...')
            sleep(2)
            sys.exit()
        else:
            print('''
                    ███╗   ██╗███████╗██╗    ██╗    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██╗
                    ████╗  ██║██╔════╝██║    ██║    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
                    ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██║
                    ██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ╚═╝
                    ██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██╗
                    ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝
                                      this version is patched/outdated.''')
            choice = input('\nWould you like to update? (y/n): ')
            if choice.lower() == 'y':
                new_version_source = requests.get(self.zipfile)
                with open("rblx-xml-bypass-2024/main.zip", 'wb')as zipfile:
                    zipfile.write(new_version_source.content)
                with ZipFile("rblx-xml-bypass-2024/main.zip", 'r') as filezip:
                    filezip.extractall(path=os.path.join(os.path.expanduser("~"), "Downloads"))
                os.remove("rblx-xml-bypass-2024/main.zip")
                print('The new version is now in ur Downloads folder.\nUpdate Complete!')
                print("Exiting...")
                sleep(5)
            if choice.lower() == 'n':
                print('Exiting...')
                sleep(2)
                sys.exit()


if __name__ == '__main__':
    Update()
