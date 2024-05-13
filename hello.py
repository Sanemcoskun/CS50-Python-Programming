# Ask user for their name
# name = input("What's your name? ").strip().title()

# Split user's name into first name and last name
# first, last = name.split(" ")

# Say hello to user
# print(f"hello, {first}")

def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="World"): #to copy name varsayılan değer olur(to)
    print("hello,",to)

main()