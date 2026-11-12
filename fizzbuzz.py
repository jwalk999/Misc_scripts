i = 0

while i <= 100:
    i += 1
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
# Wow so easy


# We can do better.
raw = input("Enter divisors separated by commas (e.g. 3,5): ")
divisors = [int(n) for n in raw.split(",") if n.strip() != "0"]

rules = {}
for d in divisors:
    rules[d] = input(f"Word for {d}: ")

for i in range(1, 101):
    output = ""
    for d, word in rules.items():
        if i % d == 0:
            output += word
    print(output or i)