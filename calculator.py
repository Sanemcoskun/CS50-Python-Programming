x = float(input("What's x? "))
y = float(input("What's y? "))

#z = round(x + y) #en yakın tam sayıya yuvarladı
#print(f"{z:,}")

z = x / y 
print(f"{z:.2f}")


def main():
    x = int(input("What's x? "))
    print("x square is",square(x))
    
       
def square(n):
    return n * n # pow(n, 2)

main()