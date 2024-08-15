from config import get_var
from enum import Enum, auto
from random import randint


class ColorMode(Enum):
    NONE = auto()
    RANDOM = auto()
    SLOW_RANDOM = auto()


BG: str = get_var("colors.background")
LINE: tuple[int, int, int] = tuple(int(get_var("colors.line")[i:i+2], 16) for i in (1, 3, 5))  # type: ignore
RANDOM_RATE = get_var("gamerules.line_color.random_line_colors_slowly_rate")


def get_mode():
    random_line_colors: bool = get_var("gamerules.line_color.random_line_colors")
    random_line_colors_slowly: bool = get_var("gamerules.line_color.random_line_colors_slowly")
    
    if random_line_colors and random_line_colors_slowly:
        raise ValueError("You must specify either random_line_colors or random_line_colors_slow")

    if not random_line_colors and not random_line_colors_slowly:
        return ColorMode.NONE
    
    if random_line_colors:
        return ColorMode.RANDOM
    
    return ColorMode.SLOW_RANDOM
MODE = get_mode()


def get_new_color_random_slowly(color: tuple[int, int, int]):
    r, g, b = color
    r += randint(-RANDOM_RATE, RANDOM_RATE)
    g += randint(-RANDOM_RATE, RANDOM_RATE)
    b += randint(-RANDOM_RATE, RANDOM_RATE)
    
    r = max(0, min(r, 255))
    g = max(0, min(g, 255))
    b = max(0, min(b, 255))
    
    return (r, g, b)

get_new_color = {
    ColorMode.NONE: lambda color: color,
    ColorMode.RANDOM: lambda _: (randint(0, 255), randint(0, 255), randint(0, 255)),
    ColorMode.SLOW_RANDOM: get_new_color_random_slowly,
}[MODE]
