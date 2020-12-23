from libqtile import bar, layout, widget
from libqtile.config import Screen
from settings.widgets import widgets
import subprocess

#Set bar on monitor high width

screens=[]


connected_monitors = subprocess.run(
    "xrandr | grep 'connected'| cut -d ' ' -f 2",
    shell=True,
    stdout=subprocess.PIPE
).stdout.decode("UTF-8").split("\n")[:-1].count("connected")


resolutions_screens=subprocess.run(
    "xrandr | grep \* | cut -d' ' -f4 -",
    shell=True,
    stdout=subprocess.PIPE
).stdout.decode("UTF-8").replace('x','').split("\n")[:-1]

res=[]

for i in resolutions_screens:
    res.append(int(i))


max_resolution = res.index(max(res))

if(connected_monitors>1):
    for screen in res:
        if(res.index(screen) == max_resolution):
            screens.append(Screen(bottom=bar.Bar(widgets,24,opacity=0.92)))
        else:
            screens.append(Screen())
else:
    screens.append(Screen(bottom=bar.Bar(widgets,24,opacity=0.92)))
