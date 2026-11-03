# Restaurant Billing Program

# ADITYA KUMAR
# RU-26-02615

## Overview

A menu-based command-line program for taking restaurant orders and calculating a bill. Add one or more menu items with their quantities, then enter `bill` to display the totals.

## Objectives

- Accept menu items and positive whole-number quantities.
- Calculate a subtotal, an optional discount, GST, and the final amount.
- Reject unknown items and invalid quantities with clear messages.

## Features

- Menu: Dosa (80), Idli (40), Thali (150), and Tea (20).
- Repeated entries for the same item are combined.
- A 10% discount is applied when the subtotal is greater than 500.
- GST is 5% of the subtotal after discount.
- Amounts in the bill are displayed to two decimal places.
- The project logic is self-contained in `one.py`; `project.py` remains a compatibility launcher.

## Requirements

- Python 3.7 or later.
- No third-party packages are required.

## Run

Open a terminal in this folder and run:

```text
python one.py
```

You can also run the compatibility launcher:

```text
python project.py
```

Enter an item name and quantity when prompted. Enter `bill` when the order is complete. Item names are case-insensitive.

## Input and output

Example input:

```text
Dosa
2
Idli
1
bill
```

The program prints each ordered item's amount followed by the subtotal, discount, GST, and grand total. For this example, the subtotal is 200.00, the discount is 0.00, GST is 10.00, and the grand total is 210.00.

If an item is not on the menu, the program displays the available items and asks again. Quantities must be positive whole numbers; invalid entries are rejected and the program asks for another item.

## Test cases

Run all six automated test cases individually through the test runner:

```text
python -m unittest -v test_one.py
```

| Test case | Input scenario | Expected result |
|---|---|---|
| Regular bill | 2 Dosa, 3 Idli, 2 Tea | Subtotal 320.00; discount 0.00; GST 16.00; total 336.00 |
| Discount | 4 Thali | Subtotal 600.00; discount 60.00; GST 27.00; total 567.00 |
| Discount threshold | 2 Thali, 2 Dosa, 1 Idli | Subtotal 500.00; no discount; GST 25.00; total 525.00 |
| Invalid quantity | Dosa with `abc`, then `0`, then `1` | Both invalid entries are rejected; total 84.00 |
| Unknown item | `Pizza`, then 1 Tea | Pizza is rejected; total 21.00 |
| Empty cart | Enter `bill` immediately | Displays `Cart is empty!` and no grand total |

`test_one.py` runs each scenario as a separate end-to-end test. It uses only Python's standard library.

## Test evidence

The `screenshots` folder contains one input/output screenshot for each test case. `test-evidence.pdf` combines all six screenshots into a single PDF.

## Files

- `one.py` — complete standalone program for submission.
- `project.py` — compatibility launcher.
- `test_one.py` — automated end-to-end tests.
- `README.md` — project documentation.
- `screenshots/` — individual test-case screenshots.
- `test-evidence.pdf` — PDF containing all six screenshots.


## Project Mentor

Mentored by [Mr. Satyaprakash Sethy](https://github.com/SATYAPRAKASHSETHY).

**Role:** Python Mentor / Technical Guide  
**GitHub:** [@SATYAPRAKASHSETHY](https://github.com/SATYAPRAKASHSETHY)
