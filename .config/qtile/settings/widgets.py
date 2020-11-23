from libqtile import widget 



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
                widget.WindowName(fontsize=14),
                widget.Memory(format='{MemUsed}M/{MemTotal}M',foreground = '#ff33ba'),
                widget.Net(interface="wlp2s0",foreground='#00cee8'),
                widget.Systray(padding=8),
                widget.Clock(fontsize=14,format='%Y-%m-%d %a %I:%M %p'),
            ]
 


widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=4,
    opacity=0.80,
)
extension_defaults = widget_defaults.copy()

