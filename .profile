xrandr --newmode "1360x768_60.00"   84.75  1360 1432 1568 1776  768 771 781 798 -hsync +vsync
xrandr --addmode VGA1 1360x768_60.00
xrandr --output LVDS1 --mode 1024x600 --primary --pos 0x0 --rotate normal --output VGA1 --mode 1360x768_60.00 --dpi 98 --pos 1024x0 --rotate normal --output VIRTUAL1 --off

xrandr --addmode VGA-1 "1360x768_60.00"
xrandr --output LVDS-1 --mode 1024x600 --pos 0x0 --rotate normal --output VGA-1 --mode 1360x768_60.00 --dpi 98 --pos 1024x0 --rotate normal

xinput set-prop "SynPS/2 Synaptics TouchPad" 266  1
xinput set-prop "SynPS/2 Synaptics TouchPad" 279  0, 1, 0

picom &
nm-applet &
udiskie -t &
volumeicon &
nitrogen --restore &
setxkbmap -layout latam &
