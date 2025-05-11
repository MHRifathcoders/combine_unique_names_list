"""🧩 Problem Statement:

Write a function that takes two parameters - both are lists of names. Your task is to return a combined list containing all unique names from both lists (i.e., no duplicates in the final result).

list1 = ["Hasan", "Rafi", "Nayeem", "Rasel"]
list2 = ["Rafi", "Nayeem", "Sakib", "Apon"]

Output = ["Hasan", "Rafi", "Nayeem", "Rasel", "Sakib", "Apon"]"""

def combine_unique_names(list1, list2):
    combined_name_list = []
    
    # Add names from the first list
    for name in list1:
        # print(name)
        if name not in combined_name_list:
            combined_name_list.append(name)
    
    # Add names from the second list, avoiding duplicates
    for name in list2:
        # print(name)
        if name not in combined_name_list:
            combined_name_list.append(name)
    
    return combined_name_list

# Example usage
list1 = ["Hasan", "Rafi", "Nayeem", "Rasel"]
list2 = ["Rafi", "Nayeem", "Sakib", "Apon"]

my_output = combine_unique_names(list1, list2)
print(my_output)