from colorama import Fore, Style, init
from json import load, load
init(autoreset=True)

file = "data\data.json"

with open(file, "r") as f:
    data = load(f)
    version_ = data["version"]
with open("data\\api_key.json", "r") as a:
    ak = load(a)
    apikey = ak["api_key"]
    apikey_2 = ak["api_key_moviedb"]
with open("data\\config.json", "r") as j:
    dcj = load(j)
    bordercolor = dcj["bordercolor"]
    logocolor = dcj["logocolor"]
    callsign = dcj["callsign"]
    channelnukename = dcj["channelnukename"]
with open("data\\token.discord", "r") as d:
        dcf = load(d)
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

# Logo
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
        print(f"                                                 {bordercolor}║{sra} Version: {Fore.YELLOW}{version_}{bordercolor}   ║{sra}")
