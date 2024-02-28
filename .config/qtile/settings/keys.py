from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
mod = "mod4"
terminal = "kitty"
home = os.getenv('HOME', default='')
terminal_aux = guess_terminal()

keys = [
    #Keys own for Apps
    Key([mod], "l",lazy.spawn("rofi -show drun -show-icons"),desc="Open Apps"),
    Key([mod], "c",lazy.spawn("rofi -show calc -modi calc -no-show-match -no-sort"),desc="Open calculator"),
    Key([mod], "x",lazy.spawn("rofi -show window --show-icons -theme ~/.config/rofi/window.rasi"),desc="Show windows"),
    Key([mod], "t",lazy.spawn("telegram-desktop"),desc="Open Telegram"),
    Key([mod], "f",lazy.spawn("firefox"),desc="Open Firefox"),
    Key([mod], "b",lazy.spawn("brave"),desc="Open Brave"),
    Key([mod], "e",lazy.spawn("thunar"),desc="Open Thunar"),
    Key([mod], "m",lazy.spawn("thunderbird"),desc="Open mail"),
    Key([mod, "control"], "b",lazy.spawn("betterlockscreen -l"),desc="lock screen"),

    #Change the scrot save folder
    Key([mod], "q",lazy.spawn(home + "/.config/qtile/settings/scripts/scrot.sh full"),desc="screenshot"),
    Key([mod], "o",lazy.spawn(home + "/.config/qtile/settings/scripts/scrot.sh"),desc="screenshot select"),
    
    Key([mod], "p",lazy.spawn(home + "/.config/rofi/powermenu/powermenu.sh"),desc="Open powermenu"),

    #Key pavucontrol
    Key([mod, "control"],"v",lazy.spawn("pavucontrol"),desc="Control Volume"),
    
    #Volume control
    Key([mod, "control"], "0",lazy.spawn(home + "/.config/qtile/settings/scripts/changevolume.sh up"),desc="Increase Volume"),
    Key([mod, "control"], "9",lazy.spawn(home + "/.config/qtile/settings/scripts/changevolume.sh down"),desc="Decrease Volume"),

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
    Key([mod, "control"], "Return", lazy.spawn(terminal_aux), desc="Launch terminal"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    #Layout Control
    Key([mod, "control"], "h", lazy.layout.left()),
    Key([mod, "control"], "l", lazy.layout.right()),
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    Key([mod, "shift"], "i", lazy.layout.grow()),
    Key([mod, "shift"], "m", lazy.layout.shrink()),
    Key([mod, "shift"], "n", lazy.layout.normalize()),
    Key([mod, "shift"], "o", lazy.layout.maximize()),
    Key([mod, "shift"], "space", lazy.layout.flip()),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

]
