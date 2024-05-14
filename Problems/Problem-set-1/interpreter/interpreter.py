expression = input("Expression: ")
x = int(x)
z = int(z)
x,y,z = expression.split(" ")

if y == '+':
    result = x + z
elif y == '-':
    result = x - z
elif y == '*':
    result = x * z
elif y == '/':
    result = x / z
    
print(f"{z:.1f}")
