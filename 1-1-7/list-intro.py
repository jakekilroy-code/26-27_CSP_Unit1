list1 = [3,4,5,6,7]
list2 = ["hello","world"]


print(list1[1])
print(list2[1])


list2[0] = "Goodbye"
print(list2[0])

# Using a loop with a list
for num in list1:
    # Printing elements - list is unchanged
    # print(num)
    print(list1.pop())
    print(list1)