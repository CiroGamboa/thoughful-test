# Package Sorter

## Overview
This Python script classifies packages into three categories: **STANDARD**, **SPECIAL**, or **REJECTED** based on their dimensions and weight. The classification is determined using predefined thresholds for bulkiness and heaviness.

## Classification Rules
- **STANDARD**: The package is neither bulky nor heavy.
- **SPECIAL**: The package is either bulky or heavy, but not both.
- **REJECTED**: The package is both bulky and heavy.

### Criteria
A package is considered **bulky** if:
- Any of its dimensions (width, height, or length) is **≥ 150 cm**.
- Its volume (**width × height × length**) is **≥ 1,000,000 cm³**.

A package is considered **heavy** if:
- Its mass is **≥ 20 kg**.

## Installation
Ensure you have Python 3 installed on your system.

```sh
# Clone the repository
git clone <your-repository-url>
cd <your-repository-folder>

# Run the script
python package_sorter.py
```

## Usage
Import the function and use it in your Python code:

```python
from package_sorter import sort

# Example usage
category = sort(width=100, height=100, length=100, mass=10)
print(category)  # Output: "SPECIAL"
```

## Input Validation
The function ensures that:
- All input values (width, height, length, and mass) must be **greater than zero**.
- If an invalid input is provided, a `ValueError` is raised.

## Running Tests
To verify the functionality, run the included test cases:

```sh
python package_sorter.py
```

If all tests pass, you will see:

```
All test cases passed!
```

## License
This project is licensed under the MIT License.

---

Let me know if you need additional details or formatting adjustments!


