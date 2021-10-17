
def installmods():
        import subprocess
        import sys
        import time
        import os
        import pkg_resources
        required = {'colorama', 'discord', 'pyowm', 'requests'}  # Here you can type in the modules that are needed.
        installed = {pkg.key for pkg in pkg_resources.working_set}
        missing = required - installed

        if missing:
            print("""Looks like there are missing modules, you haven't installed.
            I am gonna do that for you :)""")
            print("")
            python = sys.executable
            subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
        else:
            print("All modules are installed. :)")
            print("")
            time.sleep(2)
            os.system("cls")


from colorama import Fore, Style, init
import json
init(autoreset=True)

file = "data\data.json"

with open(file, "r") as f:
    data = json.load(f)
    version = data["version"]
with open("data\\api_key.json", "r") as a:
    ak = json.load(a)
    apikey = ak["api_key"]
with open("data\\config.json", "r") as j:
    dcj = json.load(j)
    bordercolor = dcj["bordercolor"]
    logocolor = dcj["logocolor"]
    callsign = dcj["callsign"]
    channelnukename = dcj["channelnukename"]
with open("data\\token.discord", "r") as d:
        dcf = json.load(d)
        token = dcf["token"]

if bordercolor == "red":
    bordercolor = Fore.RED
elif bordercolor == "blue":
    bordercolor = Fore.BLUE
elif bordercolor == "lightblue":
    bordercolor = Fore.LIGHTBLUE_EX
elif bordercolor == "lightred":
    bordercolor = Fore.LIGHTRED_EX
elif bordercolor == "green":
    bordercolor = Fore.GREEN
elif bordercolor == "lightgreen":
    bordercolor = Fore.LIGHTGREEN_EX
elif bordercolor == "grey":
    bordercolor = Fore.LIGHTBLACK_EX
elif bordercolor == "cyan":
    bordercolor = Fore.CYAN
elif bordercolor == "lightcyan":
    bordercolor = Fore.LIGHTCYAN_EX
elif bordercolor == "white":
    bordercolor = Fore.WHITE
elif bordercolor == "yellow":
    bordercolor = Fore.YELLOW
elif bordercolor == "lightyellow":
    bordercolor = Fore.LIGHTYELLOW_EX
elif bordercolor == "magenta":
    bordercolor = Fore.MAGENTA
elif bordercolor == "lightmagenta":
    bordercolor = Fore.LIGHTMAGENTA_EX
elif bordercolor == "lightwhite":
    bordercolor = Fore.LIGHTWHITE_EX
else:
    bordercolor = Fore.WHITE

if logocolor == "red":
    logocolor = Fore.RED
elif logocolor == "blue":
    logocolor = Fore.BLUE
elif logocolor == "lightblue":
    logocolor = Fore.LIGHTBLUE_EX
elif logocolor == "lightred":
    logocolor = Fore.LIGHTRED_EX
elif logocolor == "green":
    logocolor = Fore.GREEN
elif logocolor == "lightgreen":
    logocolor = Fore.LIGHTGREEN_EX
elif logocolor == "grey":
    logocolor = Fore.LIGHTBLACK_EX
elif logocolor == "cyan":
    logocolor = Fore.CYAN
elif logocolor == "lightcyan":
    logocolor = Fore.LIGHTCYAN_EX
elif logocolor == "white":
    logocolor = Fore.WHITE
elif logocolor == "yellow":
    logocolor = Fore.YELLOW
elif logocolor == "lightyellow":
    logocolor = Fore.LIGHTYELLOW_EX
elif logocolor == "magenta":
    logocolor = Fore.MAGENTA
elif logocolor == "lightmagenta":
    logocolor = Fore.LIGHTMAGENTA_EX
elif bordercolor == "lightwhite":
    logocolor = Fore.LIGHTWHITE_EX
else:
    logocolor = Fore.WHITE

class main:
    def hellomessage():
        sra = Style.RESET_ALL
        print(logocolor + """
                              ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                              ░░░░░░░░░   ░░░░░░░░░░░░░░░░   ░░░░░░░░░░░░░░░░░░░░░░░░░
                              ▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
                              ▒▒     ▒▒   ▒▒   ▒   ▒▒▒   ▒   ▒▒▒▒▒   ▒   ▒▒▒▒▒▒   ▒▒▒▒
                              ▓   ▓▓▓▓▓   ▓   ▓▓▓   ▓   ▓▓   ▓   ▓▓   ▓▓   ▓▓  ▓▓▓   ▓
                              ▓▓▓    ▓▓     ▓▓▓▓▓▓▓    ▓▓▓   ▓   ▓▓   ▓▓   ▓         ▓
                              ▓▓▓▓▓   ▓   ▓   ▓▓▓▓▓▓   ▓▓▓   ▓   ▓▓   ▓▓   ▓  ▓▓▓▓▓▓▓▓
                              █      ██   ██   ████   ████   █   █    ██   ███     ███
                              ████████████████████   █████████████████████████████████

""")
        print(f"                                                 {bordercolor}╔══════════════════╗{sra}               ")
        print(f"                                                 {bordercolor}║{Fore.LIGHTRED_EX}Made by {Fore.LIGHTCYAN_EX}@Skyline69{bordercolor}║{sra}")
        print(f"                                                 {bordercolor}║{sra} Version: {Fore.YELLOW}{version}{bordercolor}   ║{sra}")
