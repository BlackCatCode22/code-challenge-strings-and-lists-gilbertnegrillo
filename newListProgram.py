# Code Challenge - Strings and Lists
# listExample01.py 9/1/23
#
# Python file name: newListProgram.py
#
# Date: August 5 2023
#
# Programmer's name: Gilbert Negrillo

# ********************************************************************************************
# Part 1 Strings
# Instructions: Using str_one and str_two, complete the string operations below. Create comments for all code
#     operations.

str_one = " The quick brown fox jumps over the lazy dog. "
str_two = "The slow   black dog bows before the regal fox."

# TODO: Use the string functions strip() and replace() to remove all spaces from str_one and store the result
#    in a variable named str_no_spaces. Output str_no_spaces.
# print("\n str_no_spaces is... " + str_no_spaces)
str_no_spaces = str_one.strip() + str_one.replace(" ", "") # Used strip() and replace() functions to remove all spaces from str_one, stored the result in a variable named str_no_spaces.
print("\n str_no_spaces is... " + str_no_spaces) # Output str_no_spaces.

# TODO: Concatenate str_one and str_two and store the result in a variable named str_cat. Output str_cat.
# print("\n str_cat is... " + str_cat)
str_cat = str_one + str_two # Concatenated str_one and str_two using + and stored the result in a variabled named str_cat.
print("\n str_cat is... " + str_cat) # Output str_cat

# TODO: Use the string function len() to find the length of str_cat and store the result
#    in a variable named str_len. Output str_len.
# print("\n The length of " + str_cat + " is: " + str_len)
str_len = str(int(len(str_cat))) # Used string function len() to find the length of str_cat and stored the result in a variable named str_len.
print("\n The length of " + str_cat + " is: " + str_len) # Output str_len.

# TODO: Use the string function lower() to change str_cat to all lower case and store the result
#    in a variable named str_cat_lower. Output str_cat_lower.
# print("\n str_cat_lower in lower case is: " + str_cat_lower)
str_cat_lower = str_cat.lower() # Used string function lower() to change str_cat to lower case and stored the result in a variable named str_cat_lower.
print("\n str_cat_lower in lower case is: " + str_cat_lower) # Output str_cat_lower.

# TODO: Use the string function upper() to change str_cat to all upper case and store the result
#    in a variable named str_cat_upper. Output str_cat_upper.
# print("\n str_cat_upper in upper case is: " + str_cat_upper)
str_cat_upper = str_cat.upper() # Used string function upper() to change str_cat to all upper case and stored the result in a variable named str_cat_upp.
print("\n str_cat_upper in upper case is: " + str_cat_upper) # Output str_cat_upper.

# TODO: Use the following three variables in an "f-string" to produce the following string. Store the string
#    in a variable named str_formatted. Output str_formatted.
# "The *adjective* brown fox *verb* *preposition* the lazy dog."
# print("\n str_formatted is: " + str_formatted)
adjective = "smart"
verb = "ran"
preposition = "through"
str_formatted = f"The {adjective} brown fox {verb} {preposition} the lazy dog." # Used f-string to produce adjective, verb, and preposition variables and stored the string in a variable named str_formatted..
print("\n str_formatted is: " + str_formatted) # Output str_formatted.

# TODO: Use the string function find() to locate the starting index of "black dog". Store the index
#    in a variable named start_index. Output start_index.
# print("\n start_index is: " + start_index)
start_index = str(int(str_two.find("black dog"))) # Used find() function to loacte the starting index of "black dog", stored the index in a variabled named start_index.
print("\n start index is: " + start_index) # Output start_index.

# TODO: Use String Slicing to extract the string "black dog" from str_two. Store the extracted sting
#    in a variable named substring. Output substring.
# print("\n substring is: " + substring)
substring = str_two[11:21] # Used string slicing to extract the string "black dog" from str two by starting with the element number 11 and stopping at element number 21. Stored the extracted string in variable named substring.
print("\n substring is: " + substring) # Output substring.

# *******************************************************************************************************
# Part 2 Lists
# Instructions: Use the split() function to create a list from the following string. Store the list in a variable named
#     list_of_names. Output list_of_names.

str_for_list = "Natalia, Alice, Bob, Charlie, Sergei, David, Eve, Frank, Grace, Dmitri, Hannah, \
Isaac, Jack, Ivan, Olga"
# print("\n list_of_names is: " + str(list_of_names))
list_of_names = str_for_list.split() # Used split function to create a list from the str_for_list. Stored the list in a variabled named list_of_names.
print("\n list_of_names is: " + str(list_of_names)) # Output list_of_names.

# TODO: Use the sorted() function to sort the list alphabetically and store the result in a variable named list_sorted.
#    Output list_sorted. Output list_of_names to observe that the original list was not modified.
# print("\n list_sorted is: " + str(list_sorted))
# print("\n list_of_names is: " + str(list_of_names))
list_sorted = sorted(list_of_names) # Used sorted() function to sort the list alphabetically and sotred ther esult in a variable named list_sorted.
print("\n list_sorted is: " + str(list_sorted)) # Output list_sorted
print("\n list_of_names is: " + str(list_of_names)) # Output list_of_names to see that the original list was not modified.

# TODO: Use string slicing to reverse list_sorted without modifying the original list and store the result
#    in a variable named list_reversed. Output list_reversed. HINT: list_sorted[::-1]
# print("\n list_reversed is: " + str(list_reversed))
list_reversed = list_sorted[::-1] # Used string slicing to reverse list_sorted by stepping by -1 without modifying the original list and stored the result in a variable named list_reversed.
print("\n list_reversed is: " + str(list_reversed)) # Output list_reversed.

# TODO: Use a for/in loop to output the reversed name list one name on a line. Use 'for name in list_reversed
#     for the list header
# for name in list_reversed:
#     print(name)
for name in list_reversed: # Used for/in loop to output the reversed name list one name on a line.
    print(name)

# TODO: Use list slicing to extract the first three elements of list_sorted. HINT: list_sorted[0:3]
#    Store the result in a variable named first_three. Output first_three and examine the data type of first_three.
#     print(first_three)
#     print(str(type(first_three)))
first_three = list_sorted[0:3] # Used list slicing to extract the first three elements of list_sorted, start at element number 0 and end at element number 3. Stored the result in a variable named first_three.
print(first_three) # Output first_three.
print(str(type(first_three))) # Examine the data type of first_three and the data type of first_three is list.

# TODO: Modify list_sorted. Use append() and insert(). Append "Yevgeny" and "Svetlana" to list_sorted. insert() "Boris"
#    at element number 5. Output list_sorted. Note the order of the list.
# list_sorted.append("Svetlana")
# list_sorted.insert(5,"Boris")
# print(list_sorted)
list_sorted.append("Yevgeny") # Used append function to add Yevgeny to the sorted list.
list_sorted.append("Svetlana") # Used append function to add Svetlana to the sorted list.
list_sorted.insert(5, "Boris") # Used insert function to add Boris at element number 5 to the sorted list.
print(list_sorted) # Output list_sorted.

# TODO: Get list_sorted back to sorted order. To do this you will sort the list "in place" meaning your sort will change
#    the list. Use list_sorted.sort() and output list_sorted.
list_sorted.sort() # Used sort function to get list_sorted back to sorted order.
print(list_sorted) # Output list_sorted.

# TODO: Modify list_sorted. Use extend to add first_three to the end of the list. Hint: list_sorted.extend(first_three)
#    Output the list.
list_sorted.extend(first_three) # Used extend function to add first_three to the end of the lost.
print(list_sorted) # Output list_sorted

# TODO: Get list_sorted back to sorted order. To do this you will sort the list "in place" meaning your sort will change
#    the list. Use list_sorted.sort() and output list_sorted.
list_sorted.sort() # Used sort function to get list_sorted back to sorted order.
print(list_sorted) # Output list_sorted.

# TODO: Modify list_sorted. Use remove to remove the first occurance of "Alice" Hint: list_sorted.remove("Alice")
#    Output the list.

list_sorted.remove("Alice,") # Used remove function to remove the first occurrence of "Alice"
print(list_sorted) # Output list_sorted.


# last one!
# TODO: Remove duplicates in list_sorted by copying the list into a set (which will delete duplicates) and then convert
#     back into a list. here's the code for that:
#     my_set = set(list_sorted)
#     list_sorted = list(my_set)
#

my_set = set(list_sorted) # Used set to remove duplicates in list_sorted, stored the result in a variable named my_set.
list_sorted = list(my_set) # Used list to convert the set back into a list.
print(list_sorted) # Output list_sorted.
list_sorted.sort() # Used sort function to get list_sorted back to sorted order.
print(list_sorted) # Output list_sorted.

#     Examine list_sorted. it probably isn't sorted, so... sort it ("in place") with list_sorted.sort()