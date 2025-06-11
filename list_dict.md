Great question! Let’s focus on some **relevant code blocks** that form the core of many **common DSA problems** related to **lists** and **dictionaries**. I'll cover a variety of problems that come up frequently in coding interviews and competitive programming. These will help you build a strong foundation for solving problems efficiently.

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

### **1. Two Sum**

#### Problem:

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

#### Solution:

Use a dictionary to track the difference between `target` and the current number.

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

**Time Complexity**: `O(n)`
**Space Complexity**: `O(n)`

---

### **2. Maximum Subarray Sum (Kadane’s Algorithm)**

#### Problem:

Find the largest sum of any contiguous subarray in a given array.

#### Solution:

Kadane’s Algorithm uses dynamic programming to solve this in `O(n)` time.

```python
def max_subarray_sum(nums):
    max_so_far = max_ending_here = nums[0]
    for num in nums[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
```

**Time Complexity**: `O(n)`
**Space Complexity**: `O(1)`

---

### **3. Move Zeros to the End**

#### Problem:

Given an array, move all zeros to the end without changing the order of non-zero elements.

#### Solution:

Use the two-pointer technique to solve this problem in `O(n)` time.

```python
def move_zeros_to_end(nums):
    non_zero_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            non_zero_index += 1
    return nums
```

**Time Complexity**: `O(n)`
**Space Complexity**: `O(1)`

---

### **4. Find Missing Number (1 to N)**

#### Problem:

Given a list containing `n` distinct numbers taken from the range `1` to `n+1`, find the one number that is missing from the list.

#### Solution:

The sum of the first `n+1` numbers can be used to find the missing number.

```python
def find_missing_number(nums):
    n = len(nums)
    expected_sum = (n + 1) * (n + 2) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
```

**Time Complexity**: `O(n)`
**Space Complexity**: `O(1)`

---

### **5. Rotate Array (Left/Right)**

#### Problem:

Rotate an array to the right by `k` steps. This should be done in `O(n)` time.

#### Solution:

Use slicing to perform the rotation in `O(n)`.

```python
def rotate_array(nums, k):
    k = k % len(nums)  # handle cases where k >= len(nums)
    return nums[-k:] + nums[:-k]
```

**Time Complexity**: `O(n)`
**Space Complexity**: `O(n)`

---

### **6. Merge Intervals**

#### Problem:

Given a collection of intervals, merge all overlapping intervals.

#### Solution:

Sort the intervals and merge them when necessary.

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

**Time Complexity**: `O(n log n)` (due to sorting)
**Space Complexity**: `O(n)`

---

### **7. Find Duplicate in Array**

#### Problem:

Given an array `nums` containing `n+1` integers where each integer is between `1` and `n`, find the duplicate number.

#### Solution:

Use **Floyd’s Tortoise and Hare Algorithm** to detect cycles in the array, which helps find duplicates in `O(n)` time.

```python
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
```

**Time Complexity**: `O(n)`
**Space Complexity**: `O(1)`

---

### **8. Subarray Sum Equals K**

#### Problem:

Given an array `nums` and an integer `k`, find the total number of continuous subarrays whose sum equals `k`.

#### Solution:

Use **prefix sums** and a **hashmap** to efficiently track the sums.

```python
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
```

**Time Complexity**: `O(n)`
**Space Complexity**: `O(n)`

---

### **9. Product of Array Except Self**

#### Problem:

Given an array `nums`, return an array `output` such that `output[i]` is the product of all elements of `nums` except `nums[i]`.

#### Solution:

Use two passes — one to calculate the product of elements before the current element and another for the product of elements after.

```python
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
```

**Time Complexity**: `O(n)`
**Space Complexity**: `O(1)` (excluding the output array)

---

### **10. Longest Increasing Subsequence (LIS)**

#### Problem:

Given an unsorted array of integers, find the length of the longest increasing subsequence.

#### Solution:

Use dynamic programming with a time complexity of `O(n²)` or use binary search for an optimized solution with `O(n log n)`.

```python
def length_of_lis(nums):
    if not nums:
        return 0
    
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)
```

**Time Complexity**: `O(n²)`
**Space Complexity**: `O(n)`

---

### **11. Find the "Kth" Largest Element**

#### Problem:

Given an unsorted array, find the `k`th largest element.

#### Solution:

Use the **Quickselect algorithm** or **heap** to efficiently find the `k`th largest element.

```python
import heapq

def find_kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]
```

**Time Complexity**: `O(n log k)`
**Space Complexity**: `O(k)`

---

### **12. Partition Equal Subset Sum**

#### Problem:

Given a set of positive integers, determine if the set can be partitioned into two subsets such that the sum of elements in both subsets is equal.

#### Solution:

This is a **subset sum problem**, which can be solved with dynamic programming.

```python
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
```

**Time Complexity**: `O(n * sum(nums))`
**Space Complexity**: `O(sum(nums))`

---

These problems will give you ample practice on **list manipulation** and **common algorithmic techniques**. Each of these is frequently asked in coding interviews, so mastering them will make you well-prepared for most scenarios!

Would you like more explanations or variations of these problems?
