#!/usr/bin/env bash

chosen=$(printf "  Power Off\n  Restart\n  Log Out" | rofi -dmenu -i )

case "$chosen" in
	"  Power Off") poweroff ;;
	"  Restart") reboot ;;
	"  Log Out") qtile cmd-obj -o cmd -f shutdown ;;
	*) exit 1 ;;
esac
