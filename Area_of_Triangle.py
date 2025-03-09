a = float(input("Enter the side of a : "))
b = float(input("Enter the side of b : "))
c = float(input("Enter the side of c : "))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print('Area of Triangle is %0.2f' %area)
