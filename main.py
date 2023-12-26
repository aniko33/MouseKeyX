import os
import pystray
import tomllib
import psutil

from PIL import Image

CURRENT_DIR = "/".join(__file__.split("/")[:-1])

BINDINGS_FOLDER = os.path.join(os.environ["HOME"], ".config", "mousekeyx")
CONFIG_FILE = tomllib.load(open(os.path.join(CURRENT_DIR, "resource", "config.toml"), "rb"))

if not os.path.exists(BINDINGS_FOLDER):
    os.mkdir(BINDINGS_FOLDER)

# Config vars
theme_dark: bool = CONFIG_FILE["tray"]["theme_dark"]

def quit(tray: pystray.Icon):
    open(os.path.join(os.environ["HOME"], ".xbindkeysrc"), "w")
    for proc in psutil.process_iter():
        if proc.name() == "xbindkeys":
            proc.kill()

    tray.stop()

def reload(tray: pystray.Icon):
    tray.menu = refresh_menu()
    tray.update_menu()

def refresh_menu():
    configs_file = os.listdir(BINDINGS_FOLDER)
    configs = []

    for filename in configs_file:
        configs.append(pystray.MenuItem(filename, set_config))

    menu = pystray.Menu(
        pystray.MenuItem("Configs", pystray.Menu(*configs)),
        pystray.MenuItem("Reload", reload),
        pystray.MenuItem("Quit", quit),
    )

    return menu

def set_config(_, item: pystray._base.MenuItem):
    with open(os.path.join(BINDINGS_FOLDER, item.text), "r") as f:
        src = f.read()

    with open(os.path.join(os.environ["HOME"], ".xbindkeysrc"), "w") as f:
        f.write(src)
    
    for proc in psutil.process_iter():
        if proc.name() == "xbindkeys":
            proc.kill()

    os.system("xbindkeys")
    
def main():
    icon_path = os.path.join(CURRENT_DIR, "main_black.png")

    if theme_dark:
        icon_path = os.path.join(CURRENT_DIR, "main_white.png")

    icon = pystray.Icon("MouseKeyX", Image.open(icon_path), "MouseKeyX", refresh_menu())
    icon.run()

if __name__ == "__main__":
    main()