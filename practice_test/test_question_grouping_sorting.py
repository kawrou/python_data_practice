#Given a list of string
#Write a func to:
#group the strings by their lengths
#sort each group alphabetically
#return a dict where keys are string lengths, and values are the sorted lists of strings
# {3: ["cat", "dog"], 5: ["apple"], 6: ["banana"], 8: ["antelope"]}

# go through each item in list and check if len of string is in a hash map.
# add the item to the hash map

data = ["apple", "dog", "banana", "cat", "antelope"]

def main(data):
# origina:
#    sorted_list = sorted(data)
#    print(sorted_list) 
#
#    string_map = {}
#
#    for string in sorted_list:
#        if len(string) not in string_map:
#            string_map[len(string)] = [string]
#        else:
#            string_map[len(string)].append(string)
#    
#    print(string_map)

# alternative:
    string_map = {}

    for string in data:
        string_map.setdefault(len(string), []).append(string)

    for length in string_map:
        string_map[length].sort()

    # optionally
    sorted_map  = {k: string_map[k] for k in sorted(string_map)}

    print(sorted_map)

if __name__ == "__main__":
    main(data)
