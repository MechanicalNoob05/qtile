#!/bin/bash

pamixer -d 5
pamixer --get-volume-human | xargs dunstify -r 20
