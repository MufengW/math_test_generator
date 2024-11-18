from math import gcd

class Fraction:
    """
    Represents a fraction with numerator and denominator.
    Includes methods for reduction, real value, and LaTeX representation.
    """
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")

        self.numerator = numerator
        self.denominator = denominator
        self.reduced_numerator, self.reduced_denominator = self.reduce()
        self.value = self.numerator / self.denominator
        self.latex = self.to_latex()  # LaTeX representation of the original fraction
        self.reduced_latex = self.to_latex_reduced()  # LaTeX representation of the reduced fraction

    def reduce(self):
        """
        Reduces the fraction to its simplest form.
        Returns:
            (int, int): Reduced numerator and denominator.
        """
        common_divisor = gcd(self.numerator, self.denominator)
        return self.numerator // common_divisor, self.denominator // common_divisor

    def to_latex(self):
        """
        Returns the LaTeX representation of the fraction.
        """
        return f"\\frac{{{self.numerator}}}{{{self.denominator}}}"

    def to_latex_reduced(self):
        """
        Returns the LaTeX representation of the reduced fraction.
        """
        if self.reduced_numerator == 0:
            return "0"
        if self.reduced_denominator == 1:
            return f"{self.reduced_numerator}"

        return f"\\frac{{{self.reduced_numerator}}}{{{self.reduced_denominator}}}"

    def __str__(self):
        """
        String representation of the fraction.
        """
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        """
        Adds two fractions.
        Returns:
            Fraction: Result of addition.
        """
        if not isinstance(other, Fraction):
            raise ValueError("Can only add two Fraction objects.")
        lcm = (self.denominator * other.denominator) // gcd(self.denominator, other.denominator)
        new_numerator = (self.numerator * (lcm // self.denominator)) + \
                        (other.numerator * (lcm // other.denominator))
        return Fraction(new_numerator, lcm)

    def __sub__(self, other):
        """
        Subtracts two fractions.
        Returns:
            Fraction: Result of subtraction.
        """
        if not isinstance(other, Fraction):
            raise ValueError("Can only subtract two Fraction objects.")
        lcm = (self.denominator * other.denominator) // gcd(self.denominator, other.denominator)
        new_numerator = (self.numerator * (lcm // self.denominator)) - \
                        (other.numerator * (lcm // other.denominator))
        return Fraction(new_numerator, lcm)
    def __mul__(self, other):
        """
        Multiplies two fractions.
        Returns:
            Fraction: Result of multiplication.
        """
        if not isinstance(other, Fraction):
            raise ValueError("Can only multiply two Fraction objects.")
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        """
        Divides two fractions.
        Returns:
            Fraction: Result of division.
        """
        if not isinstance(other, Fraction):
            raise ValueError("Can only divide two Fraction objects.")
        # Division is equivalent to multiplying by the reciprocal of the other fraction
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        if new_denominator == 0:
            raise ZeroDivisionError("Division by zero in fraction operation.")
        return Fraction(new_numerator, new_denominator)
