#program that calculates the area of a triangle of base=2, and height=3
#formula A= 1/2 x bxh


def areaOfTriangle():
    base = int(input('Enter the base of the triangle: '))
    height = int(input('Enter the height of the triangle: '))
    
    area = (1/2) * base * height
    
    print(f"The area of the triangle of base {base} and height {height} is the {area:2f}")
    
areaOfTriangle()