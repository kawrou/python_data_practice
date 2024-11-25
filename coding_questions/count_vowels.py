# Write a function that:

# Takes a string as input.
# Counts how many vowels (a, e, i, o, u) appear in the string (case-insensitive).
# Returns the total count.


data = [
    "alphabet", #3
    "PYTHON", #1
    "Beautiful day" #6
]


def main(string: str):
    vowels = "aeiou" 
    count = 0
    for chr in string.lower():
        if chr in vowels:
            count += 1

    print(count)

if __name__ == "__main__":
    for string in data:
        main(string)
