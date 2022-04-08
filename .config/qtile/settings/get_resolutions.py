#Set bar on monitor high width
import subprocess

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
        "xrandr | grep -w 'connected' | cut -d ' ' -f3 - | cut -d '+' -f1 -", shell=True, stdout=subprocess.PIPE
    )
    .stdout.decode("UTF-8")
    .replace("x", "")
    .split("\n")[:-1]
)

resolutions_avalaibles = []

for resolution in resolutions_screens:
    split_resolution = resolution.split("_", 1)
    resolutions_avalaibles.append(split_resolution[0])

resolutions_avalaibles.sort()

max_resolution_position = resolutions_avalaibles.index(max(resolutions_avalaibles))