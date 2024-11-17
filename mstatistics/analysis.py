from mstatistics.math_utils import MStats


class MAnal:
    def __init__(self, x):
        """
        Initializes the data analyzer.
        :param x: List of numerical data to analyze.
        """
        if not x or not all(isinstance(i, (int, float)) for i in x):
            raise ValueError("Input must be a non-empty list of numbers.")
        self.x = x
        self.stats = MStats(x)

    def is_symmetric(self) -> bool:
        """
        Checks if the data distribution is symmetric (zero skewness).
        :return: True if symmetric, False otherwise.
        """
        return self.stats.skewness() == 0

    def symmetry_type(self) -> int:
        """
        Determines the symmetry type based on skewness.
        :return: 0 if symmetric, 1 if positively skewed, -1 if negatively skewed.
        """
        skewness = self.stats.skewness()
        return 0 if skewness == 0 else (1 if skewness > 0 else -1)

    def describe_symmetry(self) -> str:
        """
        Provides a textual description of the symmetry type.
        :return: Description of symmetry.
        """
        symmetry_map = {
            0: "Is symmetric",
            1: "Is positively skewed",
            -1: "Is negatively skewed"
        }
        result = symmetry_map[self.symmetry_type()]
        print(result)
        return result

    def kurtosis_type(self) -> int:
        """
        Determines the kurtosis type based on excess kurtosis.
        :return: 0 if normal-tailed, 1 if fat-tailed, -1 if thin-tailed.
        """
        kurtosis = self.stats.kurtosis()
        return 0 if kurtosis == 3 else (1 if kurtosis > 3 else -1)

    def describe_kurtosis(self) -> str:
        """
        Provides a textual description of the kurtosis type.
        :return: Description of kurtosis.
        """
        kurtosis_map = {
            0: "Is normal-tailed",
            1: "Is fat-tailed",
            -1: "Is thin-tailed"
        }
        result = kurtosis_map[self.kurtosis_type()]
        print(result)
        return result
