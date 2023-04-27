#!/bin/bash

pamixer -i 5
pamixer --get-volume-human | xargs dunstify -r 20
