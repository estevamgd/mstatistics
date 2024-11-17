class MStats:
    def __init__(self, x):
        """
        Initializes the statistics calculator.
        :param x: List of numerical data.
        """
        if not x or not all(isinstance(i, (int, float)) for i in x):
            raise ValueError("Input must be a non-empty list of numbers.")
        self.x = x

    def mean(self):
        """Calculates the mean (average) of the data."""
        return sum(self.x) / len(self.x)

    def median(self):
        """Calculates the median of the data."""
        sorted_x = sorted(self.x)  # Avoid modifying the original list
        n = len(sorted_x)
        mid = n // 2
        return (sorted_x[mid] + sorted_x[mid - 1]) / 2 if n % 2 == 0 else sorted_x[mid]

    def mode(self):
        """Calculates the mode(s) of the data. Returns a list of modes."""
        from collections import Counter
        counts = Counter(self.x)
        max_count = max(counts.values())
        modes = [key for key, count in counts.items() if count == max_count]
        return modes if len(modes) > 1 else modes[0]

    def quartiles(self):
        """Calculates the quartiles (Q1, Q2, Q3) of the data."""
        sorted_x = sorted(self.x)
        n = len(sorted_x)

        def get_quartile(position):
            lower = sorted_x[int(position) - 1]
            upper = sorted_x[int(position)]
            return lower + (upper - lower) * (position - int(position))

        q1 = get_quartile((n + 1) / 4)
        q2 = self.median()
        q3 = get_quartile(3 * (n + 1) / 4)
        return [q1, q2, q3]

    def amplitude(self):
        """Calculates the range (amplitude) of the data."""
        return max(self.x) - min(self.x)

    def variance(self):
        """Calculates the variance of the data."""
        mean = self.mean()
        return sum((xi - mean) ** 2 for xi in self.x) / len(self.x)

    def std(self):
        """Calculates the standard deviation of the data."""
        return self.variance() ** 0.5

    def var_coeff(self):
        """Calculates the coefficient of variation (CV) of the data."""
        return self.std() / self.mean()

    def m2(self):
        """Calculates the second moment about the mean."""
        mean = self.mean()
        return sum((xi - mean) ** 2 for xi in self.x) / len(self.x)

    def m3(self):
        """Calculates the third moment about the mean."""
        mean = self.mean()
        return sum((xi - mean) ** 3 for xi in self.x) / len(self.x)

    def m4(self):
        """Calculates the fourth moment about the mean."""
        mean = self.mean()
        return sum((xi - mean) ** 4 for xi in self.x) / len(self.x)

    def skewness(self):
        """Calculates the skewness of the data."""
        return self.m3() / self.m2() ** 1.5

    def kurtosis(self):
        """Calculates the kurtosis of the data."""
        return self.m4() / self.m2() ** 2


class MCombanal:
    def __init__(self, s):
        """
        Initializes the combinatorics object.
        :param s: The input sequence or list.
        """
        self.s = s
        self.n = len(s)

    def factorial(self, n):
        """
        Calculates the factorial of a number.
        :param n: The number for which to calculate the factorial.
        :return: Factorial of n.
        """
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        return 1 if n == 0 else n * self.factorial(n - 1)

    def permutation(self):
        """
        Calculates the number of permutations of the sequence.
        :return: Number of permutations.
        """
        return self.factorial(self.n)

    def arrangement(self, x):
        """
        Calculates the number of arrangements (permutations of x elements).
        :param x: The number of elements to arrange.
        :return: Number of arrangements.
        """
        if x > self.n:
            raise ValueError("Cannot arrange more elements than available.")
        return self.permutation() / self.factorial(self.n - x)

    def combination(self, x):
        """
        Calculates the number of combinations (selections of x elements).
        :param x: The number of elements to select.
        :return: Number of combinations.
        """
        if x > self.n:
            raise ValueError("Cannot select more elements than available.")
        return self.arrangement(x) / self.factorial(x)
