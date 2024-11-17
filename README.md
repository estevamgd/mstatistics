# mStatistics

`mStatistics` is a Python library for statistical analysis, combinatorics, and random number generation. It provides tools to streamline data analysis and computation.

## Features

- **Statistical Analysis**:
  - Calculate mean, variance, skewness, kurtosis, and more.
  - Evaluate data symmetry and kurtosis types.
- **Frequency Analysis**:
  - Track events and calculate relative frequencies.
- **Combinatorics**:
  - Compute permutations, combinations, and arrangements.
- **Random Number Generation**:
  - Generate random numbers within a custom range.

## Installation

Clone the repository and install the package:

```bash
git clone https://github.com/estevamgd/mstatistics.git
cd mstatistics
pip install .
```

## Usage

### Statistical Analysis

```python
from mstatistics import MStats

data = [1, 2, 3, 4, 5]
stats = MStats(data)

print("Mean:", stats.mean())
print("Variance:", stats.variance())
```

### Frequency Analysis
```python
from mstatistics import MFreqrel

tracker = MFreqrel(sdict={}, event="event1", n=100)
tracker.update_event_count("event1", 10)
print("Relative Frequency of event1:", tracker.relative_frequency("event1"))
```

### Combinatorics
```python
from mstatistics import MCombanal

sequence = [1, 2, 3]
comb = MCombanal(sequence)

print("Permutations:", comb.permutation())
print("Combinations (2):", comb.combination(2))

```

### Random Number Generation

```python
from mstatistics import MRand

random_gen = MRand(start=1, end=10, step=1)
print("Random Number:", random_gen.generate())
```

## Project Structure
```bash
mstatistics/
├── analysis.py         # Statistical analysis tools
├── freq_utils.py       # Frequency analysis tools
├── math_utils.py       # Mathematical utilities
├── random_utils.py     # Random number generation
└── __init__.py         # Module initialization
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Thank you for using `mStatistics`! 🚀
