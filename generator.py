import random
from fraction import Fraction

class MathTestGenerator:
    def __init__(self):
        self.problems = []  # List to store generated problems
        self.solutions = []  # List to store corresponding solutions

    def generate_addition_subtraction(self, limit, num_problems):
        for _ in range(num_problems):
            operation = random.choice(["+", "-"])
            a = random.randint(1, limit)
            b = random.randint(1, limit if operation == "+" else a)
            problem = f"{a} {operation} {b} = "
            solution = problem + f"{eval(f'{a} {operation} {b}')}"
            self.problems.append(problem)
            self.solutions.append(solution)

    def generate_addition_subtraction_100(self, num_problems=10):
        self.generate_addition_subtraction(100, num_problems)

    def generate_addition_subtraction_1000(self, num_problems=10):
        self.generate_addition_subtraction(1000, num_problems)

    def generate_multiplication(self, limit1, limit2, num_problems):
        for _ in range(num_problems):
            a = random.randint(2, limit1)
            b = random.randint(2, limit2)
            if random.random() > 0.5:  # 50% chance to swap
                a, b = b, a
            problem = f"${a} \\times {b}$ = "
            solution = problem + f"{a * b}"
            self.problems.append(problem)
            self.solutions.append(solution)

    def generate_multiplication_10(self, num_problems=10):
        self.generate_multiplication(10, 10, num_problems)

    def generate_multiplication_two_digit_by_one(self, num_problems=10):
        self.generate_multiplication(10, 100, num_problems)

    def generate_multiplication_two_digit_by_two(self, num_problems=10):
        self.generate_multiplication(100, 100, num_problems)

    def generate_gcd(self, num_problems=10):
        for _ in range(num_problems):
            again = True
            while again:
                # Generate two random integers
                a = random.randint(1, 100)
                b = random.randint(1, 100)
                gcd = self._gcd(a, b)

                # Adjust probabilities for specific GCD values
                if gcd == 1:
                    # Allow GCD = 1 with 10% probability
                    again = random.random() >= 0.05  # 95% chance to discard
                elif gcd == 2:
                    # Allow GCD = 2 with 20% probability
                    again = random.random() >= 0.2  # 90% chance to discard
                else:
                    again = False

            # Create the problem statement
            problem = f"GCD({a}, {b}) = "
            solution = problem + f"{gcd}"

            # Append to problems and solutions
            self.problems.append(problem)
            self.solutions.append(solution)

    def _gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def generate_lcm(self, num_problems=10):
        for _ in range(num_problems):
            # Generate two random integers
            a = random.randint(2, 20)
            b = random.randint(2, 20)

            # Create the problem statement
            problem = f"LCM({a}, {b}) = "
            solution = problem + f"{self._lcm(a, b)}"

            # Append to problems and solutions
            self.problems.append(problem)
            self.solutions.append(solution)

    def _lcm(self, a, b):
        return abs(a * b) // self._gcd(a, b)

    def generate_fraction_reduction(self, num_problems=10):
        preferred_lcms = [2, 3, 4, 5, 6, 7]

        for _ in range(num_problems):
            while True:
                # Randomly decide LCM category
                if random.random() < 0.7:  # 70% chance for preferred LCMs
                    lcm = random.choice(preferred_lcms)
                elif random.random() < 0.05:  # 5% chance for LCM = 1
                    lcm = 1
                else:  # 25% chance for other random LCMs
                    lcm = random.randint(8, 20)

                # Generate numerator and denominator
                numerator = lcm * random.randint(1, 10)
                denominator = lcm * random.randint(1, 10)

                # Ensure non-trivial fractions
                if numerator != denominator:
                    fraction = Fraction(numerator, denominator)
                    break

            # Create problem and solution
            problem = f"Reduce \\( {fraction.latex} \\) = "
            solution = f"\\( {fraction.latex} = {fraction.reduced_latex} \\)"

            self.problems.append(problem)
            self.solutions.append(solution)


    def generate_fraction_operations(self, num_problems=10):
        preferred_lcms = [2, 3, 4, 5, 6, 7]

        for _ in range(num_problems):
            while True:
                # Select denominators
                if random.random() < 0.7:  # 70% chance for preferred LCMs
                    lcm = random.choice(preferred_lcms)
                else:  # 30% chance for other LCMs
                    lcm = random.randint(8, 20)

                denom1 = lcm * random.randint(1, 10)
                denom2 = lcm * random.randint(1, 10)

                # Ensure denominators are below 100
                if denom1 < 100 and denom2 < 100:
                    break

            # Generate numerators and create fractions
            num1 = random.randint(1, denom1 - 1)
            num2 = random.randint(1, denom2 - 1)

            fraction1 = Fraction(num1, denom1)
            fraction2 = Fraction(num2, denom2)

            # Randomly choose operation
            operation = random.choice(["+", "-"])

            # Ensure subtraction results in non-negative fractions
            if operation == "-" and fraction1.value < fraction2.value:
                fraction1, fraction2 = fraction2, fraction1

            # Perform operation
            if operation == "+":
                result = fraction1 + fraction2
            else:
                result = fraction1 - fraction2

            # Create problem and solution
            problem = f"\\( {fraction1.latex} {operation} {fraction2.latex} = \\)"
            solution = f"\\( {fraction1.latex} {operation} {fraction2.latex} = {result.reduced_latex} \\)"

            self.problems.append(problem)
            self.solutions.append(solution)
