import math

def newton_method(v0, h):
    # Initial guess for α
    alpha = math.pi / 4  # 45 degrees

    # Tolerance for convergence
    epsilon = 1e-6

    # Maximum number of iterations
    max_iterations = 100

    # Perform Newton's method iterations
    for _ in range(max_iterations):
        f_alpha = math.sin(alpha) - (2 * 9.8 * h / (v0**2))**(1/2)

        if abs(f_alpha) < epsilon:
            # Convergence achieved
            break

        f_prime_alpha = math.cos(alpha)

        alpha = alpha - f_alpha / f_prime_alpha

    return alpha

# Given values
v0 = 10  # m/s
h = 1  # m

# Compute α using Newton's method
alpha = newton_method(v0, h)
print("the value of α is approximately: =", alpha)