from libqtile import layout
from libqtile.config import Match

default_conf = {
    "border_width": 2,
    "margin": 5,
    "border_focus": "#668bd7",
    "border_normal": "#1D2330"
}

layouts = [
    layout.Max(**default_conf),
    layout.MonadTall(**default_conf),
    layout.floating.Floating(**default_conf),
    layout.TreeTab(
        font = "JetBrainsMono Nerd Font",
        fontsize = 11,
        sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
        section_fontsize = 10,
        border_width = 2,
        bg_color = "#1c1f24",
        active_bg = "#c678dd",
        active_fg = "#000000",
        inactive_bg = "#a9a1e1",
        inactive_fg = "#1c1f24",
        padding_left = 0,
        padding_x = 0,
        padding_y = 5,
        section_top = 10,
        section_bottom = 20,
        level_shift = 8,
        vspace = 3,
        panel_width = 200
    ),
    # layout.Stack(num_stacks=2),
    # # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    # layout.MonadWide(**default_conf),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class = 'confirmreset'),         # gitk
    Match(wm_class = 'dialog'),               # Dialogs stuff
    Match(wm_class = 'makebranch'),           # gitk
    Match(wm_class = 'maketag'),              # gitk
    Match(wm_class = 'ssh-askpass'),          # ssh-askpass
    Match(title = 'branchdialog'),            # gitk
    Match(title = 'pinentry'),                # GPG key password entry
])
