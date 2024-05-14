greeting = input("Greeting: ").strip().lower()

if greeting.startswith("hello"): # hello ile başlayan
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")