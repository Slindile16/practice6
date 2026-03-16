def count_items(data):
    total = 0
    for i in data:
        total += 1
    return total
# print(count_items(["sli","ntsako","bongane","lebo"]))



def unique_items(data):
    item = set()
    for i in data:
        item.add(i)
    return item
# print(unique_items(["sli","sli","ntsako","lebo","nana","lebo"]))


def get_keys(dictionary):
    list = []
    for keys,value in dictionary.items():
        list.append(keys)
    return list
# print(get_keys({"a":1,"b":2}))
        

def get_values(dictionary):
    list = []
    for keys,values in dictionary.items():
        list.append(values)
    return list
# print(get_values({"a":1,"b":2}))

def sort_numbers(numbers):
    numbers.sort()
    return numbers
# print(sort_numbers([22,6,88,49]))


def filter_even(numbers):
    even = []
    for i in numbers:
        if i % 2 == 0:
            even.append(i)
    return even
# print(filter_even([44,5,16,25]))



def remove_duplicates(numbers):
    dup = []
    for i in numbers:
        if i not in dup:
            dup.append(i)
    return dup
# print(remove_duplicates(["sli","sli","ntsako","lebo","nana","lebo"]))


def sum_numbers(numbers):
    total = 0
    for i in numbers:
        total += i
    return total
# print(sum_numbers([1,2,3]))

def factorial(n):
    if n <= 0:
        return 1
    return n * factorial(n - 1)
# print(factorial(4))


def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)
# print(recursive_sum(4))

def format_name(name, age):
    return (f"Name: {name}, Age: {age}")
# print(format_name("Alice",20))


def format_price(item, price):
    return (f"Item: {item} costs ${price}")
# print(format_price("Apple",5))