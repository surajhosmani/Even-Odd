import sys
if len(sys.argv) < 2:
    print("Usage: python even_odd_count.py <num1> <num2> <num3> ...")
    sys.exit(1)

numbers = [int(n) for n in sys.argv[1:]]
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even Numbers Count:", even_count)
print("Odd Numbers Count:", odd_count)
