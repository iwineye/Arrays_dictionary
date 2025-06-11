


Some **easy to medium-level Python interview questions** that focus on **lists** and **dictionaries**. These questions will test both your understanding of basic operations and your ability to solve problems effectively using these data structures.

### **List-Related Python Interview Questions**

#### **1. Reverse a List**

**Question**: Write a function to reverse a list in Python.

```python
def reverse_list(lst):
    # Your code here
    return lst[::-1]  # Option 1: Using slicing

# OR
def reverse_list(lst):
    # Option 2: Using in-place reverse
    lst.reverse()
    return lst
```

#### **2. Remove Duplicates from a List**

**Question**: Given a list of numbers, write a Python function to remove duplicate numbers and return the result as a list.

```python
def remove_duplicates(lst):
    return list(set(lst))  # Convert to set to remove duplicates, then back to list
```

#### **3. Find the Maximum Product of Two Numbers in a List**

**Question**: Write a Python function to find the maximum product of two numbers in a list of integers.

```python
def max_product(lst):
    lst.sort()
    return lst[-1] * lst[-2]  # Return product of two largest numbers
```

#### **4. Check if a List is a Sublist of Another**

**Question**: Write a function to check if one list is a sublist of another list.

```python
def is_sublist(list1, list2):
    return any(list1 == list2[i:i+len(list1)] for i in range(len(list2)-len(list1)+1))
```

#### **5. Rotate a List by K Positions**

**Question**: Write a function that rotates a list by `k` positions to the right.

```python
def rotate_list(lst, k):
    k = k % len(lst)  # Handle cases where k > len(lst)
    return lst[-k:] + lst[:-k]
```

#### **6. Find the Intersection of Two Lists**

**Question**: Write a function to find the intersection of two lists (i.e., elements common to both lists).

```python
def intersection(list1, list2):
    return list(set(list1) & set(list2))  # Using set intersection
```

#### **7. Merge Two Sorted Lists**

**Question**: Write a Python function to merge two sorted lists into one sorted list.

```python
def merge_sorted_lists(list1, list2):
    return sorted(list1 + list2)
```

---

### **Dictionary-Related Python Interview Questions**

#### **8. Count Frequency of Elements in a List**

**Question**: Write a function to count the frequency of each element in a list.

```python
from collections import Counter

def count_frequency(lst):
    return dict(Counter(lst))  # Using collections.Counter to count frequencies
```

#### **9. Find the Most Frequent Element in a List**

**Question**: Write a Python function to find the most frequent element in a list.

```python
from collections import Counter

def most_frequent(lst):
    count = Counter(lst)
    return count.most_common(1)[0][0]  # Return the element with the highest frequency
```

#### **10. Merge Two Dictionaries**

**Question**: Write a Python function to merge two dictionaries. If a key appears in both dictionaries, the value from the second dictionary should be used.

```python
def merge_dicts(dict1, dict2):
    dict1.update(dict2)  # Update dict1 with dict2 values
    return dict1
```

#### **11. Group Anagrams from a List of Strings**

**Question**: Given a list of strings, group the anagrams together. Anagrams are strings that contain the same characters, but in different orders.

```python
from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)
    for word in strs:
        anagrams[tuple(sorted(word))].append(word)
    return list(anagrams.values())
```

#### **12. Find the First Non-Repeating Character in a String**

**Question**: Write a function to find the first non-repeating character in a string.

```python
def first_non_repeating(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in s:
        if count[char] == 1:
            return char
    return None  # Return None if no unique character found
```

#### **13. Check if Two Dictionaries are Equal**

**Question**: Write a Python function to check if two dictionaries are equal (i.e., have the same keys and values).

```python
def are_dicts_equal(dict1, dict2):
    return dict1 == dict2
```

#### **14. Find the Missing Element in a Dictionary**

**Question**: Given a dictionary of integers and a key, write a function to return the missing element (i.e., an element from a given range not present in the dictionary).

```python
def find_missing_element(d, n):
    for i in range(1, n+1):
        if i not in d:
            return i
```

#### **15. Count the Number of Keys with Specific Value**

**Question**: Write a function that counts how many keys in a dictionary have a specific value.

```python
def count_keys_with_value(d, value):
    return sum(1 for v in d.values() if v == value)
```

---

### **Combination List and Dictionary Questions**

#### **16. Flatten a Nested List (List of Lists)**

**Question**: Write a function to flatten a nested list of lists into a single list. You can assume that the lists only contain integers.

```python
def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))  # Recursively flatten sublists
        else:
            result.append(item)
    return result
```

#### **17. Group List Elements by Frequency Using a Dictionary**

**Question**: Write a function that groups elements of a list into dictionaries where the keys are the elements and the values are their counts.

```python
def group_by_frequency(lst):
    frequency = {}
    for elem in lst:
        frequency[elem] = frequency.get(elem, 0) + 1
    return frequency
```

#### **18. Find the Pair with the Closest Sum to a Target**

**Question**: Given a list of integers and a target sum, find the two elements whose sum is closest to the target.

```python
def closest_pair(lst, target):
    lst.sort()
    left, right = 0, len(lst) - 1
    closest_sum = float('inf')
    closest_pair = None
    
    while left < right:
        current_sum = lst[left] + lst[right]
        if abs(current_sum - target) < abs(closest_sum - target):
            closest_sum = current_sum
            closest_pair = (lst[left], lst[right])
        
        if current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
        else:
            break  # Exact match found
    
    return closest_pair
```

---

### **Explanation of Complexity (Time and Space) for These Questions**

* **Time Complexity**:

  * **O(n)** for linear operations like iterating through the list/dictionary.
  * **O(n log n)** for sorting operations (e.g., `merge_sorted_lists`).
  * **O(n^2)** for nested loops, but most of the examples above are optimized to O(n).

* **Space Complexity**:

  * **O(n)** for storing extra data (e.g., frequency count, intermediate results in a dictionary).
  * **O(1)** for in-place operations like reversing a list or checking for equality.

---


Here are some **medium-level interview problems** involving **lists** and **dictionaries**. These problems test your ability to manipulate these data structures efficiently, and many of them require you to combine multiple concepts such as **searching**, **sorting**, **dynamic programming**, and **hashing**.



Memorizing **time complexity** and **space complexity** can be challenging at first, but once you break down the concepts and use strategies to reinforce your understanding, it becomes much easier. Here are some practical and easy ways to **memorize and calculate complexity** for algorithms:

### **1. Understand Big O Notation Basics**

Before jumping into memorizing individual complexities, it's important to get a strong grasp of **Big O notation** and what it represents:

* **Big O notation** describes the **upper bound** of the time or space an algorithm will take as the input grows larger.
* It gives us an idea of **how an algorithm's performance will scale** with the input size.

### **2. Group Algorithms by Patterns**

Most algorithm time complexities fall into common patterns. By recognizing these patterns, you can quickly estimate the complexity without needing to memorize everything. Here's how you can group them:

* **Constant Time: O(1)**: No matter the input size, the operation takes the same amount of time.

  * Example: Accessing an element in an array by index.

* **Linear Time: O(n)**: The time increases linearly with the size of the input.

  * Example: Traversing through a list or array.

* **Quadratic Time: O(n²)**: Time increases with the square of the input size. This happens often with **nested loops**.

  * Example: Bubble sort or selection sort.

* **Logarithmic Time: O(log n)**: Time increases logarithmically with the size of the input.

  * Example: Binary search.

* **Linearithmic Time: O(n log n)**: Time increases linearly and logarithmically.

  * Example: Merge sort or quicksort.

* **Exponential Time: O(2^n)**: Time doubles with each additional input element.

  * Example: Recursive solutions for problems like the Fibonacci sequence.

### **3. Use Analogies to Visualize Complexity**

#### **1. Constant Time (O(1))**:

* Imagine having a **light switch**. It doesn’t matter if there are 1000 lightbulbs or just one—the action of turning the switch on or off takes the same amount of time.

#### **2. Linear Time (O(n))**:

* Think of **reading a book** where you read each page one after the other. The time to finish depends on the number of pages, i.e., the input size.

#### **3. Quadratic Time (O(n²))**:

* Think of **double-checking every pair of people** in a room to see if they are friends. For each person, you check against every other person. This is O(n²) because for each element you do n operations.

#### **4. Logarithmic Time (O(log n))**:

* Imagine you are looking for a **specific page in a dictionary**. You start by opening the middle, and depending on whether the word is before or after, you cut the search space in half. This is logarithmic search.

#### **5. Linearithmic Time (O(n log n))**:

* Think of **merging sorted lists**. You need to go through all elements (O(n)) and for each element, you do a logarithmic search (O(log n)).

#### **6. Exponential Time (O(2^n))**:

* Imagine you're making **all possible combinations of yes/no answers**. For every element, you have two choices, and it doubles with each additional input.

### **4. Use Mnemonics for Common Complexities**

You can make mnemonics or little memory tricks to help remember which operations lead to which time complexity. For example:

* **"Bunny Sorts" for O(n²)**: Imagine a bunny hopping through **all pairs** of elements in a list, checking them one by one.
* **"Bookshelf Binary Search" for O(log n)**: You start with a large bookshelf and always pick the middle book, cutting the search area in half each time.

### **5. Learn by Doing (Practice)**

The best way to remember complexities is to **practice coding**. As you work on more algorithms, you'll start to recognize common patterns of complexity.

* Try solving different problems and **write down the time complexity** as you solve them.
* Use **real-world examples** like sorting algorithms (bubble sort vs quicksort) to understand how their time complexity grows with input size.

### **6. Use the "Counting Steps" Method for Complexity Calculation**

To understand the complexity of an algorithm, count the number of **basic operations** (like comparisons, assignments, etc.). Here's how you can do it:

* **For loops**: Count how many times they run.

  * Example: `for i in range(n):` runs **n** times, so it’s **O(n)**.
* **Nested loops**: Multiply the number of iterations in each loop.

  * Example: `for i in range(n): for j in range(n):` runs **n × n** times, so it's **O(n²)**.
* **Recursive calls**: Use **recurrence relations** to estimate the complexity of recursive algorithms.

  * Example: The recursive Fibonacci function has **O(2^n)** complexity because it makes two calls at each step.

### **7. Simplify Complexities Using Big O Rules**

* **Addition**: If you have two parts in an algorithm with complexities **O(n)** and **O(n²)**, the overall complexity is **O(n²)** because the larger term dominates as the input grows.
* **Multiplication**: For nested loops, multiply their complexities.

  * Example: A loop inside another loop, both running `n` times, results in **O(n × n) = O(n²)**.
* **Division**: When dividing input size, the complexity typically becomes logarithmic.

  * Example: Binary search divides the search space in half each time, so it's **O(log n)**.

### **8. Use Complexity Cheat Sheets**

You can use **cheat sheets** to quickly refer to the most common complexities. Many of them categorize complexities for sorting algorithms, searching algorithms, tree and graph traversals, and dynamic programming.

Here’s a sample cheat sheet:

* **O(1)**: Direct access or constant time operations (e.g., accessing array index).
* **O(n)**: Looping through each element in a list.
* **O(n log n)**: Efficient sorting algorithms (e.g., merge sort, quicksort).
* **O(n²)**: Nested loops for comparisons (e.g., bubble sort).
* **O(2^n)**: Recursive algorithms that explore all possibilities (e.g., Fibonacci without memoization).

### **9. Practice with Real Problems**

Solve problems with well-known time complexities:

* **Bubble Sort** → O(n²)
* **Binary Search** → O(log n)
* **Merge Sort** → O(n log n)
* **Linked List Traversal** → O(n)
* **Matrix Multiplication** → O(n³)

After solving these problems, try calculating the complexity **before** you run them, and then check your answer.

### **10. Visualization Tools**

There are several tools that allow you to **visualize time complexities**:

* Use online visualizers for sorting algorithms (e.g., **visuAlgo**).
* Graph tools like **Big-O calculator** show how algorithms grow with input size, which can help you visualize time complexity in action.

---

### **Key Takeaways for Memorizing Complexity**:

1. **Group algorithms by common patterns** (e.g., linear, logarithmic).
2. **Understand the behavior** of common data structures and algorithms.
3. Use **mnemonics** and **visual analogies** to connect concepts.
4. **Practice regularly** and calculate complexities as you solve problems.
5. **Simplify complexities** using Big O rules (e.g., addition, multiplication).
6. **Use cheat sheets and references** when needed.
7. **Apply your knowledge** by solving a wide range of problems with varying complexities.
# consistent practice and by following these strategies, the process of memorizing and calculating time and space complexities will become much easier and more intuitive.


Sure! Let’s break down **time complexity** and **space complexity** in a simple way.

### **What is Time Complexity?**

Time complexity tells us how **long** an algorithm will take to complete, **based on the size of the input**. The bigger the input, the more time it takes. It’s like asking: *“How much time does my solution take to finish as the number of things I’m working with gets bigger?”*

For example:

* **O(1)**: Constant time – No matter how big your input is, it always takes the same amount of time.
* **O(n)**: Linear time – If the input grows bigger, the time it takes grows directly with it.
* **O(n²)**: Quadratic time – If you double the input, the time will increase **four times** (for nested loops, like a double for-loop).

### **What is Space Complexity?**

Space complexity tells us how much **memory** (space) the algorithm needs to complete. It's like asking: *“How much room do I need to store the things I’m working with?”*

For example:

* **O(1)**: Constant space – No matter how big the input is, it doesn’t need any extra space.
* **O(n)**: Linear space – The memory needed grows with the input size.
* **O(n²)**: Quadratic space – The memory needed grows very quickly as the input grows.

---

### **Simple Examples to Understand Time Complexity**

#### **1. Constant Time – O(1)**

Imagine you have a **light switch**. Whether you have one light or 100 lights, **turning the switch on** or **off** takes the same amount of time.

Example:

```python
def turn_on_light():
    return "Light turned on"  # No matter what, it only takes 1 step.
```

* **Time Complexity**: **O(1)** because it’s always the same time, no matter the input.

#### **2. Linear Time – O(n)**

Now, think of **reading a book** where you read one page at a time. If the book has 10 pages, it will take 10 steps. If it has 100 pages, it will take 100 steps.

Example:

```python
def print_numbers(n):
    for i in range(n):  # You go through each number one at a time
        print(i)
```

* **Time Complexity**: **O(n)** because it depends directly on the number of pages (input size).

#### **3. Quadratic Time – O(n²)**

Imagine you’re checking **pairs of people** at a party to see if they’re friends. For each person, you check them against **every other person**.

Example:

```python
def check_pairs(people):
    for i in range(len(people)):  # First loop
        for j in range(len(people)):  # Second loop
            print(f"Checking pair: {people[i]} and {people[j]}")
```

* **Time Complexity**: **O(n²)** because for every person, you check them against everyone else. If there are 10 people, it takes 100 steps (10 × 10).

---

### **Quick Way to Remember Complexities**

Here’s a simple way to remember the basic complexities:

1. **O(1)**: **Constant time** – Does not depend on input size.

   * Example: Getting the 10th item in a list.

2. **O(n)**: **Linear time** – Time increases with the size of the input.

   * Example: Traversing through a list of size `n`.

3. **O(n²)**: **Quadratic time** – Time increases very fast with input size, often caused by nested loops.

   * Example: Bubble Sort.

4. **O(log n)**: **Logarithmic time** – Time increases slowly as the input grows. It’s like halving the input each time (binary search).

   * Example: Binary Search in a sorted list.

5. **O(n log n)**: **Linearithmic time** – This is a combination of linear and logarithmic, often seen in efficient sorting algorithms (like Merge Sort and Quick Sort).

   * Example: Sorting a list with Merge Sort.

---

### **How to Calculate Complexity**

When you calculate time complexity, you **count the number of operations** (steps) your algorithm takes.

* For **loops**, count how many times they run.

  * Example: A loop that runs `n` times is **O(n)**.
  * A loop inside another loop (nested loops) that runs `n` times inside another `n` is **O(n²)**.

* For **recursion** (functions that call themselves), use the **recurrence relation**.

  * Example: For Fibonacci, each function calls two others, leading to **O(2^n)** time complexity.

---

### **Tips for Memorizing Complexity**

1. **Use Simple Analogies**: Think of real-world examples, like a light switch for O(1), or reading a book for O(n).

2. **Group by Patterns**: Most algorithms fall into patterns, so recognizing these can help. For example:

   * Linear problems: O(n)
   * Nested loops: O(n²)
   * Divide and conquer: O(log n) or O(n log n)

3. **Practice with Examples**: The more you practice, the more these complexities will stick. Try calculating complexity for common algorithms like sorting and searching.

4. **Use Cheat Sheets**: Keep a reference sheet that lists common algorithms and their complexities.

---

### **Key Takeaways**

* **Time Complexity**: How long an algorithm takes as the input grows (e.g., O(n), O(log n)).
* **Space Complexity**: How much memory an algorithm uses as the input grows (e.g., O(n)).
* **Memorizing**: Think of real-world examples, practice with algorithms, and use simple mnemonics.

With time, these concepts will start to feel more natural. Keep practicing, and it’ll become second nature!











### **Medium-Level Python Interview Problems**

---

### **1. Longest Substring Without Repeating Characters**

**Problem**: Given a string, find the length of the longest substring without repeating characters.

```python
def length_of_longest_substring(s: str) -> int:
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length
```

**Explanation**:

* This is a **sliding window** problem where you dynamically adjust the left and right pointers to maintain a substring with no repeating characters.
* **Time Complexity**: `O(n)`, as each character is processed at most twice (once added, once removed).
* **Space Complexity**: `O(min(n, m))`, where `n` is the size of the string and `m` is the number of unique characters in the string (constant for alphabet-based characters).

---

### **2. Top K Frequent Elements**

**Problem**: Given a list of integers, return the `k` most frequent elements.

```python
from collections import Counter

def top_k_frequent(nums, k):
    count = Counter(nums)
    return [item for item, _ in count.most_common(k)]
```

**Explanation**:

* We use `Counter` from the `collections` module to count the frequency of elements.
* Then, `most_common(k)` helps return the top `k` frequent elements.
* **Time Complexity**: `O(n log k)`, due to the internal heap used by `most_common()`.
* **Space Complexity**: `O(n)` to store the frequencies in a `Counter` object.

---

### **3. 3Sum**

**Problem**: Given an array `nums` of `n` integers, return all unique triplets `[nums[i], nums[j], nums[k]]` such that `i != j != k` and `nums[i] + nums[j] + nums[k] == 0`.

```python
def three_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue  # Skip duplicate values for `i`

        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicates for `left` and `right`
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return result
```

**Explanation**:

* First, we **sort the array**. Then, for each element, use a two-pointer approach to find pairs that sum up to `-nums[i]`.
* **Time Complexity**: `O(n^2)` because of sorting and the two-pointer iteration.
* **Space Complexity**: `O(1)` (ignoring the space used by the result array).

---

### **4. Subarray Sum Equals K**

**Problem**: Given an array of integers and a target integer `k`, return the total number of continuous subarrays whose sum equals `k`.

```python
from collections import defaultdict

def subarray_sum(nums, k):
    prefix_sum = defaultdict(int)
    prefix_sum[0] = 1
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num
        if current_sum - k in prefix_sum:
            count += prefix_sum[current_sum - k]
        prefix_sum[current_sum] += 1

    return count
```

**Explanation**:

* The idea is to use a **prefix sum** and a **hashmap** to keep track of the frequency of prefix sums encountered so far.
* For each element, we check if the difference between the current prefix sum and `k` has been encountered before. If so, it means a subarray sum of `k` exists.
* **Time Complexity**: `O(n)`.
* **Space Complexity**: `O(n)` for the hashmap that stores the prefix sums.

---

### **5. Valid Anagram**

**Problem**: Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

```python
from collections import Counter

def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
```

**Explanation**:

* We use `Counter` to count the frequency of each character in both strings and compare them.
* **Time Complexity**: `O(n)`, where `n` is the length of the strings.
* **Space Complexity**: `O(n)` to store the character counts.

---

### **6. Container With Most Water**

**Problem**: You are given an integer array `height` representing the height of vertical lines drawn on a coordinate plane. Find the maximum area of water that can be trapped between any two lines.

```python
def max_area(height):
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area
```

**Explanation**:

* We use a **two-pointer** approach where the pointers move toward each other, calculating the area between the two lines at each step and updating the maximum area.
* **Time Complexity**: `O(n)`.
* **Space Complexity**: `O(1)`.

---

### **7. Word Pattern**

**Problem**: Given a pattern and a string `s`, return `true` if `s` follows the same pattern.

```python
def word_pattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False

    map_pattern_to_word = {}
    map_word_to_pattern = {}

    for p, w in zip(pattern, words):
        if map_pattern_to_word.get(p) != w or map_word_to_pattern.get(w) != p:
            return False
        map_pattern_to_word[p] = w
        map_word_to_pattern[w] = p

    return True
```

**Explanation**:

* This problem requires using **two dictionaries** to map the pattern to the words and vice versa to ensure that each character maps to a unique word and vice versa.
* **Time Complexity**: `O(n)`, where `n` is the length of the string.
* **Space Complexity**: `O(n)` for the two mappings.

---

### **8. Largest Palindromic Substring**

**Problem**: Given a string, return the largest palindromic substring.

```python
def longest_palindromic_substring(s):
    def expand_from_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        # Odd-length palindrome
        odd_palindrome = expand_from_center(i, i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        # Even-length palindrome
        even_palindrome = expand_from_center(i, i + 1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome

    return longest
```

**Explanation**:

* This problem uses the **expand-around-center** technique, where we expand around each possible center to find the longest palindrome.
* **Time Complexity**: `O(n^2)`.
* **Space Complexity**: `O(1)`.

---

### **9. Find All Duplicates in an Array**

**Problem**: Given an integer array, return all the elements that appear more than once in the array.

```python
def find_duplicates(nums):
    duplicates = []
    for num in nums:
        if nums[abs(num)] < 0:
            duplicates.append(abs(num))
        else:
            nums[abs(num)] = -nums[abs(num)]
    return duplicates
```

**Explanation**:

* The idea is to **modify the array in place** by marking elements as negative when we encounter them, which allows us to track duplicates without using extra space.
* **Time Complexity**: `O(n)`.
* **Space Complexity**: `O(1)`.

---

### **Conclusion**

**medium-level Python interview problems** involving **lists and dictionaries** will challenge you to think critically about common patterns like **sliding windows**, **two-pointer technique**, **hashing**,


**common DSA problems** related to **lists** and **dictionaries**. I'll cover a variety of problems that come up frequently in coding interviews and competitive programming. These will help you build a strong foundation for solving problems efficiently.

Certainly! Here’s a **summary table** that outlines the **time complexity** and **space complexity** for different cases in the problems discussed. We’ll categorize based on common scenarios and explain how these complexities arise.

### **Summary of Time and Space Complexities**

| **Problem**                         | **Time Complexity** | **Space Complexity** | **Explanation**                                                                                          |
| ----------------------------------- | ------------------- | -------------------- | -------------------------------------------------------------------------------------------------------- |
| **Two Sum**                         | `O(n)`              | `O(n)`               | One pass through the list, using a dictionary to store seen numbers.                                     |
| **Maximum Subarray Sum (Kadane's)** | `O(n)`              | `O(1)`               | Single iteration over the list, with just a few variables for tracking the current and max sums.         |
| **Move Zeros to the End**           | `O(n)`              | `O(1)`               | Single pass through the array, swapping in-place.                                                        |
| **Find Missing Number (1 to N)**    | `O(n)`              | `O(1)`               | One pass to sum the array and compute the difference from the expected sum.                              |
| **Rotate Array**                    | `O(n)`              | `O(n)`               | Array slicing requires creating new arrays, hence extra space and linear time complexity.                |
| **Merge Intervals**                 | `O(n log n)`        | `O(n)`               | Sorting the intervals first takes `O(n log n)`, followed by a linear pass to merge intervals.            |
| **Find Duplicate in Array**         | `O(n)`              | `O(1)`               | Floyd’s Tortoise and Hare algorithm uses constant space, with two pointers to detect cycles.             |
| **Subarray Sum Equals K**           | `O(n)`              | `O(n)`               | We use a hashmap (or defaultdict) to store cumulative sums, and iterate through the array once.          |
| **Product of Array Except Self**    | `O(n)`              | `O(1)`               | Two passes over the list, computing left and right products, all done in-place using the `output` array. |
| **Kth Largest Element**             | `O(n log k)`        | `O(k)`               | Heap-based approach or sorting, where heap operations are efficient for small `k`.                       |
| **Longest Increasing Subsequence**  | `O(n^2)`            | `O(n)`               | Nested iteration through the array, using dynamic programming to store intermediate results.             |
| **Partition Equal Subset Sum**      | `O(n * sum(nums))`  | `O(sum(nums))`       | Uses dynamic programming with a 1D array to track possible subset sums.                                  |
| **Find Missing Number (1 to N)**    | `O(n)`              | `O(1)`               | One pass through the list, using a simple sum formula to determine the missing number.                   |

---

### **Key Takeaways:**

1. **Linear Time Complexity (`O(n)`)**:

   * Problems where you only need to **traverse the array once** and make **constant-time operations** (like checks, updates, or lookups) are generally `O(n)`.
   * Examples: `Two Sum`, `Maximum Subarray Sum`, `Move Zeros to the End`, `Find Missing Number`, `Find Duplicate in Array`.

2. **Quadratic Time Complexity (`O(n^2)`)**:

   * Problems involving **nested loops** where each element is compared to every other element often result in `O(n^2)`.
   * Example: `Longest Increasing Subsequence` with dynamic programming.

3. **Logarithmic Time Complexity**:

   * **Sorting** or problems where you can **reduce the problem size logarithmically** (like binary search or heap operations) often involve logarithmic complexity.
   * Example: `Kth Largest Element` with a heap or sorting.
   * Merge Intervals: `O(n log n)` due to sorting.

4. **Space Complexity**:

   * **Constant space (`O(1)`)**: These algorithms use a few variables and do not require additional data structures.

     * Example: `Maximum Subarray Sum`, `Find Missing Number`, `Find Duplicate in Array`.
   * **Linear space (`O(n)`)**: When the algorithm needs to store some form of intermediate data, like a hashmap or list, proportional to the size of the input.

     * Example: `Subarray Sum Equals K`, `Merge Intervals`, `Product of Array Except Self`.

5. **Linearithmic Time Complexity (`O(n log n)`)**:

   * **Sorting-based algorithms** or algorithms that break the input into smaller subproblems, such as **merge** or **quick sort**.
   * Example: `Merge Intervals`.

6. **Space Complexity with `O(n)`**:

   * When storing intermediate states, such as prefix sums or cumulative results, or when sorting requires additional space (e.g., Merge Sort).
   * Example: `Merge Intervals`, `Subarray Sum Equals K`.

7. **Dynamic Programming**:

   * Problems that require maintaining **state over multiple subproblems** will often have both time and space complexity proportional to `n` or the total size of the possible subsets.
   * Example: `Partition Equal Subset Sum`.

---

### **When to Choose One Approach Over Another?**

* **Time Complexity (`O(n)`)** is optimal for problems where you can solve them with a **single pass** or **constant-time operations**.

  * **Best for: Search-based problems, counting, or linear traversals.**

* **Space Complexity (`O(n)`)** becomes relevant when we need to store intermediate states or results (like using a hashmap, set, or list).

  * **Best for: Storing dynamic states (prefix sums, hashes), or when sorting requires extra space.**

* **Sorting Problems (`O(n log n)`)**: If sorting is required for solving the problem efficiently, the time complexity often involves `O(n log n)`.

  * **Best for: Problems that need ordering (merge intervals, kth largest).**

* **Dynamic Programming (`O(n^2)` or `O(n * sum(nums))`)**: These algorithms use extra space to store intermediate results and may involve multiple iterations or recursive subproblems.

  * **Best for: Problems involving subset sums or sequences.**

---

Would you like further clarification on any specific case or problem?

---

### **1. Two Sum (Using List and Dictionary)**

#### Problem:

Given an array of integers, return the indices of the two numbers that add up to a specific target.

#### Solution:

* Use a **hashmap (dictionary)** to store the complement of each number as you iterate through the list.

```python
def two_sum(nums, target):
    seen = {}  # Dictionary to store complement values
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]  # Return indices of the pair
        seen[num] = i
    return None  # If no solution found
```

**Time Complexity**: `O(n)`
**Space Complexity**: `O(n)`

---

### **2. Majority Element (Using Dictionary)**

#### Problem:

Given an array of size `n`, find the majority element (an element that appears more than `n/2` times).

#### Solution:

* Use a **hashmap (dictionary)** to count occurrences of each element.

```python
from collections import Counter

def majority_element(nums):
    count = Counter(nums)
    majority_count = len(nums) // 2
    for num, freq in count.items():
        if freq > majority_count:
            return num
    return None
```

**Time Complexity**: `O(n)`
**Space Complexity**: `O(n)`

---

### **3. Group Anagrams (Using Dictionary)**

#### Problem:

Group a list of strings into anagrams (strings that can be rearranged to form each other).

#### Solution:

* Use a **dictionary** where the key is the sorted version of the string, and the value is a list of anagrams.

```python
from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)
    for word in strs:
        key = ''.join(sorted(word))
        anagrams[key].append(word)
    return list(anagrams.values())
```

**Time Complexity**: `O(n * k log k)` where `n` is the number of strings and `k` is the average length of the strings
**Space Complexity**: `O(n * k)`

---

### **4. Sliding Window Maximum (Using Deque + List)**

#### Problem:

Given an array, find the maximum value in each sliding window of size `k`.

#### Solution:

* Use a **deque** (double-ended queue) to store indices of array elements in decreasing order.

```python
from collections import deque

def sliding_window_max(nums, k):
    result = []
    window = deque()
    
    for i, num in enumerate(nums):
        # Remove indices that are out of the window
        if window and window[0] < i - k + 1:
            window.popleft()
        
        # Remove smaller elements in the window
        while window and nums[window[-1]] < num:
            window.pop()
        
        # Add the current element index
        window.append(i)
        
        # Add the maximum element of the current window to result
        if i >= k - 1:
            result.append(nums[window[0]])
    
    return result
```

**Time Complexity**: `O(n)`
**Space Complexity**: `O(k)`

---

### **5. Longest Substring Without Repeating Characters (Using Dictionary)**

#### Problem:

Given a string, find the length of the longest substring without repeating characters.

#### Solution:

* Use a **sliding window** with a **hashmap** to track the most recent index of each character.

```python
def longest_substring(s):
    char_index = {}
    left = 0
    max_len = 0

    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1
        
        char_index[s[right]] = right
        max_len = max(max_len, right - left + 1)

    return max_len
```

**Time Complexity**: `O(n)`
**Space Complexity**: `O(min(n, m))` where `n` is the length of the string and `m` is the number of characters in the character set.

---

### **6. Find Intersection of Two Arrays (Using Dictionary)**

#### Problem:

Given two arrays, return their intersection.

#### Solution:

* Use a **set** or **hashmap (dictionary)** to store the elements of one array and check for existence in the other.

```python
def intersection(nums1, nums2):
    set1 = set(nums1)
    return list(set1 & set(nums2))  # Intersection using set
```

**Time Complexity**: `O(n + m)` where `n` and `m` are the lengths of the two arrays
**Space Complexity**: `O(n + m)`

---

### **7. Validate Subsequence (Using List)**

#### Problem:

Given a sequence `s` and a target string `t`, check if `s` is a subsequence of `t`.

#### Solution:

* Use two pointers to check if all characters of `s` appear in `t` in order.

```python
def is_subsequence(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)
```

**Time Complexity**: `O(n + m)` where `n` is the length of `s` and `m` is the length of `t`
**Space Complexity**: `O(1)`

---

### **8. Palindrome Permutation (Using Dictionary)**

#### Problem:

Given a string, check if any permutation of the string could form a palindrome.

#### Solution:

* Count the frequency of characters using a **dictionary** and check if there’s at most one character with an odd frequency.

```python
from collections import Counter

def can_permute_palindrome(s):
    count = Counter(s)
    odd_count = sum(1 for freq in count.values() if freq % 2 != 0)
    return odd_count <= 1
```

**Time Complexity**: `O(n)` where `n` is the length of the string
**Space Complexity**: `O(n)`

---

### **9. Top K Frequent Elements (Using Dictionary and Heap)**

#### Problem:

Given a list of numbers, return the `k` most frequent elements.

#### Solution:

* Use a **dictionary** to count frequencies, then use a **heap** to get the top `k` frequent elements.

```python
from collections import Counter
import heapq

def top_k_frequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=lambda x: count[x])
```

**Time Complexity**: `O(n log k)` where `n` is the length of the list
**Space Complexity**: `O(n)`

---

### **10. Subarray Sum Equals K (Using Dictionary)**

#### Problem:

Given an array of integers, find the total number of continuous subarrays whose sum equals `k`.

#### Solution:

* Use a **prefix sum** with a **dictionary** to store the frequency of each sum.

```python
def subarray_sum(nums, k):
    prefix_sum = {0: 1}
    current_sum = 0
    result = 0
    
    for num in nums:
        current_sum += num
        if current_sum - k in prefix_sum:
            result += prefix_sum[current_sum - k]
        
        prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
    
    return result
```

**Time Complexity**: `O(n)`
**Space Complexity**: `O(n)`

---

These code blocks represent key **patterns and techniques** for solving common problems involving **lists** and **dictionaries**. They form the basis for solving many interview-style questions and competitive programming problems. Each problem utilizes efficient data structures and algorithms, making them crucial to mastering DSA concepts.

Would you like to dive deeper into any specific problem or code block?


**common DSA problems** that specifically involve **lists (arrays)**. These problems will help you hone your understanding of **list manipulations** and improve your problem-solving skills.

---

Certainly! Understanding **time complexity** and **space complexity** is key to evaluating the efficiency of algorithms, especially in coding interviews and competitive programming. Let’s break down the **time complexity** and **space complexity** for different problems you've asked about, using **Big O notation**. We'll discuss how they are derived and why they differ in each case.

### **1. Two Sum**

```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None
```

#### **Time Complexity: `O(n)`**

* **Reason**: We traverse the list once (from start to end), performing a constant time dictionary lookup (`seen[complement]`) for each element.

  * Accessing a dictionary and checking for existence is `O(1)` on average.
  * Therefore, the time complexity is proportional to the length of the list: **O(n)**.

#### **Space Complexity: `O(n)`**

* **Reason**: The `seen` dictionary stores up to `n` elements (in the worst case).

  * In the worst case, we may need to store every number in the array (if no two numbers sum up to the target), so the space complexity is proportional to the size of the input array: **O(n)**.

---

### **2. Maximum Subarray Sum (Kadane’s Algorithm)**

```python
def max_subarray_sum(nums):
    max_so_far = max_ending_here = nums[0]
    for num in nums[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
```

#### **Time Complexity: `O(n)`**

* **Reason**: The algorithm iterates over the array only once.

  * For each element, we perform constant time operations (comparisons and additions).
  * Hence, the time complexity is **O(n)**.

#### **Space Complexity: `O(1)`**

* **Reason**: The algorithm uses only a constant amount of space to store variables (`max_so_far`, `max_ending_here`), irrespective of the input size.

  * No additional data structures (like arrays or hashmaps) are used, so the space complexity is **O(1)**.

---

### **3. Move Zeros to the End**

```python
def move_zeros_to_end(nums):
    non_zero_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            non_zero_index += 1
    return nums
```

#### **Time Complexity: `O(n)`**

* **Reason**: We iterate over the array once, and for each element, we perform a constant-time operation (`if` check and potential swap).

  * Therefore, the time complexity is **O(n)**.

#### **Space Complexity: `O(1)`**

* **Reason**: The algorithm uses a constant amount of extra space. We’re just using a few variables (`non_zero_index` and `i`), and the array is modified in place.

  * So, the space complexity is **O(1)**.

---

### **4. Find Missing Number (1 to N)**

```python
def find_missing_number(nums):
    n = len(nums)
    expected_sum = (n + 1) * (n + 2) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
```

#### **Time Complexity: `O(n)`**

* **Reason**: The function computes the sum of all numbers in the array, which takes **O(n)** time, where `n` is the length of the array.

  * The rest of the operations (sum and arithmetic) take constant time, so the overall time complexity is **O(n)**.

#### **Space Complexity: `O(1)`**

* **Reason**: The algorithm uses a constant amount of space (just a few variables like `n`, `expected_sum`, `actual_sum`).

  * No additional data structures are used, so the space complexity is **O(1)**.

---

### **5. Rotate Array**

```python
def rotate_array(nums, k):
    k = k % len(nums)
    return nums[-k:] + nums[:-k]
```

#### **Time Complexity: `O(n)`**

* **Reason**: The slicing operation (`nums[-k:]` and `nums[:-k]`) involves creating two subarrays, each of size `n`.

  * Hence, copying the subarrays takes **O(n)** time.
  * The rest of the operations are constant time, so the time complexity is **O(n)**.

#### **Space Complexity: `O(n)`**

* **Reason**: The function creates a new list to store the rotated result (`nums[-k:] + nums[:-k]`), which requires `O(n)` extra space.

  * Therefore, the space complexity is **O(n)**.

---

### **6. Merge Intervals**

```python
def merge_intervals(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for interval in intervals[1:]:
        if merged[-1][1] >= interval[0]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)
    
    return merged
```

#### **Time Complexity: `O(n log n)`**

* **Reason**: Sorting the intervals takes **O(n log n)** time. After sorting, we go through the list once to merge intervals, which takes **O(n)** time.

  * Hence, the overall time complexity is **O(n log n)** due to the sorting step.

#### **Space Complexity: `O(n)`**

* **Reason**: The space complexity is **O(n)** because, in the worst case, we might store all the intervals in the `merged` list. Sorting is done in place, but we still require space for the merged result.

  * Hence, the space complexity is **O(n)**.

---

### **7. Find Duplicate in Array**

```python
def find_duplicate(nums):
    slow = nums[0]
    fast = nums[0]
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow
```

#### **Time Complexity: `O(n)`**

* **Reason**: In the first loop, the `fast` pointer moves two steps at a time and the `slow` pointer moves one step at a time. They will eventually meet inside the cycle. This takes **O(n)** time.

  * The second loop also takes **O(n)** time to find the starting point of the cycle.
  * So, the overall time complexity is **O(n)**.

#### **Space Complexity: `O(1)`**

* **Reason**: The algorithm uses only two pointers (`slow` and `fast`) and no extra space to store data structures.

  * Therefore, the space complexity is **O(1)**.

---

### **8. Subarray Sum Equals K**

```python
from collections import defaultdict

def subarray_sum(nums, k):
    prefix_sum = defaultdict(int)
    prefix_sum[0] = 1
    current_sum = 0
    result = 0
    
    for num in nums:
        current_sum += num
        if current_sum - k in prefix_sum:
            result += prefix_sum[current_sum - k]
        prefix_sum[current_sum] += 1
    
    return result
```

#### **Time Complexity: `O(n)`**

* **Reason**: We iterate over the list once, and each dictionary operation (check if `current_sum - k` exists, increment count) is **O(1)** on average.

  * Therefore, the time complexity is **O(n)**.

#### **Space Complexity: `O(n)`**

* **Reason**: We use a `defaultdict` to store the cumulative sum frequencies, which can store up to `n` different cumulative sums in the worst case.

  * Therefore, the space complexity is **O(n)**.

---

### **9. Product of Array Except Self**

```python
def product_except_self(nums):
    n = len(nums)
    output = [1] * n
    
    left = 1
    for i in range(n):
        output[i] *= left
        left *= nums[i]
    
    right = 1
    for i in range(n - 1, -1, -1):
        output[i] *= right
        right *= nums[i]
    
    return output
```

#### **Time Complexity: `O(n)`**

* **Reason**: We iterate over the list twice: once to compute the product of elements to the left and once to compute the product of elements to the right.

  * Therefore, the time complexity is **O(n)**.

#### **Space Complexity: `O(1)`**

* **Reason**: We use the `output` array to store the result, which takes **O(n)** space. However, the space complexity is considered **O(1)** since we’re using the output array for storage, and no additional space is used for intermediate




Traversal problems are a core part of any data structure interview, and understanding how to traverse through data structures like **arrays**, **linked lists**, **trees**, and **graphs** is essential.

Here are some **easy-level traversal problems** that you can practice to solidify your understanding of basic traversal techniques:

### **1. Traverse a List (Array)**

**Problem**: Given a list of integers, traverse and print all the elements.

```python
def traverse_list(nums):
    for num in nums:
        print(num)
```

**Explanation**:

* This is a basic traversal of a list (array) where each element is printed in order.
* **Time Complexity**: `O(n)`, where `n` is the number of elements in the list.
* **Space Complexity**: `O(1)`.

---

### **2. Find the Sum of Elements in a List**

**Problem**: Given a list of integers, find the sum of all the elements in the list.

```python
def sum_of_list(nums):
    total = 0
    for num in nums:
        total += num
    return total
```

**Explanation**:

* A simple traversal that aggregates the sum of the elements.
* **Time Complexity**: `O(n)`.
* **Space Complexity**: `O(1)`.

---

### **3. Reverse a Linked List (Iterative Approach)**

**Problem**: Reverse a singly linked list.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev
```

**Explanation**:

* This is an iterative solution where we reverse the pointers as we traverse the linked list.
* **Time Complexity**: `O(n)`, where `n` is the number of nodes in the linked list.
* **Space Complexity**: `O(1)`.

---

### **4. Traverse a Binary Tree (In-Order Traversal)**

**Problem**: Given a binary tree, return its **in-order traversal** as a list of values.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    result = []
    def helper(node):
        if node:
            helper(node.left)
            result.append(node.val)
            helper(node.right)
    
    helper(root)
    return result
```

**Explanation**:

* **In-order traversal** means we first visit the left subtree, then the current node, and finally the right subtree.
* **Time Complexity**: `O(n)`, where `n` is the number of nodes in the binary tree.
* **Space Complexity**: `O(h)`, where `h` is the height of the tree (due to recursion stack).

---

### **5. Traverse a Binary Tree (Pre-Order Traversal)**

**Problem**: Given a binary tree, return its **pre-order traversal** as a list of values.

```python
def preorder_traversal(root):
    result = []
    def helper(node):
        if node:
            result.append(node.val)
            helper(node.left)
            helper(node.right)
    
    helper(root)
    return result
```

**Explanation**:

* **Pre-order traversal** means we first visit the current node, then the left subtree, and finally the right subtree.
* **Time Complexity**: `O(n)`.
* **Space Complexity**: `O(h)`.

---

### **6. Traverse a Binary Tree (Post-Order Traversal)**

**Problem**: Given a binary tree, return its **post-order traversal** as a list of values.

```python
def postorder_traversal(root):
    result = []
    def helper(node):
        if node:
            helper(node.left)
            helper(node.right)
            result.append(node.val)
    
    helper(root)
    return result
```

**Explanation**:

* **Post-order traversal** means we first visit the left subtree, then the right subtree, and finally the current node.
* **Time Complexity**: `O(n)`.
* **Space Complexity**: `O(h)`.

---

### **7. Level Order Traversal of a Binary Tree (Breadth-First Search)**

**Problem**: Given a binary tree, return its **level order traversal** (BFS) as a list of values.

```python
from collections import deque

def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    
    return result
```

**Explanation**:

* **Level order traversal** is a **Breadth-First Search (BFS)** where we visit all nodes at the present depth level before moving on to nodes at the next depth level.
* **Time Complexity**: `O(n)`.
* **Space Complexity**: `O(n)` for the queue.

---

### **8. Traverse a Graph Using DFS (Depth-First Search)**

**Problem**: Given a graph (represented as an adjacency list), traverse it using **DFS** and return the nodes in the order they are visited.

```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited
```

**Explanation**:

* This function performs a **Depth-First Search** to visit all nodes in the graph, starting from the `start` node.
* **Time Complexity**: `O(V + E)`, where `V` is the number of vertices and `E` is the number of edges.
* **Space Complexity**: `O(V)` due to the recursive stack and the `visited` set.

---

### **9. Find the Height of a Binary Tree**

**Problem**: Given a binary tree, find its **height** (the number of edges on the longest path from the root to a leaf node).

```python
def tree_height(root):
    if not root:
        return -1
    
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    
    return max(left_height, right_height) + 1
```

**Explanation**:

* The height of a tree is defined as the length of the longest path from the root to a leaf node. The base case is when the node is `None`, returning `-1` (indicating no nodes).
* **Time Complexity**: `O(n)`, where `n` is the number of nodes in the tree.
* **Space Complexity**: `O(h)`, where `h` is the height of the tree (due to recursion).

---

### **10. Find the Depth of a Node in a Binary Tree**

**Problem**: Given a binary tree and a target value, find the depth of the node containing that value.

```python
def find_depth(root, target, depth=0):
    if not root:
        return -1
    
    if root.val == target:
        return depth
    
    left_depth = find_depth(root.left, target, depth + 1)
    if left_depth != -1:
        return left_depth
    
    return find_depth(root.right, target, depth + 1)
```

**Explanation**:

* This function recursively traverses the binary tree, passing the current depth at each node.
* **Time Complexity**: `O(n)`.
* **Space Complexity**: `O(h)` due to recursion.

---

### **11. Traverse a Linked List (Reverse Print)**

**Problem**: Given a singly linked list, print its elements in reverse order.

```python
def reverse_print_linked_list(head):
    stack = []
    while head:
        stack.append(head.val)
        head = head.next
    while stack:
        print(stack.pop())
```

**Explanation**:

* We first traverse the linked list, storing each element in a stack. Then, we pop and print the elements in reverse order.
* **Time Complexity**: `O(n)`.
* **Space Complexity**: `O(n)` due to the stack.

---

### **Conclusion**

**easy-level traversal problems** are designed to help you practice basic concepts of traversal in different data structures such as **arrays**, **linked lists**, **binary trees**, and **graphs**. Each problem introduces you to common traversal techniques like **Depth-First Search (DFS)**, **Breadth-First Search (BFS)**, and **recursive** or **iterative** solutions. As you practice these, you’ll strengthen your ability to traverse and process data structures in an efficient way.
