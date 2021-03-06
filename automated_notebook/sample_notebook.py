# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + tags=["parameters"]
foo = "bar"
num = 17

# +
import tensorflow

a = 4

# +
from IPython.display import Image

b = a + 5

url = 'https://same-project.github.io/SAME-samples/automated_notebook/FaroeIslands.jpeg'

from IPython import display
display.Image(url)


# +
import plotly

def some_math(x, z) -> tuple:
    return (x + z, x / z)


# + tags=["same_step_1"]
# SAME-step-2

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
mu = 0
std = 1
x = np.linspace(start=-4, stop=4, num=100)
y = stats.norm.pdf(x, mu, std) 
plt.plot(x, y)
plt.show()

# +
# SAME-step-3

import requests
import pandas as pd
import io
import plotly.figure_factory as ff
import chart_studio.plotly as py

url = 'https://same-project.github.io/SAME-samples/automated_notebook/test.csv'
df = pd.read_csv(url)

df.describe()
# -



# SAME-step-3
g = some_math(8, 21)

# +
# SAME-step-4

print(f"j: {g[0]}")

# +
# SAME-step-4

print(f"k: {g[1]}")
# -






