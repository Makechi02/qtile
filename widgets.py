import os
from libqtile import widget
from libqtile.lazy import lazy

from functions import PWA

colors = [
    ["#292d3e", "#292d3e"],     # panel background
    ["#434758", "#434758"],     # background for current screen tab
    ["#ffffff", "#ffffff"],     # font color for group names
    # border line color for current tab
    ["#bc13fe", "#bc13fe"],     # Group down color
    ["#8d62a9", "#8d62a9"],     # border line color for other tab and odd widgets
    ["#668bd7", "#668bd7"],     # color for the even widgets
    ["#e1acff", "#e1acff"],     

    ["#000000", "#000000"],
    ["#AD343E", "#AD343E"],
    ["#f76e5c", "#f76e5c"],
    ["#F39C12", "#F39C12"],
    ["#F7DC6F", "#F7DC6F"],
    ["#f1ffff", "#f1ffff"],
    ["#4c566a", "#4c566a"],
]

terminal = 'gnome-terminal'

def separator(pad = 0, foreground = 0, background = 0):
    separator = widget.Sep(
        linewidth = 0,
        padding = pad,
        foreground = colors[foreground],
        background = colors[background]
    )

    return separator

def powerline(foreground, background = 0):
    powerline = widget.TextBox(
        text = '',
        background = colors[background],
        foreground = colors[foreground],
        padding = 0,
        fontsize = 37
    )

    return powerline

widgets = [            
    separator(6, 2),

    widget.Image(
        filename = "~/.config/qtile/icons/terminal-iconx14.png",
        mouse_callbacks = {
            # 'Button1': lambda qtile: qtile.cmd_spawn('dmenu_run -p "Run: "')
            'Button1': lambda qtile: qtile.cmd_spawn('rofi -show drun')
        }
    ),
                
    separator(5, 2),

    widget.GroupBox(
        font = "The Bomb",
        fontsize = 13,
        margin_y = 3,
        margin_x = 3,
        padding_y = 10,
        padding_x = 10,
        borderwidth = 1,
        active = colors[-2],
        inactive = colors[-1],
        rounded = False,
        # highlight_color = colors[9],
        #highlight_method = "line",
        highlight_method = 'block',
        urgent_alert_method = 'block',
        # urgent_border = colors[9],
        this_current_screen_border = colors[9],
        this_screen_border = colors[4],
        other_current_screen_border = colors[0],
        other_screen_border = colors[0],
        foreground = colors[2],
        background = colors[0],
        disable_drag = True
    ),

    widget.Prompt(
        prompt = lazy.spawncmd(),
        font = "JetBrainsMono Nerd Font",
        padding = 10,
        foreground = colors[3],
        background = colors[1]
    ),

    separator(40, 2),

    widget.WindowName(
        foreground = colors[6],
        background = colors[0],
        padding = 10,
        fontsize = 14
    ),

    powerline(11, 0),

    widget.TextBox(
        text = " 🖬",
        foreground = colors[7],
        background = colors[11],
        padding = 0,
        fontsize = 14
    ),

    widget.Memory(
        foreground = colors[7],
        background = colors[11],
        mouse_callbacks = {
            'Button1': lambda qtile: qtile.cmd_spawn(terminal + ' -e htop')
        },
        padding = 5
    ),

    powerline(10, 11),

    widget.TextBox(
        text = "  ",
        foreground = colors[7],
        background = colors[10],
        padding = 0,
        mouse_callbacks = {
            "Button1": lambda qtile: qtile.cmd_spawn("pavucontrol")
        }
    ),

    widget.Volume(
        foreground = colors[7],
        background = colors[10],
        padding = 5
    ),

    powerline(9, 10),

    widget.CurrentLayoutIcon(
        # custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
        foreground = colors[0],
        background = colors[9],
        padding = 0,
        scale = 0.7
    ),

    widget.CurrentLayout(
        foreground = colors[7],
        background = colors[9],
        padding = 5
    ),

    powerline(8, 9),

    widget.Clock(
        foreground = colors[7],
        background = colors[8],
        mouse_callbacks = {
            "Button1": lambda qtile: qtile.cmd_spawn(PWA.calendar())
        },
        format = "%B %d  [ %H:%M ]"
    ),

    separator(10, 0, 8),

    powerline(0, 8),

    widget.Systray(
        background = colors[0],
        padding = 10
    ),

    separator(10),
]


widget_defaults = {
    'font': "Choco cooky",
    'fontsize': 15,
    'padding': 1,
    'background': colors[0]
}
extension_defaults = widget_defaults.copy()

