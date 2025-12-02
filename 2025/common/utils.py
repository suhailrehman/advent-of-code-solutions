"""
Common AOC Utilities
"""

from typing import Callable, Any

def process_input(filename: str, fn: Callable[[str], Any]) -> list[Any]:
    """ Process each line of the input file using the provided function"""
    data = []
    with open(filename, encoding="utf-8") as fp:
        for line in fp:
            line = line.strip()
            data.append(fn(line))
    return data
