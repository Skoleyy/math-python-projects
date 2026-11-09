import math

"""Computing the GCD of two integers a,b as well as the coefficients of Bézout's identity via the (extended) Euclidean algorithm."""

def gcd(a, b):
    """This function recursively calculates the greatest common divisor of two integers a,b."""
    if b == 0:
        return abs(a)   # to avoid a negative gcd for a or b < 0
    return gcd(b, a % b)


def extended_gcd(a, b):
    """This function iteratively calculates the Bézout coefficients as well as the greatest common divisor of two integers a,b with the extended Euclidean algorithm. 
    Returns (g, s, t) with g = s·a + t·b."""
    r0, s0, t0 = a, 1, 0
    r1, s1, t1 = b, 0, 1

    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
    if r0 < 0:
        r0,s0,t0 = -r0,-s0,-t0 # similar to the normal gcd function, we have to account for negative results and thus negate the values for g = r0 < 0
    return r0, s0, t0

# Lastly, some comparisons to the inbuilt gcd method of the math module
print(f"For a = 48, b = 24, the GCD with math.gcd() is: {math.gcd(48, 24)} while my function provides the solution {gcd(48, 24)}")
print(f"For a = 1374, b = 498, the GCD with math.gcd() is: {math.gcd(1374, 498)} while my function provides the solution {gcd(1374, 498)}")
print(f"For a = -35988, b = 5892, the GCD with math.gcd() is: {math.gcd(-35988, 5892)} while my function provides the solution {gcd(-35988, 5892)}")
print(f"Lastly, for the case (a = -35988, b = 5892), the GCD and Bézout coefficients are {extended_gcd(-35988, 5892)} ")