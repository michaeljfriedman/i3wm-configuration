#!/bin/bash

icon="$HOME/.config/i3/lock-icon.png"
tmpbg="/tmp/screen.png"
scrot "$tmpbg"
convert "$tmpbg" -scale 5% -scale 2000% -brightness-contrast -5% "$tmpbg"
convert "$tmpbg" "$icon" -gravity Center -composite -matte "$tmpbg"
i3lock --image="$tmpbg" --pointer=default
