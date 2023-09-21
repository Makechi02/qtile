from libqtile.config import Group

group_names = ["M", "A", "K", "E", "C", "H", "I"]

groups = [
    Group(name, layout = "floating") if name == group_names[0]
    else Group(name, layout = "monadtall")
    if name == group_names[-1] else Group(name, layout = "max")
    for name in group_names
]
