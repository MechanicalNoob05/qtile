#!/bin/bash

while getopts 'lim' OPTION; do
  case "$OPTION" in
    l)
        pamixer -d 5
        pamixer --get-volume-human | xargs dunstify -r 20
      ;;
    i)
        pamixer -i 5
        pamixer --get-volume-human | xargs dunstify -r 20
      ;;
    m)
        pamixer -t
        pamixer --get-volume-human | xargs dunstify -r 20
      ;;
    ?)
      echo "script usage: $(basename \$0) [-l] [-h] [-a somevalue]" >&2
      exit 1
      ;;
  esac
done
shift "$(($OPTIND -1))"
