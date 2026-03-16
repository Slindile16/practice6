# Python Data Structures and Recursion Practice

This project contains programming exercises that test knowledge of:

* Data Structures
* Data Manipulation
* Recursion
* String Formatting

Each question contains **4 functions** that must be implemented.

---

# Question 1 — Data Structure Utilities

count_items(data)

Return the number of elements in a list.

Example

Input
[1,2,3]

Output
3

unique_items(data)

Return a set of unique elements.

Example

Input
[1,1,2,3]

Output
{1,2,3}

get_keys(dictionary)

Return the keys of a dictionary as a list.

Example

Input
{"a":1,"b":2}

Output
["a","b"]

get_values(dictionary)

Return dictionary values as a list.

Example

Input
{"a":1,"b":2}

Output
[1,2]

---

# Question 2 — Data Manipulation

sort_numbers(numbers)

Return the list sorted in ascending order.

Example

Input
[3,1,2]

Output
[1,2,3]

filter_even(numbers)

Return only even numbers.

Example

Input
[1,2,3,4]

Output
[2,4]

remove_duplicates(numbers)

Return the list without duplicates.

Example

Input
[1,1,2,3]

Output
[1,2,3]

sum_numbers(numbers)

Return the sum of numbers.

Example

Input
[1,2,3]

Output
6

---

# Question 3 — Recursion and String Formatting

factorial(n)

Calculate the factorial of n using recursion.

Example

Input
4

Output
24

recursive_sum(n)

Return the sum of numbers from 1 to n using recursion.

Example

Input
4

Output
10

format_name(name, age)

Return a formatted string with name and age.

Example

Input
 

Output
"Name: Alice, Age: 20"

format_price(item, price)

Return a formatted string describing the item price.

Example

Input
("Apple",5)

Output
"Item: Apple costs $5"

---

# Running Tests

Run the tests with:

python3 -m unittest
