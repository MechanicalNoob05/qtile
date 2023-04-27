#!/bin/bash

pamixer -t
pamixer --get-volume-human | xargs dunstify -r 20
