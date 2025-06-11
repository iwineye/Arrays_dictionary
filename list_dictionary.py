# Create a list
fruits = ['apple', 'banana', 'cherry']

# Add elements
fruits.append('orange')       # ['apple', 'banana', 'cherry', 'orange']
fruits.insert(1, 'kiwi')      # Insert at index 1

# Remove elements
fruits.remove('banana')       # Removes first occurrence
popped = fruits.pop()         # Removes and returns last item
del fruits[0]                 # Deletes element at index 0

# Access and modify
print(fruits[1])              # Access
fruits[1] = 'mango'           # Modify

# Slicing
print(fruits[1:3])            # ['mango', 'cherry']




squares = [x**2 for x in range(10)]   # [0, 1, 4, ..., 81]
evens = [x for x in range(10) if x % 2 == 0]


| Operation                    | Time Complexity |
| ---------------------------- | --------------- |
| Indexing (`list[i]`)         | O(1)            |
| Append (`list.append(x)`)    | O(1)            |
| Insert (`list.insert(i, x)`) | O(n)            |
| Delete (`del list[i]`)       | O(n)            |
| Search (in)                  | O(n)            |
| Iteration                    | O(n)            |
| Sort (`list.sort()`)         | O(n log n)      |



## Common Use-Cases

* Storing sequences of elements

* Stack/Queue implementations

* Searching/sorting problems

* Sliding window, two-pointer techniques


#Great! Let’s explore some **common DSA problems** that specifically involve **lists (arrays)**. These problems will help you hone your understanding of **list manipulations** and improve your problem-solving skills.

### **1. Two Sum**

#### Problem:

#Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

#### Solution:

#Use a dictionary to track the difference between `target` and the current number.


def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None


#Time Complexity**: `O(n)`
#**Space Complexity**: `O(n)`

### **2. Maximum Subarray Sum (Kadane’s Algorithm)**

#### Problem:

#Find the largest sum of any contiguous subarray in a given array.

#### Solution:

#Kadane’s Algorithm uses dynamic programming to solve this in `O(n)` time.


def max_subarray_sum(nums):
    max_so_far = max_ending_here = nums[0]
    for num in nums[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

#Time Complexity**: `O(n)`
#Space Complexity**: `O(1)`



### **3. Move Zeros to the End**

#### Problem:

#Given an array, move all zeros to the end without changing the order of non-zero elements.

#### Solution:

#Use the two-pointer technique to solve this problem in `O(n)` time.

def move_zeros_to_end(nums):
    non_zero_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            non_zero_index += 1
    return nums

#*Time Complexity**: `O(n)`
#*Space Complexity**: `O(1)`


### **4. Find Missing Number (1 to N)**

#### Problem:

#Given a list containing `n` distinct numbers taken from the range `1` to `n+1`, find the one number that is missing from the list.

#### Solution:

#The sum of the first `n+1` numbers can be used to find the missing number.


def find_missing_number(nums):
    n = len(nums)
    expected_sum = (n + 1) * (n + 2) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

#*Time Complexity**: `O(n)`
#*Space Complexity**: `O(1)`



### **5. Rotate Array (Left/Right)**

#### Problem:

#Rotate an array to the right by `k` steps. This should be done in `O(n)` time.

#### Solution:

#Use slicing to perform the rotation in `O(n)`.


def rotate_array(nums, k):
    k = k % len(nums)  # handle cases where k >= len(nums)
    return nums[-k:] + nums[:-k]

#*Time Complexity**: `O(n)`
#*Space Complexity**: `O(n)`

---

### **6. Merge Intervals**

#### Problem:

#Given a collection of intervals, merge all overlapping intervals.

#### Solution:

#Sort the intervals and merge them when necessary.


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

#**Time Complexity**: `O(n log n)` (due to sorting)
#**Space Complexity**: `O(n)`



### **7. Find Duplicate in Array**

#### Problem:

#Given an array `nums` containing `n+1` integers where each integer is between `1` and `n`, find the duplicate number.

#### Solution:

#Use **Floyd’s Tortoise and Hare Algorithm** to detect cycles in the array, which helps find duplicates in `O(n)` time.


def find_duplicate(nums):
    slow = nums[0]
    fast = nums[0]
    
    # Phase 1: Find the intersection point inside the cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # Phase 2: Find the entrance to the cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow

#**Time Complexity**: `O(n)`
#**Space Complexity**: `O(1)`



### **8. Subarray Sum Equals K**

#### Problem:

#Given an array `nums` and an integer `k`, find the total number of continuous subarrays whose sum equals `k`.

#### Solution:

#Use **prefix sums** and a **hashmap** to efficiently track the sums.

from collections import defaultdict

def subarray_sum(nums, k):
    prefix_sum = defaultdict(int)
    prefix_sum[0] = 1  # To handle cases where the subarray starts from the beginning
    current_sum = 0
    result = 0
    
    for num in nums:
        current_sum += num
        if current_sum - k in prefix_sum:
            result += prefix_sum[current_sum - k]
        prefix_sum[current_sum] += 1
    
    return result


#**Time Complexity**: `O(n)`
#**Space Complexity**: `O(n)`



### **9. Product of Array Except Self**

#### Problem:

#Given an array `nums`, return an array `output` such that `output[i]` is the product of all elements of `nums` except `nums[i]`.

#### Solution:

#Use two passes — one to calculate the product of elements before the current element and another for the product of elements after.

#```python
def product_except_self(nums):
    n = len(nums)
    output = [1] * n
    
    # Left product
    left = 1
    for i in range(n):
        output[i] *= left
        left *= nums[i]
    
    # Right product
    right = 1
    for i in range(n - 1, -1, -1):
        output[i] *= right
        right *= nums[i]
    
    return output

#**Time Complexity**: `O(n)`
#**Space Complexity**: `O(1)` (excluding the output array)

### **10. Longest Increasing Subsequence (LIS)**

#### Problem:

#Given an unsorted array of integers, find the length of the longest increasing subsequence.

#### Solution:

#Use dynamic programming with a time complexity of `O(n²)` or use binary search for an optimized solution with `O(n log n)`.

def length_of_lis(nums):
    if not nums:
        return 0
    
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)


#**Time Complexity**: `O(n²)`
#**Space Complexity**: `O(n)`


### **11. Find the "Kth" Largest Element**

#### Problem:

#Given an unsorted array, find the `k`th largest element.

#### Solution:

#Use the **Quickselect algorithm** or **heap** to efficiently find the `k`th largest element.


import heapq

def find_kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]

#**Time Complexity**: `O(n log k)`
#**Space Complexity**: `O(k)`



### **12. Partition Equal Subset Sum**

#### Problem:

#Given a set of positive integers, determine if the set can be partitioned into two subsets such that the sum of elements in both subsets is equal.

#### Solution:

#This is a **subset sum problem**, which can be solved with dynamic programming.


def can_partition(nums):
    total_sum = sum(nums)
    
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    return dp[target]

#*Time Complexity**: `O(n * sum(nums))`
#**Space Complexity**: `O(sum(nums))`


#These problems will give you ample practice on **list manipulation** and **common algorithmic techniques**. Each of these is frequently asked in coding interviews, so mastering them will make you well-prepared for most scenarios!
#Would you like more explanations or variations of these problems?








# Create a dictionary
person = {'name': 'Alice', 'age': 25}

# Access
print(person['name'])        # Alice
print(person.get('age'))     # 25

# Add or update
person['city'] = 'New York'
person['age'] = 26

# Remove
del person['age']
city = person.pop('city')    # Returns the value

# Keys, values, items
print(person.keys())         # dict_keys(['name'])
print(person.values())       # dict_values(['Alice'])
print(person.items())        # dict_items([('name', 'Alice')])


squares = {x: x**2 for x in range(5)}   # {0: 0, 1: 1, 2: 4, ...}







