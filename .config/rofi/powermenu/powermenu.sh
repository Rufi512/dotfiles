#!/usr/bin/env bash

SCRIPT_DIR=$(dirname $(realpath $0))

LOCK="󰌾"
LOGOUT="󰍃"
RESTART=""
SHUTDOWN="󰚥"

list_icons() {
    echo $SHUTDOWN
    echo $RESTART
    echo $LOCK
    echo $LOGOUT
}

handle_option() {
    case "$1" in
        "$SHUTDOWN")
            systemctl poweroff
            ;;
        "$LOCK")
            [ -x "$(command -v dunst)" ] && dunstctl set-paused true
            betterlockscreen -l
            [ -x "$(command -v dunst)" ] && dunstctl set-paused false
            ;;
        "$LOGOUT")
            qtile cmd-obj -o cmd -f shutdown || openbox --exit
            ;;
        "$RESTART")
            systemctl reboot
            ;;
       
    esac
}

SELECTION="$(list_icons | rofi -dmenu -theme ~/.config/rofi/powermenu/options-menu.rasi -selected-row 2)"
handle_option $SELECTION
