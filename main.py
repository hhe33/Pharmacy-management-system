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

class Medication:
    def __init__(self, name, price, stock, manufacturer):
        self.name         = name
        self.price        = price
        self.stock        = stock
        self.manufacturer = manufacturer

    def __str__(self):
        return (
            f"Medication  : {self.name}\n"
            f"Price       : {self.price} FCFA\n"
            f"Stock       : {self.stock} units\n"
            f"Manufacturer: {self.manufacturer}"
        )

    def __eq__(self, other):
        return self.name.lower() == other.name.lower()

    @staticmethod
    def validate_price(price):
        return price > 0

    @classmethod
    def create_generic(cls, name, stock):
        return cls(name, 500.0, stock, "Generic Lab")





class PrescriptionMedication(Medication):
    def __init__(self, name, price, stock, manufacturer, doctor, treatment_duration):
        super().__init__(name, price, stock, manufacturer)
        self.doctor             = doctor
        self.treatment_duration = treatment_duration

    def display_prescription(self):
        print(f"Prescribing Doctor  : {self.doctor}")
        print(f"Treatment Duration  : {self.treatment_duration} days")


# --- Member 2 : DEHOUMON Christelle ---
# Part 1 - Input Validation Functions
# - get_text() : validates text input
# - get_float() : validates float input
# - get_int() : validates integer input
# - get_bool() : validates yes/no input and returns correct boolean

# YOUR CODE HERE


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
