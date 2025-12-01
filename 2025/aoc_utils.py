from typing import Any, Callable


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
