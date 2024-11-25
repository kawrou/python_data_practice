# Max Consecutive Characters

# Write a funciton that:
# Finds the character that appears most consecutively in a string.
# Returns the character and it smaximum consecutive count.

# how:
# Need to keep track of the current most consecutive
# Need to keep track of the next most consecutive
# Need to see if the next chr is the same as the prev chr
# 
data = [
    "aabbccc", #"c", 3
    "helloooo", #"o", 4
    "python" #"p", 1
]


def main(string: str):
    current_chr = string[0] 
    current_count = 1
    max_count = 0
    max_chr = string[0]
    
    for i in range(1, len(string)):
        if string[i] == current_chr:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                max_chr = current_chr

            current_chr = string[i]
            current_count = 1
    if current_count > max_count:
        max_count = current_count
        max_chr = current_chr

    print(f"Character: {max_chr}, Count: {max_count}")

if __name__ == "__main__":
    for string in data:
        main(string)
