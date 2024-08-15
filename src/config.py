from functools import reduce
from typing import Any
import toml
from sys import argv

argv = argv[1:]
if len(argv) > 1:
    raise ValueError("Too many command-line arguments. Only one config file is supported.")
if len(argv) == 0:
    argv.append("config.toml")

try:
    config = toml.load(open(argv[0]))
except FileNotFoundError:
    with open("error.log", "w") as f:
        msg = f"[ERROR] Config file '{argv[0]}' not found"
        print(msg)
        f.write(f"{msg}")
    exit(1)

def get_var(name: str) -> Any:
    parts = name.split(".")
    return reduce(lambda item, part: item[part], parts, config)

LINE_LENGTH: int = get_var("other.line_length")
SET_BORDER_GAMERULE: bool = get_var("gamerules.set_borders")
TIMEOUT: int = get_var("gamerules.timeout")

SCREEN_WIDTH: int = get_var("window.width")
SCREEN_HEIGHT: int = get_var("window.height")
CAPTION: str = get_var("window.caption")
STARTING_POS: tuple[int, int] = get_var("other.starting_pos_x"), get_var("other.starting_pos_y")
