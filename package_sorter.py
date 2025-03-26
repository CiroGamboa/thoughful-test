def sort(width: int, height: int, length: int, mass: float) -> str:
    """Classifies a package as 'STANDARD', 'SPECIAL', or 'REJECTED' based on its size and mass.

    - 'STANDARD': Not bulky and not heavy.
    - 'SPECIAL': Either bulky or heavy, but not both.
    - 'REJECTED': Both bulky and heavy.

    A package is bulky if any dimension ≥ 150 cm or its volume ≥ 1,000,000 cm³.
    A package is heavy if its mass ≥ 20 kg.

    Args:
        width (int): Width in cm.
        height (int): Height in cm.
        length (int): Length in cm.
        mass (float): Mass in kg.

    Returns:
        str: Package category ('STANDARD', 'SPECIAL', or 'REJECTED').

    Raises:
        TypeError: If inputs are not numbers.
        ValueError: If all dimensions are ≤ 0 or mass is negative.
    """

    # Define limits as constants
    DIM_LIMIT = 150
    VOL_LIMIT = 1_000_000
    MASS_LIMIT = 20

    # Validate that all inputs are numbers (int or float)
    if not all(isinstance(dim, (int, float)) for dim in (width, height, length, mass)):
        raise TypeError("All inputs must be numbers.")

    # Validate input values (no negative or zero values allowed)
    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        raise ValueError("All dimensions and mass must be greater than zero.")

    # Define conditions for bulky and heavy
    is_bulky = (
        max(width, height, length) >= DIM_LIMIT
        or (width * height * length) >= VOL_LIMIT
    )
    is_heavy = mass >= MASS_LIMIT

    # Determine the package category
    if is_bulky and is_heavy:
        return "REJECTED"
    if is_bulky or is_heavy:
        return "SPECIAL"
    return "STANDARD"


# Test cases
def test_package_sorter():
    """Runs test cases to validate package classification logic."""

    # Standard package
    assert sort(10, 10, 10, 10) == "STANDARD"

    # Bulky packages
    assert sort(100, 100, 100, 10) == "SPECIAL"  # Volume-based bulky
    assert sort(150, 10, 10, 10) == "SPECIAL"  # Dimension-based bulky

    # Heavy package
    assert sort(10, 10, 10, 20) == "SPECIAL"

    # Rejected package (both bulky and heavy)
    assert sort(150, 100, 100, 20) == "REJECTED"

    # Edge cases (just at the limit)
    assert sort(150, 10, 10, 19.99) == "SPECIAL"  # Bulky but not heavy
    assert sort(10, 10, 10, 20) == "SPECIAL"  # Heavy but not bulky
    assert sort(150, 10, 10, 20) == "REJECTED"  # Both bulky and heavy

    # Input validation tests
    try:
        sort(-10, -10, -10, 5)  # All dimensions are negative
    except ValueError as e:
        assert str(e) == "All dimensions and mass must be greater than zero."

    try:
        sort(0, 0, 0, 5)  # All dimensions are zero
    except ValueError as e:
        assert str(e) == "All dimensions and mass must be greater than zero."

    try:
        sort(10, 10, 10, -5)  # Negative mass
    except ValueError as e:
        assert str(e) == "All dimensions and mass must be greater than zero."

    try:
        sort("10", 10, 10, 5)  # Invalid type (string)
    except TypeError as e:
        assert str(e) == "All inputs must be numbers."

    try:
        sort(10, 10, 10, "5")  # Invalid type (string)
    except TypeError as e:
        assert str(e) == "All inputs must be numbers."

    print("All test cases passed!")


if __name__ == "__main__":
    test_package_sorter()
