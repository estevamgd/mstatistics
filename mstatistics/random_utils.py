import time


class MRand:
    def __init__(self, start: int, end: int, step: int):
        """
        Initializes the random number generator with a specified range and step size.

        :param start: The start of the range (inclusive).
        :param end: The end of the range (inclusive).
        :param step: The step size between possible numbers.
        """
        if start >= end:
            raise ValueError("Start must be less than end.")
        if step <= 0:
            raise ValueError("Step size must be greater than zero.")

        self.start = start
        self.end = end
        self.step = step

    @property
    def range(self):
        """
        Computes the range of numbers based on the start, end, and step.
        :return: A list of numbers in the range.
        """
        return list(range(self.start, self.end + 1, self.step))

    def _current_millis(self) -> int:
        """
        Retrieves the current time in milliseconds (modulo 1000).
        :return: The last three digits of the current time in milliseconds.
        """
        return int((time.time() * 1000) % 1000)

    def generate(self) -> int:
        """
        Generates a pseudo-random number within the specified range.
        :return: A random number from the range.
        """
        index = self._current_millis() % len(self.range)
        return self.range[index]
