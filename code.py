
RESET = "\033[0m"
CYAN = "\033[96m"
GREEN = "\033[92m"
GRAY = "\033[90m"
WHITE = "\033[97m"

user = f"{GREEN}mateus{RESET}@{GREEN}bsod{RESET}"

ascii_art = [
        "   +--------------+",
        "  /|             /|",
        " / |            / |",
        "*--+-----------*  |",
        "|  |           |  |",
        "|  |           |  |",
        "|  |           |  |",
        "|  +-----------+--+",
        "| /            | /",
        "|/             |/",
        "*--------------*",

]

info = [
    ("OS", "Ubuntu and Windows"),
    ("Host", "BSOD Technologies, Inc."),
    ("Kernel", "BSOD Operating System"),
    ("IDE", "Sublime Text, VSCode"),

    ("", ""),

    ("Languages.Programming", "C, CPP, C#, Python, Rust, JavaScript"),
    ("Languages.Computer", "HTML, CSS, JSON, LaTeX"),
    ("Languages.Real", "Português"),

    ("", ""),

    ("Hobbies.Software", "Minecraft and GTA:SA Modding"),
    ("Hobbies.Hardware", "Create what's in my mind"),

    ("", ""),

    ("LinkedIn", "mateus-bsod"),
    ("Discord", "mateusbsod"),
]

print(f"{user} {GRAY}{'─'*60}{RESET}\n")

width = 20
max_lines = max(len(ascii_art), len(info))

for i in range(max_lines):

    left = ascii_art[i] if i < len(ascii_art) else ""
    
    if i < len(info):
        key, value = info[i]
        if key:
            right = f"{CYAN}{key:<22}{GRAY}:{RESET} {WHITE}{value}{RESET}"
        else:
            right = ""
    else:
        right = ""

    print(f"{GREEN}{left:<{width}}{RESET}  {right}")
