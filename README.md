# Lab Assignment: Pizza Calculator
---

## Learning Objectives and Standards

**Objective:** Review Python fundamentals: variables, arithmetic operators, conditionals, and input/output formatting.

This lab aligns with the following standards:

- **AAP-1.A:** Represent a value with a variable.
- **AAP-1.B:** Determine the value of a variable as a result of an assignment.
- **AAP-2.B:** Represent a step-by-step algorithmic process using sequential code statements.
- **AAP-2.C:** Evaluate expressions that use arithmetic operators.

By completing this lab, you will:
1. Practice using **variables** and **assignment** to represent and determine values (AAP-1.A, AAP-1.B).
2. Represent algorithms using **sequential code statements** (AAP-2.B).
3. Evaluate **arithmetic expressions** and use them to solve problems (AAP-2.C).

---
## Overview

You and your partner have been elected to the prestigious **Pizza Council**. Your mission is to write a Python program that calculates how many pizzas are needed for an event, determines the total cost including a tip, and computes fun statistics like the total and per-person square inches of pizza ordered.

###  Pizza Data

The following table provides information about the various sized pizzas that you’ll need to implement this assignment.

| Pizza Size | Price    | Diameter   | People Fed |
|------------|----------|------------|------------|
| Large      | $14.68   | 20 inches  | 7 people   |
| Medium     | $11.48   | 16 inches  | 3 people   |
| Small      | $7.28    | 12 inches  | 1 person   |

### Constants

The program provides several constants for use in your calculations. These constants are defined in the `constants.py` file and are imported into your program using `from constants import *`.

#### Available Constants

| Constant Name      | Description                      | Value            |
|--------------------|----------------------------------|------------------|
| `PEOPLE_PER_LARGE` | Number of people a large pizza serves | 7              |
| `PEOPLE_PER_MEDIUM`| Number of people a medium pizza serves | 3              |
| `PEOPLE_PER_SMALL` | Number of people a small pizza serves | 1              |
| `DIAMETER_LARGE`   | Diameter of a large pizza in inches | 20             |
| `DIAMETER_MEDIUM`  | Diameter of a medium pizza in inches | 16            |
| `DIAMETER_SMALL`   | Diameter of a small pizza in inches | 12             |
| `COST_LARGE`       | Cost of a large pizza in dollars | 14.68           |
| `COST_MEDIUM`      | Cost of a medium pizza in dollars | 11.48           |
| `COST_SMALL`       | Cost of a small pizza in dollars | 7.28            |

---

## Tasks

You will need to implement three core functions (Tasks 1 to 3), each handling a specific aspect of the pizza calculation:

- **Task 1:** Calculate the number of large, medium, and small pizzas required.
- **Task 2:** Compute the total area of the pizzas ordered.
- **Task 3:** Calculate the total cost of the pizzas, including a tip.

After implementing these functions, you will complete **Task 4**, where you will integrate all three functions into a cohesive program. This program will prompt the user for input, call each function to process the data, and display the final results exactly as shown in the example outputs.

---

### Task 1: `calculate_pizzas`

#### Description
The `calculate_pizzas` function determines the number of large, medium, and small pizzas needed to serve a specified number of guests.

For example, if you have 9 guests, ordering two large pizzas would exceed the requirement. Instead, the function calculates that you would need one large pizza and two small pizzas to serve exactly 9 people.

*Hint: Use Python's floor division (`//`) and modulus (`%`) operators to calculate the number of pizzas efficiently.*

#### Details
- The function relies on constants that specify how many people each pizza size can feed.
- It calculates the pizza order by:
  - Prioritizing large pizzas.
  - Using medium and small pizzas to cover any remaining guests.
- Returns the result as a tuple of three integers:
  - `return large, medium, small`

---

### Task 2: `serving_size`

#### Description
The `serving_size` function computes the total area of pizzas ordered, given the number of large, medium, and small pizzas.

For example, if the order consists of **1 large pizza**, **2 medium pizzas**, and **0 small pizzas**, the total area is calculated using the formula for the area of a circle:
Area = π * (radius^2)
where the radius is half the diameter of the pizza. The total area would be:
- Area of 1 large pizza = π * (10^2) = 314.16 square inches
- Area of 2 medium pizzas = 2 * π * (8^2) = 402.12 square inches
- Area of 0 small pizzas = 0

Total Area = 314.16 + 402.12 + 0 = 716.28 square inches.
The function would return `716.28`.

#### Details
- **Formula for the area of a circle**:
  Area = π * (radius^2)
  - The radius is calculated as half the diameter of the pizza.
  - Use the constant π provided in the program.
- The function uses constants to represent the diameters of large, medium, and small pizzas.
- It calculates the total area by summing the areas of all the pizzas ordered:
  Total Area = (Area of Large Pizzas) + (Area of Medium Pizzas) + (Area of Small Pizzas)
- Returns the total area as a float in square inches.

---

### Task 3: `calculate_cost`

#### Description
The `calculate_cost` function calculates the total cost of pizzas ordered, including a tip.

For example, if you have **9 guests**, the required pizzas might be **1 large pizza** and **2 small pizzas**. Assuming the tip is **15%**, the total cost would be:
- Cost of 1 large pizza = $14.68
- Cost of 2 small pizzas = 2 * $7.28 = $14.56
- Subtotal = $14.68 + $14.56 = $29.24
- Tip (15%) = $29.24 * 0.15 = $4.39
- Total Cost = $29.24 + $4.39 = $33.63

The function would return `33.63`.

#### Details
- Uses constants for the price of large, medium, and small pizzas.
- Multiplies the number of each pizza size by its corresponding price.
- Adds a tip based on the percentage input by the user.
- Returns the total cost as a float in dollars.


---

### Task 4: `main`

#### Description
The `main` function runs the pizza calculator program by integrating all other functions. It prompts the user for input, processes the data using the helper functions, and displays the final results.

#### Details
- Prompts the user to input:
  - The number of guests.
- Calls `calculate_pizzas` to determine the number of pizzas needed.
- Calls `serving_size` to compute the total pizza area and area per person.
- Prompts the user to input:
  - The tip percentage.
- Calls `calculate_cost` to compute the total cost, including the tip.
- Outputs the results to the user:
  - Number of pizzas.
  - Total area and area per person.
  - Total cost, including tip.

Refer to the **sample outputs** provided in the `sample_outputs` folder for guidance on formatting and expected results.

---

## Testing

You can test the functions for Task 1, Task 2, and Task 3 using **pytest**, a Python testing framework that simplifies writing and running test cases.

---

### Step 1: Install pytest
To install pytest, run the following command in your terminal:
```bash
$ pip install pytest
```

### Step 2: Testing Tasks

Each task can be tested using the provided test cases in the `test_pizza_calculator.py` file.

To test a specific task, use pytest and run the associated test function:

- Task 1: `pytest -k test_calculate_pizzas`
- Task 2: `pytest -k test_serving_size`
- Task 3: `pytest -k test_calculate_cost`

To run all the tests at once, use: `pytest`

### Step 3: Reviewing Test Results

pytest will display a summary of the results:

- A green dot (.) indicates a test passed.
- A red F indicates a test failed, with details about the error provided.

```bash
================= test session starts ==================
collected 3 items

test_pizza_calculator.py ...                        [100%]

================= 3 passed in 0.11s ====================
```

Debugging Failed Tests

If any tests fail:

- Review the function's implementation based on the error message.

- Make the necessary corrections in your code.

- Rerun pytest until all tests pass.

---

## Acknowledgment

This assignment was originally developed for CS 111 at BYU by its professors. I take no credit for its creation and have only adapted it for instructional purposes.
