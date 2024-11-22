# Iteration Problem: Longest Even Subarray
# You are given a list of integers. Write a function to find the length of the longest contiguous subarray where all elements are even.

from typing import List


sample_data = [
    [1, 2, 4, 6, 3, 8, 10, 12, 1, 14],  # Expected Output: 3
    [2, 4, 6, 8, 10],  # Expected Output: 5
    [1, 3, 5, 7],  # Expected Output: 0
    [4],  # Expected Output: 1
]

def main(data: List):
    current_longest = 0
    max_length = 0

    for i in data:
        if i % 2 == 0:
            current_longest +=1
            max_length = max(max_length, current_longest)
        else:
            current_longest = 0

    print(max_length) 

if __name__ == "__main__":
    for data in sample_data:
        main(data)
