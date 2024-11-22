# Given a list of strings, write a function that returns the most frequently occurring character across all strings of the same length.
# 
# Return a dictionary where:
# 
# The keys are the lengths of the strings.
# The values are dictionaries containing:
# The most frequently occurring character for that length.
# The number of times it appears.

# Input: 
# ["dog", "cat", "banana", "apple", "ant", "bat"]

# Output:
# {
#     3: {"character": "a", "count": 3},
#     5: {"character": "p", "count": 2},
#     6: {"character": "a", "count": 3}
# }

# If two characters have the same length, return the lexiographically smaller one.

from typing import Dict, List
import json

sample_data = ["dog", "cat", "banana", "apple", "ant", "bat"]
 

def main(data):
    grouped_strings = group_strings(data)
    summary = summarise(grouped_strings)
    print(json.dumps(summary, indent=4))
    return summary

def summarise(grouped_string: Dict) -> Dict:
    summary_dict = {}
    
    for string_length in grouped_string:
        summary_dict[string_length] = find_most_occuring_chr(grouped_string[string_length])

    return summary_dict

def find_most_occuring_chr(string_list: List) -> Dict:
    chr_map = {}

    for s in string_list:
        for c in s:
            chr_map[c] = chr_map.get(c, 0) + 1

    chr = max(chr_map, key=lambda count : (chr_map[count], -ord(count)))
    
    return {"character": chr, "count": chr_map[chr] }

# Groups strings in a list by the length of the string
def group_strings(strings: List) -> Dict:
    length_map = {}

    for s in strings:
        length_map.setdefault(len(s), []).append(s)

    return dict(sorted(length_map.items()))

if __name__ == "__main__":
    main(sample_data)
