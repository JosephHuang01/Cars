from components.common_game_color import CommonGameColor
from components.position import Position

# name, type, position, width, length, bg_color, fg_color
shape_specification = {
    'name': 'Shape',
    'type': 'shape',
    'position': Position(0, 0),
    'width': 50,
    'length': 50,
    'bg_color': CommonGameColor.GRAY,
    'fg_color': CommonGameColor.BLACK
}

print (shape_specification['name'])