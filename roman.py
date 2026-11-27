"""Roman numeral conversion for the fizzbuzz --roman option.

Standard subtractive notation for integers from 1 to 3999 inclusive,
using only the letters I, V, X, L, C, D and M.
"""

_NUMERALS = (
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
)


def to_roman(n):
    """Return the Roman numeral string for an integer n from 1 to 3999.

    Uses standard subtractive notation, e.g. 4 -> 'IV', 1994 -> 'MCMXCIV'.

    Raises ValueError if n is an integer outside 1..3999, and TypeError
    if n is not an int (bool is rejected even though it subclasses int).
    """
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError(f"to_roman() requires an int, got {type(n).__name__}")
    if not 1 <= n <= 3999:
        raise ValueError(f"to_roman() requires an integer from 1 to 3999, got {n}")
    parts = []
    for value, numeral in _NUMERALS:
        count, n = divmod(n, value)
        parts.append(numeral * count)
    return "".join(parts)
