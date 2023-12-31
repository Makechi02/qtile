#!/usr/bin/env bash
# ---
# Use "run program" to run it only if it is not already running
# Use "program &" to run it regardless
# ---
# NOTE: This script runs with every restart of AwesomeWM
# TODO: run_once


function run {
    if ! pgrep $1 > /dev/null ;
    then
        $@&
    fi
}

nm-applet &
blueman-applet &

# run picom -CGb &
run picom &
run nitrogen --restore & 
run /usr/lib/polkit-kde-authentication-agent-1 &
run megasync
run xfce4-clipman
run gammy
run dunst
