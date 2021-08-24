from libqtile import bar, layout, widget
from libqtile.config import Screen
from settings.widgets import widgets
import subprocess

#Set bar on monitor high width

screens = []

xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"

screen_connected = subprocess.run(
    xrandr,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
).stdout.decode("UTF-8")

resolutions_screens = (
    subprocess.run(
        "xrandr | grep /* | cut -d' ' -f4 -", shell=True, stdout=subprocess.PIPE
    )
    .stdout.decode("UTF-8")
    .replace("x", "")
    .split("\n")[:-1]
)

resolutions_avalaibles = []

for resolution in resolutions_screens:
    split_resolution = resolution.split("_", 1)
    resolutions_avalaibles.append(split_resolution[0])

max_resolution = resolutions_avalaibles.index(max(resolutions_avalaibles))

if (int(screen_connected) > 1):
    for screen in resolutions_avalaibles:
        if (resolutions_avalaibles.index(screen) == max_resolution):
            screens.append(Screen(bottom=bar.Bar(widgets, 24, opacity=0.92)))
        else:
            screens.append(Screen())
else:
    screens.append(Screen(bottom=bar.Bar(widgets, 24, opacity=0.92)))
