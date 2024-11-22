# Write a function that:
# Accepts a list of strings as input. The list will always have at least 3 strings.
# Returns the third longest string in the list.
# If multiple strings have the same length:
# Preserve their original order when determining which string to select.

# Input:
# ["dog", "cat", "elephant", "bat", "antelope"]

# Output: 
# "dog"

# Explanation:
# [3, 3, 3, 8]

# Distinct lengths:
# [8,7,3]

# Input:
# ["apple", "banana", "apricot", "ant", "carrot"]

# Output:
# "apple"

# Distinct lengths:
# [7,6,5]

# Input:
# ["ant", "bat", "cat", "dog"]

# Output:
# "ant"

# Distinct lengths:
# [3]

from typing import Dict, List

sample_data = [
    ["dog", "cat", "elephant", "bat", "antelope"],  # Not enough distinct lengths
    ["apple", "banana", "apricot", "ant", "carrot"],  # apple
    ["ant", "bat", "cat", "dog"],  # Not enough distinct lengths
    ["apple", "bat", "elephant", "dog", "fish"],  # bat - [5,3,8,4] - fish
    ["dog", "antelope", "cat", "elephant", "bat", "apple"],  # dog
    ["short", "tiny", "minuscule", "medium", "small", "large"],  # medium - [5,4,9,6] - short
]

def main(sample_data):
    grouped_data = group_data(sample_data)
    if len(grouped_data) < 3:
        print("Not enough distinct lengths.")
        return "Not enough distinct lengths."

    third_longest_string = get_third_longest(grouped_data)
    
    print(third_longest_string)
    return third_longest_string

def group_data(input_strings: List) -> Dict:
    grouped_data = {}

    for string in input_strings:
        key = len(string)
        if key not in grouped_data:
            grouped_data[key] = []
        grouped_data[key].append(string)

    return grouped_data

def get_third_longest(data: Dict):
    sorted_keys = sorted(data.keys(), reverse=True)
    
    third_longest_key = sorted_keys[2]

    return data[third_longest_key][0]
    
if __name__ == "__main__":
    for data in sample_data:
        main(data)


