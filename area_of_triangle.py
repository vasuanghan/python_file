def triangle(a, b):
    area = (1 / 2) * a * b
    return area

base = input("enter the base of triangle = ")
base = int(base)
height = input("enter the height of triangle = ")
height = int(height)

total = triangle(base, height)
print(total)
