from libqtile import widget
from libqtile import qtile

#Mouse Callbacks

def Wifi(qtile):
    qtile.cmd_spawn('nm-connection-editor')

def Htop(qtile):
    qtile.cmd_spawn('kitty -e htop')

#Widgets

widgets =   [
               widget.GroupBox(fontsize=26,
                               padding_x=5,
                               padding_y=8,
                               disable_drag=True,
                               highlight_method='block',
                               inactive='#5e5e5e',
                               this_current_screen_border='#138edb',
                               this_screen_border='#383b3d'),
                widget.Prompt(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },

                    name_transform=lambda name: name.upper(),
                ),
                widget.WindowName(fontsize=12),
                widget.TextBox(text='',fontsize=33,foreground='#ff33ba',padding=0),
                widget.Memory(format='{MemUsed:.0f}M/{MemTotal:.0f}M',mouse_callbacks={'Button1': Htop},foreground = '#ff33ba'),
                widget.Spacer(length=7),
                widget.TextBox(text='',mouse_callbacks={'Button1': Wifi},fontsize=34,foreground='#00cee8',padding=0),
                widget.Spacer(length=5),
                widget.Wlan(interface="wlp2s0",mouse_callbacks={'Button1': Wifi},fontsize=12,format='{essid}',foreground="#00cee8",padding=0),
                widget.Spacer(length=2),
                widget.Net(interface="wlp2s0",mouse_callbacks={'Button1': Wifi},fontsize=13,format='{up}↑|↓{down}',foreground='#00cee8'),
                widget.Spacer(length=2),
                widget.Pomodoro(color_active='#48e34f', color_inactive='#5081f1', foreground='ffffff',color_break='#db9e3b',length_long_break=10,prefix_inactive

="Let's fucking code",length_pomodori=35,length_short_break=5,notification_on=True),

                widget.Systray(padding=8),
                widget.Spacer(length=4),
                widget.Clock(padding=2,fontsize=14,format='%Y-%m-%d %a [%H:%M]',timezone="America/Caracas"),
                widget.Spacer(length=4),
                widget.CurrentLayoutIcon(fontsize=10),
                widget.Spacer(length=2),
            ]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=4
)
extension_defaults = widget_defaults.copy()

