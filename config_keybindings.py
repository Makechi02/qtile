"""
MODIFY THIS FILE TO CREATE CUSTOM KEYBINDINGS

Keybindings are configured with tuples, inside Predifined lists Variables
"""

from libqtile.confreader import ConfigError

# Import default mod keys
from keys.default import *
from functions import PWA
from os.path import expanduser

HOME = expanduser("~")

# Define constants here
# TERMINAL = "alacritty"
TERMINAL = "gnome-terminal"
BROWSER = "google-chrome"

# Basic window manager movements

# Qtile shutdown/restart keys
SHUTDOWN_MODIFIER = [MOD, CONTROL]
RESTART           = "r"
SHUTDOWN          = "q"

# Group movement keys:
GROUPS_KEY     = CONTROL
SWAP_GROUP_KEY = SHIFT

NEXT_GROUP = "period"
PREV_GROUP = "comma"


# --------------- HARDWARE_CONFIGS --------------- #
HARDWARE_KEYS = [
    # VOLUME
    ([], "XF86AudioLowerVolume", "pactl set-sink-volume @DEFAULT_SINK@ -5%"),
    ([], "XF86AudioRaiseVolume", "pactl set-sink-volume @DEFAULT_SINK@ +5%"),
    ([], "XF86AudioMute", "pactl set-sink-mute @DEFAULT_SINK@ toggle"),
     
    # BRIGHTNESS
    ([], "XF86MonBrightnessUp", "brightnessctl set +10%"),
    ([], "XF86MonBrightnessDown", "brightnessctl set 10%-"),
]


APPS = [
    ([MOD], "Return", TERMINAL),
    ([MOD],      "e", "thunar"),
    ([MOD, ALT], "d", "emacs"),
    ([MOD, ALT], "o", "env LIBGL_ALWAYS_SOFTWARE=1 obs"),
    ([MOD, ALT], "v", "gvim"),
    ([MOD],      "b", BROWSER),
    ([MOD, ALT], "c", "code"),
    ([MOD, ALT], "a", "pavucontrol"),
    ([MOD, ALT], "e", "vim -g .config/qtile/config.py"),
    ([MOD, ALT], "z", "zoom"),

    # MEDIA HOTKEYS
    ([MOD],      "Up", "pulseaudio-ctl up 5"),
    ([MOD],      "Down", "pulseaudio-ctl down 5"),
    
    # Makes reference to play-pause script
    # You can find it in my scripts repository
    ([ALTGR],    "space", "play-pause"),
   
    # ROFI
    # ([MOD], "space", 'rofi -modi "drun,power-menu:rofi-power-menu,run,window,ssh" -show drun -show-icons'),
    ([ALT], "space", 'rofi -show drun'),

    # SCREENSHOT
    ([],         "Print", "xfce4-screenshooter"),
    # FULL SCREEN SCREENSHOT
    ([ALT],      "Print", "xfce4-screenshooter -f -c"),

    # TERMINAL APPS
    ([MOD, ALT], "n", TERMINAL + " -e nvim"),
    
]


CUSTOM_SPAWN_KEYS = [
    # PWA keys
    ([MOD, ALT], "s", PWA.spotify()),
    ([MOD, ALT], "m", PWA.music()),
    ([MOD, ALT], "t", PWA.calendar()),
    ([MOD, ALT], "y", PWA.youtube()),
    ([MOD, ALT], "l", PWA.notion()),
    ([MOD, ALT], "h", PWA.habitica()),
]


SPAWN_KEYS = HARDWARE_KEYS + APPS + CUSTOM_SPAWN_KEYS 

SPAWN_CMD_KEYS = [
    # Takes full screenshot and creates a file on the screenshot folder
    ([SHIFT],    "Print", f"xfce4-screenshooter -f -s {HOME}/Pictures/Screenshots/"),
]
