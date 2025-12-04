import os
from typing import Any, Callable, Optional

import requests
from dotenv import load_dotenv


def download_input(day: str | int, year: int, session_token: Optional[str] = "") -> bool:
    """Download the input for a given day and year from the Advent of Code website."""
    destination = os.path.join(os.getcwd(), f"day_{int(day):02d}_input.txt")
    if os.path.exists(destination):
        return True
    load_dotenv()
    session_token = session_token or os.getenv("AOC_SESSION_TOKEN")
    url = f"https://adventofcode.com/{year}/day/{int(day)}/input"
    headers = {"Cookie": f"session={session_token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    with open(destination, "w") as f:
        f.write(response.text.strip())
    return True


def compose(*functions: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """Compose multiple functions into a single function.

    Args:
        *functions: Variable number of functions to be composed.

    Returns:
        A function that applies the given functions in sequence.

    Examples:
        >>> def add_one(x):
        ...     return x + 1
        ...
        >>> def multiply_by_two(x):
        ...     return x * 2
        ...
        >>> def square(x):
        ...     return x ** 2
        ...
        >>> composed = compose(add_one, multiply_by_two, square)
        >>> composed(2)
        25
    """

    def composition(element: Any) -> Any:
        for function in functions:
            element = function(element)
        return element

    return composition
