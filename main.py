# ============================================
# PHARMACY MANAGEMENT SYSTEM
# PRG1406 - Advanced Programming (Python and C)
# Burkina Institute of Technology
# Group 22 - May 2026
# Instructor: Kweyakie Afi Blebo
# ============================================


# --- Member 1 : DOUAMBA Niddata Sidonie ---
# Part 2 - Parent Class and Child Class
# - class Medication : __init__, __str__, __eq__, @staticmethod, @classmethod
# - class PrescriptionMedication : super().__init__(), doctor, treatment_duration, display_prescription()

# YOUR CODE HERE


# --- Member 2 : DEHOUMON Christelle ---
# Part 1 - Input Validation Functions
# - get_text() : validates text input
# - get_float() : validates float input
# - get_int() : validates integer input
# - get_bool() : validates yes/no input and returns correct boolean
def get_text(message):
    while True:
        value = input(message).strip()
        if value != "":
            return value
        print("Error: This field cannot be empty. Please try again.")

def get_float(message):
    while True:
        try:
            value = float(input(message))
            if value > 0:
                return value
            print("Error: The value must be greater than 0.")
        except ValueError:
            print("Error: Invalid input. Please enter a number.")

def get_int(message):
    while True:
        try:
            value = int(input(message))
            if value >= 0:
                return value
            print("Error: The value must be positive.")
        except ValueError:
            print("Error: Invalid input. Please enter a whole number.")

def get_bool(message):
    while True:
        value = input(message).strip().lower()
        if value in ["yes", "no"]:
            return value == "yes"
        print("Error: Please type 'yes' or 'no' only.")



# --- Member 3 : ZABRE Yenderima Elvine ---
# Part 1 - Main Program
# - 10 input() calls with str, int, float, bool
# - 3 arithmetic expressions : total, discount, remaining stock
# - Create Medication or PrescriptionMedication object based on user input

# YOUR CODE HERE


# --- Member 4 : ZINGUE Anitha Estelle Cynthia ---
# Part 1 - Purchase Summary
# - f-strings for all output
# - Full summary screen at the end
# - Loyalty discount display
# - Generic medication availability using __eq__()

# YOUR CODE HERE


# --- Member 5 : KAMBOU Yeri Hermine ---
# README and Documentation
