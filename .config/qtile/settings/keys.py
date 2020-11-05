from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    #Keys own for Apps
    Key([mod], "l",lazy.spawn("rofi -show drun"),desc="Open Apps"),
    Key([mod], "t",lazy.spawn("telegram-desktop"),desc="Open Telegram"),
    Key([mod], "f",lazy.spawn("firefox"),desc="Open Firefox"),
    Key([mod], "e",lazy.spawn("thunar"),desc="Open explore file"),
    Key([mod], "q",lazy.spawn("scrot"),desc="screenshot"),
    Key([mod], "p",lazy.spawn("rofi -show run"),desc="Open All Apps"),

    #Key pavucontrol
    Key([mod, "control"],"v",lazy.spawn("pavucontrol"),desc="Control Volume"),
    # Keys Redshift
    Key([mod, "control"],"o",lazy.spawn("redshift -O 3600k"),desc="Redshift Active"),
    Key([mod, "control"],"p",lazy.spawn("redshift -x"),desc="Redshift Inactive"),

    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "j", lazy.layout.up(),
        desc="Move focus up in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "control"], "j", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(),
        desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

]
