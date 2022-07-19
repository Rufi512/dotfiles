from libqtile import bar, layout, widget
from libqtile.config import Screen
from settings.widgets import widgets
from settings.get_resolutions import screens, screen_connected, resolutions_screens, resolutions_avalaibles, max_resolution_position

#Set color on bar
try:
    from settings.colors import read_json
    color = read_json()
    color_bar = color['bar']
except:
    color_bar = '#ffffffFF'

#Set bar on monitor high width

if (int(screen_connected) > 1):
    for screen in resolutions_avalaibles:
        if (resolutions_avalaibles.index(screen) == max_resolution_position):
            screens.append(Screen(bottom=bar.Bar(widgets, 26, opacity=1, background=color_bar)))
        else:
            screens.append(Screen())
else:
    screens.append(Screen(bottom=bar.Bar(widgets, 24, opacity=1, background=color_bar)))
