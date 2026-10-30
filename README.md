
# Community Food Bank

## Student Information
- Name: [Your Full Name]
- Assignment: Python Final Exam — Community Food Bank

## Description
This is a menu-driven Python console application that manages
family registration, food pack stock and food distribution.

## Requirements
- Python 3
- No external packages required

## How to Run
1. Install Python 3 if it is not already installed.
2. Open a terminal in the project folder.
3. Run:

   python main.py

   On some systems, use:

   python3 main.py

## Classes
- Family: Stores a family's ID, name and number of members.
- FoodBank: Registers families, manages stock, distributes food
  and displays the report.

## Data Structures
- Dictionary: Stores family objects using family IDs as keys.
- Set: Prevents duplicate family IDs.
- List: Stores distribution history.
- Tuple: Stores each distribution record.

## Validation
The program rejects duplicate IDs, invalid member counts,
nonpositive quantities, unknown family IDs and insufficient stock.
It also handles nonnumeric integer input and invalid menu choices.

## Starting Stock
The available food pack stock starts at zero.
