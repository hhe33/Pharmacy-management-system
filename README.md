# Pharmacy Management System

PRG1406 — Advanced Programming (Python and C)
Burkina Institute of Technology — Group Assignment 1 — May 2026

---

## What the program does

This program simulates a Pharmacy Management System.
The user registers a medication, processes a purchase, and gets a full summary at the end.
The program handles both regular medications and prescription medications.

---

## Classes

### Medication (Parent class)

Represents a generic medication in the pharmacy.

| Attribute / Method | Type | Description |
|--------------------|------|-------------|
| name | str | Medication name |
| price | float | Unit price in FCFA |
| stock | int | Quantity in stock |
| manufacturer | str | Manufacturer name |
| __str__() | magic method | Controls what print(medication) displays |
| __eq__() | magic method | Compares two medications by name |
| validate_price(price) | @staticmethod | Returns True if price is valid |
| create_generic(name, stock) | @classmethod | Creates a generic version of a medication |

### PrescriptionMedication (Child class) — inherits from Medication

Represents a medication that requires a doctor prescription.
A PrescriptionMedication IS a Medication — the inheritance relationship makes sense.

| Attribute / Method | Type | Description |
|--------------------|------|-------------|
| doctor | str | Prescribing doctor name |
| treatment_duration | int | Duration of treatment in days |
| display_prescription() | method | Displays prescription details |

---

## How to run

Make sure Python 3.8 or higher is installed.

Open a terminal in the project folder and run:

```
python main.py
```

No external libraries needed. Standard Python only.

---

## Assignment checklist

| Requirement | Done |
|-------------|------|
| All 4 data types: str, int, float, bool | Yes |
| Correct boolean with .lower() == "yes" | Yes |
| At least 10 input() calls with type casting | Yes |
| At least 3 arithmetic expressions | Yes |
| Input validation with while + try/except | Yes |
| f-strings for all output | Yes |
| Summary screen at the end | Yes |
| Parent class + Child class | Yes |
| super().__init__() called in child | Yes |
| Child adds new attributes and methods | Yes |
| Magic method __str__ | Yes |
| Magic method __eq__ | Yes |
| Decorator @staticmethod | Yes |
| Decorator @classmethod | Yes |

---

## File structure

```
main.py       main program
README.md     this file
```

---

## Group 22

| Name | Role |
|------|------|
| DOUAMBA Niddata Sidonie | Parent class Medication |
| ZABRE Yenderima Elvine | Child class PrescriptionMedication |
| DEHOUMON Christelle | Input validation functions |
| KAMBOU Yeri Hermine | Main program, final assembly and GitHub |
| ZINGUE Anitha Estelle Cynthia | README |

---

 
## Group Members and Contributions
 
### Member 1 — DOUAMBA Niddata Sidonie
Part 2 - Parent Class and Child Class
- Created the parent class Medication
- Defined the four attributes: name (str), price (float), stock (int), manufacturer (str)
- Implemented the magic methods __str__() and __eq__()
- Implemented the decorators @staticmethod and @classmethod
- Created the child class PrescriptionMedication
- Inherited from Medication using class PrescriptionMedication(Medication)
- Called the parent constructor using super().__init__()
- Added new attributes: doctor (str) and treatment_duration (int)
- Added new method: display_prescription()
### Member 2 — DEHOUMON Christelle
Part 1 - Input Validation Functions
- Implemented all input validation functions using while loop and try/except
- get_text() : validates text input, re-prompts if empty
- get_float() : validates float input, re-prompts on bad input
- get_int() : validates integer input, re-prompts on bad input
- get_bool() : validates yes/no input and returns a correct boolean
### Member 3 — ZABRE Yenderima Elvine
Part 1 - Main Program
- Wrote the full main program
- Used all 4 data types: str, int, float, bool
- Made 10 input() calls with correct type casting
- Wrote 3 arithmetic expressions: total, discount, remaining stock
- Created Medication or PrescriptionMedication objects based on user input
- Called validate_price() and create_generic() to use all class features
### Member 4 — ZINGUE Anitha Estelle Cynthia
Part 1 - Purchase Summary
- Wrote the purchase summary section of the main program
- Used f-strings for all output
- Displayed a clear purchase summary screen at the end
- Handled loyalty discount display conditionally
- Displayed generic medication availability using __eq__()
### Member 5 — KAMBOU Yeri Hermine
README and Documentation
- Wrote the README.md file
- Documented what the program does
- Documented all classes and their attributes and methods
- Documented how to run the program
- Documented each group member's contribution
-For transparency, part of the work assigned to DEHOUMON Christelle was completed by the group because she was unavailable due to illness during the committe period.

---
Submitted by Group 22 - Burkina Institute of Technology#
