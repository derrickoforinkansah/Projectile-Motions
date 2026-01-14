# Projectile Motions
These files tell you everything about the motion of a projectile in Numerical Analysis
## How the Code Works
- Importing Math Functions

```python
import math
```
This allows the use of sin, cos, and pi.

- Defining the Newton Method Function

```python
def newton_method(v0, h):
```

This function takes:
v0: initial velocity
h: height
And returns the angle α.

- Initial Guess

```python
alpha = math.pi / 4
```
Starts with 45° as the first guess.

- Convergence Settings

```python
epsilon = 1e-6
max_iterations = 100
```
epsilon: how accurate the result should be

max_iterations: safety limit

- Newton’s Iteration

```python
f_alpha = math.sin(alpha) - (2 * 9.8 * h / (v0**2))**(1/2)
f_prime_alpha = math.cos(alpha)
alpha = alpha - f_alpha / f_prime_alpha
```
This updates α using:

𝛼_𝑛𝑒𝑤 =𝛼 − 𝑓(𝛼)/𝑓′(𝛼)

​
Until the error is very small.

- Using the Function

```python
v0 = 10
h = 1
alpha = newton_method(v0, h)
print("the value of α is approximately: =", alpha)
```

It calculates α for:

Velocity = 10 m/s

Height = 1 m


## note 

*all the figures used are just samples to prove the code works*

### In the second part/section of the code (Visuals)
- Import Libraries
```python
import matplotlib.pyplot as plt
import numpy as np
```
numpy → for numerical arrays

matplotlib → for plotting graphs

- Set Desired Initial Velocity
```python
v0 = 10  # m/s
```
Same velocity as before.

- Create Height Values
```python
h_values = np.arange(0, 3.1, 0.1)
```
This creates: 0.0, 0.1, 0.2, ..., 3.0

So you test many heights instead of just one.

- Compute Angles
```python
alpha_values = [newton_method(v0, h) for h in h_values]
```
For each height:

Newton’s Method finds α

Results are stored in a list

- Plot the Graph
```python
plt.plot(h_values, alpha_values)
plt.xlabel("Height (h)")
plt.ylabel("Angle (α)")
plt.title("Angle α vs. Height h")
plt.grid(True)
plt.show()
```
This produces a clean graph showing how the angle changes with height

## note again 

*all the figures used are just samples to prove the code works*

 # the first file (PM) contains the first section of the code and the second section of the code is (PM02)

*comnbning them in Jupyter Lab is also shown the 3rd File*
