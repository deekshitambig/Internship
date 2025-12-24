my_list=[10,20,30,40,50]
my_list[1]=200
print("after changing second element",my_list)
my_list.append(600)
print("list after appending",my_list)
my_list.insert(2,300)
print("list after inserting 300 at index 2",my_list)
my_list.remove(600)
print("list after removing 600",my_list)
my_list.pop(0)
print("list after removing element",my_list