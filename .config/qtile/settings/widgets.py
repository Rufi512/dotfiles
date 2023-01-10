from libqtile import widget, qtile
from settings.get_resolutions import resolutions_avalaibles
fontsize_value = 12
fontsize_icon = 23
#Mouse Callbacks

def Wifi():
    qtile.cmd_spawn('nm-connection-editor')

def Htop():
    qtile.cmd_spawn('kitty -e htop')

#Set color text
try:
    from settings.colors import read_json
    color = read_json()
    color_text = color['text']
except:
    color_text = '#ffffffFF'

#Set font Size

try:
    longer = len(resolutions_avalaibles)
    if int(resolutions_avalaibles[longer-1][:-3]) > 1300 :
        fontsize_value = 12
        fontsize_icon = 24
    else:
        fontsize_value = 12
        fontsize_icon = 23
except:
    fontsize_value = 12

widgets =   [
               widget.GroupBox(fontsize=20,
                               padding_x=6,
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
                widget.WindowName(format="",fontsize=fontsize_value),
                widget.Spacer(length=7),
                widget.TextBox(text='|',fontsize=33,padding=0,foreground=color_text,),
                widget.TextBox(text='',fontsize=fontsize_icon,padding=3,foreground="#f93a7b",),
                widget.Memory(format='{MemUsed:.0f}M/{MemTotal:.0f}M',mouse_callbacks={'Button1': Htop}, foreground=color_text, fontsize=fontsize_value,),
                widget.Spacer(length=2),
                widget.TextBox(text='|',fontsize=33,padding=0, foreground=color_text,),
                widget.Spacer(length=3),
                widget.TextBox(text='',mouse_callbacks={'Button1': Wifi},fontsize=fontsize_icon,padding=3, foreground="#49a4ed",),
                widget.Spacer(length=4),
                widget.Net(mouse_callbacks={'Button1': Wifi},fontsize=fontsize_value,format='Speed: {up}  | {down} ', foreground=color_text,),
                #widget.TextBox(text='|',fontsize=33,padding=0,foreground=color_text),
                #widget.Spacer(length=2),
                #widget.TextBox(text="", fontsize=22, foreground="#f3b644"),
                #widget.GenPollText(update_interval=500, func=lambda:subprocess.call([os.path.expanduser("~/.config/qtile/scripts/track_info.sh"), "tauon"]).decode("utf-8"),mouse_callbacks={'Button1':lambda:subprocess.call([os.path.expanduser("~/.config/qtile/scripts/track_info.sh"), "tauon", "PLAY"]), 'Button2':lambda:subprocess.call([os.path.expanduser("~/.config/qtile/scripts/track_info.sh"), "tauon", "PAUSE"])}),
                widget.TextBox(text='|',fontsize=33,padding=0,foreground=color_text),
                widget.TextBox(padding=5,text="",fontsize=18, foreground="#ef203d"),
                widget.ThermalSensor(tag_sensor='Package id 0'),
                widget.TextBox(text='|',fontsize=33,padding=0, foreground=color_text),
                widget.Systray(padding=8, icon_size=19),
                widget.Spacer(length=8),
                widget.TextBox(text='|',fontsize=33,padding=0, foreground=color_text),
                widget.TextBox(text="",fontsize=fontsize_icon, foreground="#e7a237"),
                widget.Clock(padding=2,fontsize=fontsize_value,format='%Y-%m-%d %a [%H:%M]',foreground=color_text),
                widget.Spacer(length=4),
                widget.CurrentLayoutIcon(fontsize=10,foreground=color_text,),
                widget.Spacer(length=2),
            ]

widget_defaults = dict(
    font='MesloLGS NF',
    fontsize=fontsize_value,
    padding=4
)
extension_defaults = widget_defaults.copy()

