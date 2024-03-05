#!/usr/bin/env bash

time=$(date '+%Y-%m-%d %A [%I-%M-%S %p]')
dir="/mnt/win/arch_folder/screenshots"
file="$dir/$time.png"
full="$1"

function notify_view() {
	if [[ -e "$file" ]]; then
		notify-send -i "$file" -a Scrot -u low Screenshot "Screenshot Saved!"
		else
		notify-send -a Scrot "Screenshot Cancelled!"
	fi
}

function call_scrot() {
	if [[ -n "$full" ]]; then
		scrot "$file"
		else
	  scrot -fs "$file"
	fi
	wait
	notify_view

}

call_scrot
