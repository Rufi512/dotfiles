from libqtile import widget
from libqtile import qtile

#Mouse Callbacks

def Wifi(qtile):
    qtile.cmd_spawn('nm-connection-editor')

def Htop(qtile):
    qtile.cmd_spawn('kitty -e htop')

#Set color text
try:
    from settings.colors import read_json
    color = read_json()
    color_text = color['text']
except:
    color_text = '#ffffffFF'

widgets =   [
               widget.GroupBox(fontsize=30,
                               padding_x=5,
                               padding_y=8,
                               disable_drag=True,
                               highlight_method='block',
                               active=color_text,
                               inactive="#a1a1a1",
                               #background="#ffffff",
                               foreground="#138edb",
                               this_current_screen_border='#082758',
                               this_screen_border='#383b3d'),
                widget.Prompt(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },

                    name_transform=lambda name: name.upper(),
                ),
                widget.WindowName(format="",fontsize=14),
                widget.Spacer(length=7),
                widget.TextBox(text='|',fontsize=40,padding=2,foreground=color_text,),
                widget.TextBox(text='',fontsize=40,padding=0,foreground="#f93a7b",),
                widget.Memory(format='{MemUsed:.0f}M/{MemTotal:.0f}M',mouse_callbacks={'Button1': Htop}, foreground=color_text, fontsize=14,),
                widget.Spacer(length=2),
                widget.TextBox(text='|',fontsize=40,padding=0, foreground=color_text,),
                widget.Spacer(length=7),
                widget.TextBox(text='',mouse_callbacks={'Button1': Wifi},fontsize=40,padding=0, foreground="#49a4ed",),
                widget.Spacer(length=8),
                widget.Wlan(interface="wlp2s0",mouse_callbacks={'Button1': Wifi},fontsize=14,format='{essid}',padding=0, foreground=color_text,),
                widget.Spacer(length=2),
                widget.Net(interface="wlp2s0",mouse_callbacks={'Button1': Wifi},fontsize=14,format='{up}↑ | {down}↓', foreground=color_text,),
                widget.TextBox(text='|',fontsize=40,padding=0,foreground=color_text),
                widget.Spacer(length=2),
                widget.TextBox(text="", fontsize=24, foreground="#e12116"),
                widget.Pomodoro(color_active='#48e34f', color_inactive=color_text, foreground=color_text,color_break='#db9e3b',length_long_break=10,prefix_inactive

="Let's fucking code!",length_pomodori=35,length_short_break=5,notification_on=True, fontsize=14),
                widget.TextBox(text='|',fontsize=40,padding=0,foreground=color_text),

                widget.Systray(padding=8, icon_size=20),
                widget.Spacer(length=8),
                widget.TextBox(text='|',fontsize=40,padding=0, foreground=color_text),
                widget.TextBox(text="",fontsize=36, foreground="#e7a237"),
                widget.Clock(padding=2,fontsize=14,format='%Y-%m-%d %a [%H:%M]',timezone="America/Caracas",foreground=color_text),
                widget.Spacer(length=4),
                widget.CurrentLayoutIcon(fontsize=10,foreground=color_text,),
                widget.Spacer(length=2),
            ]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=4
)
extension_defaults = widget_defaults.copy()

