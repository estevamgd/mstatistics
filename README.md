# `mstats` - A Basic Statistical Analysis Class

`mstats` is a lightweight Python class designed to perform basic statistical analysis on a dataset. It offers methods for calculating common statistical measures such as mean, median, mode (yet to be implemented), variance, standard deviation, and more. The class also provides moment calculations, skewness, and kurtosis to give insights into the distribution properties of a dataset.

## Features

- **Central Tendency Measures**: 
  - `mean()`: Calculates the arithmetic mean.
  - `median()`: Computes the median (middle value of a sorted dataset).
  - `mode()`: *Not implemented yet.*
  
- **Dispersion Measures**:
  - `variance()`: Calculates the variance.
  - `std()`: Computes the standard deviation.
  - `var_coeff()`: Returns the coefficient of variation.

- **Distribution Shape Measures**:
  - `skewness()`: Computes the skewness, giving insight into the symmetry of the data.
  - `kurtosis()`: Calculates kurtosis, indicating the "tailedness" of the data.

- **Quantiles and Quartiles**:
  - `quartiles()`: Calculates and returns the first, second (median), and third quartiles.

## Example Usage

```python
from mstats import mstats

# Create an instance with a dataset
data = [1, 2, 3, 4, 5]
stats = mstats(data)

# Access quartiles
quartiles = stats.quartiles()
print("First Quartile:", quartiles[0])  # Output: 1.5

# Access kurtosis
print("Kurtosis:", stats.kurtosis())  # Output: 1.7

# Additional measures
print("Mean:", stats.mean())
print("Variance:", stats.variance())
print("Standard Deviation:", stats.std())
```

## Installation
Currently, `mstats` is not available as a package. Simply download main.ipynb and include it in your project directory. You can then import and use the class as shown above.
