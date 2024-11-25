# Problem: First Unique Character in a String
# You are given a string containing only lowercase alphabetic characters. Write a function to:
 
# Find the first unique character in the string (a character that appears only once).
# Return the index of this unique character.
# If there is no unique character, return -1.

from typing import Dict, List


sample_data = [
    "alphabet",  # Expected Output: 1
    "aabbcc",  # Expected Output: -1
    "z",  # Expected Output: 0
    "abcabcde",  # Expected Output: 6
]

def main(string: str):
    chr_count_map = create_chr_count_map(string)
    
    for i, c in enumerate(string):
        if chr_count_map[c] == 1:
            print(i)
            return

    print(-1)

def create_chr_count_map(string: str) -> Dict:
    chr_count = {}
    for c in string:
        chr_count[c] = chr_count.get(c, 0) + 1
    return chr_count

if __name__ == "__main__":
    for data in sample_data:
        main(data)
