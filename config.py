from libqtile import bar, layout, widget,hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen,KeyChord,ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os
import subprocess


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/')
    subprocess.call([home+'/autostart.sh'])

nord_dark = {
    'bg': "#24272d",
    'fg': "#a1a9b7",
    'fg_gutter': "#4b5668",
    'black': "#3b4252",
    'red': "#dc6069",
    'green': "#8dbb6e",
    'yellow': "#e1b86f",
    'blue': "#57a5ed",
    'magenta': "#b48ead",
    'cyan': "#4badba",
    'white': "#e5e9f0",
    'orange': "#c9826b",
    'pink': "#bf88bc",

    'light-yellow': '#e1b86f',
    'dark-yellow':  '#d79921',
    'lime':         '#43a047',
    'purple':       '#C8BD8B',
    'dark-blue':    '#458588',
    'light-cyan':   '#09c3ef',

    'widget-bg':    '#4c566a',
    'widget-fg':    '#eceff4',

    'box_bg': "#e3f2fd",
    'box_fg': "#262926",
    'box_active': "#eceff4",
    'box_inactive': "#2e3440",
    'block_highlight': "#262926",
    'box_highlight': "#bf616a",

    'border_active':    '#4badba',
    'border_inactive':  '#e1b86f',
}
mod = "mod4"
terminal = "kitty"
fileManager = "nautilus"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "x", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "p", lazy.spawn("/home/tejasm/.config/qtile/scripts/powermenu.sh"), desc="powermenu"),
    Key([mod], "r", lazy.spawn("/home/tejasm/.config/rofi/launchers/type-7/launcher.sh"), desc="Launch Rofi"),
    Key([mod], "b",
        lazy.spawn("firefox"),
        desc="Firefox"
        ),

    Key([mod], "f",
        lazy.spawn(fileManager),
        desc="File"
        ),

    Key([mod], "c",
        lazy.spawn("rofi -modi 'clipboard:greenclip print' -show clipboard -run-command '{cmd}'"),
        desc="Clipboard"
        ),

    KeyChord([mod], "d",[
        Key([], "g",
            lazy.spawn("libreoffice")
            ),
        Key([], "b",
            lazy.spawn("libreoffice --base")
            ),
        Key([], "d",
            lazy.spawn("libreoffice --writer")
            ),
        Key([], "p",
            lazy.spawn("libreoffice --draw")
            ),
        Key([], "e",
            lazy.spawn("libreoffice --calc")
            ),
        Key([], "p",
            lazy.spawn("libreoffice --impress")
            )
    ]
             ),

    Key([], "Print",
        lazy.spawn("gnome-screenshot -a"),
        desc="File"
        ),

    Key([mod], "m",
        lazy.spawn("thunderbird"),
        desc="Mail"
        ),

    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl set +2%")
    ),

    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl set 2%-")
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn('pactl set-sink-volume 0 -5%'),
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn('pactl set-sink-volume 0 +5%'),
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn('pactl set-sink-mute 0 toggle'),
    ),
]
groups = [
    Group(
        '1',
        label=" ",
        layout="monadtall"
    ),
    Group(
        '2',
        label=" ",
        layout="monadtall"
    ),
    Group(
        '3',
        label=" ",
        layout="column"
    ),
    Group(
        '4',
        label=" ",
        layout="stack"
    ),
    Group(
        '5',
        label=" ",
        layout="stack"
    ),
    Group(
        '6',
        label=" ",
        layout="max"
    ),
    Group(
        '7',
        label=" ",
        layout="max"
    ),
    Group(
        '8',
        label=" ",
        layout="monadtall"
    ),
    Group(
        '9',
        label=" ",
        layout="monadtall"
    ),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_focus=[nord_dark["fg"]],
        border_width=2,
        margin=[3,3,3,3]
    ),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.Spiral(
        border_focus=[nord_dark["fg"]],
        border_width=2,
        margin=[3,3,3,3]
    ),
    layout.Matrix(
        border_focus=[nord_dark["fg"]],
        margin=[3,3,3,3]
    ),
    layout.MonadTall(
        border_focus=[nord_dark["fg"]],
        border_width=2,
        margin=3
    ),
    layout.Max(
        margin=[3,3,3,3]
    ),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]
widget_defaults = dict(
    font="Monaspice Nerd Font",
    fontsize=15,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    highlight_method='line',
                    hide_unused=True
                ),
                widget.Spacer(),
                widget.Clock(
                    format='%I:%M %p',
                ),
                widget.Spacer(),
                widget.Systray(
                    icon_size=25,
                ),
                widget.Battery(
                    format = "󰁹 {percent:2.0%}",
                ),
                # widget.NetGraph(
                #     type='line',
                #     line_width=1,
                #     border_width=0
                # )
            ],
            30,
            background='#262926',
        ),
    ),
]
groups.append(
        ScratchPad('scratchpad',
                   [
                       DropDown(
                           'term',
                           terminal,
                           width = 0.4,
                           height = 0.5,
                           x=0.3,
                           y=0.1,
                           opacity=0.8
                           ),
                       DropDown(
                           'File-manager',
                           fileManager,
                           width=0.5,
                           height=0.6,
                           x=0.25,
                           y=0.1,
                           opacity=1
                           ),
                       DropDown(
                           'Wallpaper',
                           'nitrogen',
                           width=0.4,
                           height=0.5,
                           x=0.3,
                           y=0.1,
                           opacity=1
                           ),
                       DropDown(
                           'Calender',
                           'gnome-calendar',
                           width=0.4,
                           height=0.5,
                           x=0.3,
                           y=0.1,
                           opacity=1
                           ),
                       ]
                   )
        )
# extend keys list with keybinding for scratchpad
keys.extend(
    [
    Key(
        ["control"],
        "1",
        lazy.group['scratchpad'].dropdown_toggle('term')
    ),
    Key(
        ["control"],
        "2",
        lazy.group['scratchpad'].dropdown_toggle('File-manager')
    ),
    Key(
        ["control"],
        "3",
        lazy.group['scratchpad'].dropdown_toggle('Wallpaper')
        ),
    Key(
        ["control"],
        "4",
        lazy.group['scratchpad'].dropdown_toggle('Calender')
        ),
    ]
)
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=[nord_dark["bg"]],
    border_normal = '#98971a',
    border_width = 2,
    margin = 2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
