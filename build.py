import os, re

PROJECTS = ["hackmate", "hackmate-hwdb", "hackmate-core", "hackmate-goldengate"]
SECTIONS = {
    "Introduction": ["Prerequisites", "Overview", "Supported Hardware"],
    "Installation": ["Creating the USB", "Booting the Installer", "Installing macOS", "Post-Install"],
    "Configuration": ["Config Basics", "Kernel Patches", "Drivers", "Boot Arguments"],
    "Troubleshooting": ["Boot Issues", "Graphics Issues", "Kernel Panics", "FAQ"],
    "About": ["Changelog", "Credits"],
}
slug = lambda s: re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

root = open("index.html").read()
NAV = re.search(r"<nav>.*?</nav>", root, re.S).group(0)
HEAD = root.split("<link rel=\"stylesheet\"")[0]

def page(depth, current, title):
    up = "../" * depth
    local = "" if depth == 1 else "../"
    aside = ""
    for sec, chs in SECTIONS.items():
        aside += f'<div class="section">{sec}</div>'
        for c in chs:
            cls = "chapter active" if c == current else "chapter"
            aside += f'<a class="{cls}" href="{local}{slug(c)}/">{c}</a>'
    nav = re.sub(r'href="(\.\./)*index.html"', f'href="{up}index.html"', NAV)
    return (f'{HEAD}<link rel="stylesheet" href="{up}style.css">\n</head><body>{nav}'
            f'<aside>{aside}</aside><div class="page"><h1>{title}</h1></div></body></html>\n')

for p in PROJECTS:
    os.makedirs(p, exist_ok=True)
    open(f"{p}/index.html", "w").write(page(1, None, p))
    for chs in SECTIONS.values():
        for c in chs:
            d = f"{p}/{slug(c)}"
            os.makedirs(d, exist_ok=True)
            open(f"{d}/index.html", "w").write(page(2, c, c))
