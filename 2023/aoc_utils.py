from typing import Any, Callable


def compose(*functions: Callable[[Any], Any]) -> Callable[[Any], Any]:
    def composition(element: Any) -> Any:
        for function in functions:
            element = function(element)
        return element

    return composition
