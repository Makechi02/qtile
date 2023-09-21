
import os
import subprocess

from libqtile import hook

# Local Files
from keys.keybindings import mouse, Keybindings
from layouts import layouts, floating_layout
from groups import groups, group_names
from widgets import widget_defaults, extension_defaults
from screen import screens

 
###### MAIN ######
if __name__ in ["config", "__main__"]:
    # Initializes keybindings
    obj_keys          = Keybindings()
    keys              = obj_keys.init_keys()
    keys              += obj_keys.init_keys_groups(group_names)


dgroups_key_binder = None
dgroups_app_rules = []                      # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
respect_minimize_requests = True
wmname = "LG3D"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.client_new
def dialogs(window):
    if(window.window.get_wm_type() == 'dialog' or window.window.get_wm_transient_for()):
        window.floating = True
