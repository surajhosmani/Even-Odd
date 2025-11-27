import sys

if len(sys.argv) < 2:
    print("Usage: python even_odd_count.py <numbers>")
    sys.exit()

# Convert all command-line arguments to integers
numbers = [int(x) for x in sys.argv[1:]]

even_count = 0
odd_count = 0

for n in numbers:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even Count:", even_count)
print("Odd Count:", odd_count)
