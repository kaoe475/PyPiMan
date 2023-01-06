import sh

def pip_list():
    items = []
    for line in sh.pip("list").split("\n"):
        if "Package" in line or "--" in line or not line:
            continue
        items.append(Item(line.rsplit()[0]))
    return items

def pip_install(title):
    try:
        proc = sh.pip("install", title)
        return f"{proc}"
    except sh.ErrorReturnCode as err:
        return str(err)

def pip_uninstall(title):
    try:
        proc = sh.pip("uninstall", "-y", title)
        return f"{proc}"
    except sh.ErrorReturnCode as err:
        return str(err)

class Item:
    about = "None"

    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title

    def get_about(self):
        try:
            self.about = sh.pip('show', self.title)
        except sh.ErrorReturnCode as err:
            print(err)