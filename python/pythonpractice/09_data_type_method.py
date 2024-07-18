# list method:-
l1 = [10, 20, 30, 40, 50, 60, 70]
list1 = ["abc", 34, True, 40, "male"]

l1.insert(
    1, "orange"
)  # insert method() inserts an item at the specified index
print(l1)

# append() method:- To add an item to the end of the list.
l1.append("banana")
print(l1)

# extend():-Add the elements of a list (or any iterable), to the end of the current list
l1.extend(list1)
print(l1)

# remove() method:- removes the specified item.
list1.remove(True)
print(list1)

# pop() method :-- removes the specified index.
list1.pop(1)
print(list1)

list1.pop()
print(list1)

# del keyword
del list1[1]
print(list1)

# clear() method :-empties the list.
list1.clear()
print(list1)

# sort() method :- sort list
li1 = [56, 78, 100, 2, 47, 10, 5, 5, 1, 1000]
li1.sort()
print(li1)

li1.sort(reverse=True)  # sort descending order
print(li1)

# Copy a List:-
mylist = li1.copy()
print(mylist)
