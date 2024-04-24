import math

a_vec = [1, 2, 3]
b_vec = [4, 5, 6]
scalar = 2


def vector_addition(a, b):  # a + b
    if len(a) != len(b):
        return None
    res = [0] * len(a)
    for i in range(len(a)):
        res[i] = a[i] + b[i]
    return res


def vector_scalar_multiplication(s, a):  # s * a
    res = [0] * len(a)
    for i in range(len(a)):
        res[i] = s * a[i]
    return res


def vector_norm(a):
    sum = 0
    for val in a:
        sum += pow(val, 2)
    return math.sqrt(sum)


print(vector_addition(a_vec, b_vec))  # prints: [5, 7, 9]
print(vector_scalar_multiplication(scalar, a_vec))  # prints: [2, 4, 6]
print(vector_norm(a_vec))  # prints: 3.741...
print(vector_norm(b_vec))
