# take a list of ints
# returns the index of the first number that breaks the increasing sequence
# If no break, return -1


data = [
    [1,2,3,5,4,6], #output 3
    [1,2,3,4,5,6],  #output -1
    [2,4,6,8,7,10], # output 4
    [10,20,30,40] # output -1
]

def main(num_list):
    result = find_break(num_list)
    print(result)

def find_break(num_list):
# original
#    current_num = 0
#
#    for i, num in enumerate(num_list):
#        if num == current_num + 1:
#            current_num = num
#        else:
#            return i
#            
#    return -1

# correction

    for i in range(1, len(num_list)):
        if num_list[i] <= num_list[i-1]:
            return i
    return -1

if __name__ == "__main__":
    for num_list in data:
        main(num_list)
