xrandr --newmode "1360x768"   85.25  1360 1440 1576 1784  768 771 781 798 -hsync +vsync
xrandr --addmode VGA1 1360x768
xrandr --output LVDS1 --mode 1024x600 --primary --pos 0x0 --rotate normal --output VGA1 --mode 1360x768 --pos 1024x0 --rotate normal --output VIRTUAL1 --off
picom &
nitrogen --restore &
setxkbmap -layout latam &
