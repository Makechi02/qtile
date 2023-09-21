from libqtile import bar
from libqtile.config import Screen

from widgets import widgets

def init_widgets_screen():
    '''
    Function that returns the widgets in a list.
    It can be modified so it is useful if you  have a multimonitor system
    '''
    return widgets

def init_widgets_screen2():
    '''
    Function that returns the widgets in a list.
    It can be modified so it is useful if you  have a multimonitor system
    '''
    return widgets

screens = [
    Screen(top = bar.Bar(widgets = init_widgets_screen(), opacity = 0.8, size = 25)),
    Screen(top = bar.Bar(widgets = init_widgets_screen2(), opacity = 0.8, size = 25))
]
   