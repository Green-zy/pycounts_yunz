# pycounts_yunz

A package to calculate the number of the words in a text file.

## Installation

```bash
$ pip install pycounts_yunz
```

## Usage

`pycounts_yunz` can be used to calculate the number of the words in text file and visualize the result with the following code:

```python
from pycounts_yunz.pycounts_yunz import count_words
from pycounts_yunz.plotting import plot_words
import matplotlib.pyplot as plt

file_path = "test.txt"  # path to your file
counts = count_words(file_path)
fig = plot_words(counts, n=10)
plt.show()
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`pycounts_yunz` was created by Yun Zhou. It is licensed under the terms of the MIT license.

## Credits

`pycounts_yunz` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

The code in `pycounts_yunz` was adapted from [`How to package a Python`](https://py-pkgs.org/03-how-to-package-a-python).