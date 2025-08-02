import scipy.integrate as spi


def integrand(x):
    return x**2

# spi.quad performs numerical integration.
result, error = spi.quad(integrand, 0, 1)
print(result)
