# 1. Target Problem

# def find_target_pairs(nums, target):
#     pairs = []
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i] + nums[j] == target:
#                 pairs.append((nums[i], nums[j]))
#     return pairs


# nums = [2, 7, 11, 15, 5, 3]
# target = 10
# result = find_target_pairs(nums, target)

# if result:
#     print("Pairs found:", result)
# else:
#     print("No pairs found")
    


# nums = [2, 7, 11, 15, 5, 3]
# target = 10

# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] + nums[j] == target:
#             print(nums[i],nums[j])


# --------------------------------------------------------------

# 2. Missing numbers in the list

# def missing(arr, n):
#     total = n*(n+1)//2
#     su = 0
#     for i in arr:
#         su += i
#     return total-su
# arr = [1,2,3,5,6]
# n = 6
# print(missing(arr,n))


# num = [1, 2, 4, 5, 6] 
# n = 6 
# total = n*(n+1)//2 
# su = 0 
# for i in num:
#     su += i 
#     total = total - su
#     print(total)

# --------------------------------------------------------------

# 3. Maximum subarray (kadane's Algorithms)

# def max_subarray_sum(arr):
#     max_sum = arr[0]
#     current_sum = arr[0]
#     for i in range(1,len(arr)):
#         current_sum = max(arr[i], current_sum + arr[i])
#         max_sum = max(max_sum, current_sum)
#     return max_sum
# arr= [-2,-3,4,-1,-2,1,5,-3]
# print(max_subarray_sum(arr))



# arr= [-2,-3,4,-1,-2,1,5,-3]
# max_sum = arr[0]
# current_sum = arr[0]
# for i in range(1, len(arr)):
#     current_sum = max(arr[i], current_sum + arr[i])
#     max_sum = max(max_sum, current_sum)
# print(max_sum)

# -------------------------------------------------------------

# 4. Move all zeroes to the end

# def moves_zero(arr):
#     position = 0
#     for i in range(len(arr)):
#         if arr[i] != 0:
#             arr[position], arr[i]= arr[i], arr[position]
#             position += 1
#     return arr
# arr= [1,0,2,0,3,0,12,0,5]
# print(moves_zero(arr))



# arr= [1,0,2,0,3,0,12,0,5]
# position = 0
# for i in range(len(arr)):
#     if arr[i] != 0:
#         arr[position], arr[i] = arr[i], arr[position]
#         position += 1
# print(arr)


# ---------------------------------------------------------

# 5. Count Frequency

# def count_frequency(arr):
#     freq = {}
#     for i in arr:
#         if i in freq:
#             freq[i] +=1
#         else:
#             freq[i] =1
#     return freq
    
# arr = [1,2,2,3,1,3,2,4,5,6,4,2,3,44,5,2,2]
# print(count_frequency(arr))



# arr = [1,2,2,3,1,3,2,4,5,6,4,2,3,44,5,2,2] 
# freq = {}
# for i in arr:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] =1
# print(freq)


# ----------------------------------------------------------

# 6. Longest Consecutive sequence data in the list

# def longest_consecutive(nums):
#     nums_set = set(nums)
#     longest = 0

#     for num in nums_set:
#         if num - 1 not in nums_set:  # start of sequence
#             length = 1
#             while num + length in nums_set:
#                 length += 1
#             longest = max(longest, length)

#     return longest

# # Example usage
# arr = [100, 4, 200, 1, 3, 2]
# print("Longest consecutive sequence length:", longest_consecutive(arr))

# -----------------------------------------------------------------------------------------

# 7. Non repeating data in the list

# arr = [9, 4, 9, 6, 7, 4]
# a = []
# d ={}

# for i in arr:
#     if i not in d:
#         d[i] =1
#     else:
#         d[i] += 1
# print(d)
# for i in arr:
#     if d[i] == 1:
#         a.append(i)
# print(a)

# --------------------------------------------------------------------------------------

# 8. Flatten list (multiple list into single list)

# nested_list = [[1, 2, 3], [4, 5, [6, 7, 8]], [9, 10, [11, 12, 13, [14, 15, 16]]], [17]]
# data = []

# def flatten(lst):
#     for item in lst:
#         if isinstance(item,list):
#             flatten(item)
#         else:
#             data.append(item)

# flatten(nested)
# print(data)

# --------------------------------------------------------------------------------------

# 9. Second largest number in the list

# arr = [10, 20, 5, 8, 30,30,21]

# max1 = arr[0]
# max2 = arr[0]
# for i in range(len(arr)):
#     if arr[i] > max1:
#         max2 = max1
#         max1 = arr[i]
#     elif arr[i] > max2 and arr[i] != max1:
#         max2 = arr[i]
# print(max2)

# ------------------------------------------------------------------------------------------

# 10. Repeated characters in the list

# arr = [4, 3, 2, 7, 8, 2, 3, 1]

# d= {}
# for i in arr:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# print(d)

# for key, value in d.items():
#     if value > 1:
#         print(key)

# -----------------------------------------------------------------------------------------

# 11.Permutations code in list

# num = [1,2,3]
# d = []
# for i in range(len(num)):
#     for j in range(len(num)):
#         for k in range(len(num)):
#             if i != j and j != k and i != k:
#                 d.append([num[i],num[j],num[k]])
# for p in d:
#     print(p)
    
# ----------------------------------------------------------------------------------
# 
# 12. Combinations code in list    
    
# num = [1,2,3,4]

# n = len(num)
# for i in range(n):
#     for j in range(i+1, n):
#         for k in range(j+1, n):
#             print([num[i],num[j], num[k]])

# -------------------------------------------------------------------------------------

# 13. Bubble sorting without buildin methods

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):  # Last i elements are already sorted
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
#     return arr
    
    

# arr = [64, 34, 25, 12, 22, 11, 90]
 
# print(bubble_sort(arr))


# arr = [64, 34, 25, 12, 22, 11, 90]
# n = len(arr)

# for i in range(n):
#     for j in range( n - i - 1):
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]

# print(arr)

# -----------------------------------------------------------------------------------


# 1. Permutations code in string

# s = "abc"
# permutations = []

# for i in range(len(s)):
#     for j in range(len(s)):
#         for k in range(len(s)):
#             if i != j and j != k and i != k:
                
#                 permutations += [s[i] + s[j] + s[k]]

# print("Permutations of 'abc':")
# for p in permutations:
#     print(p)
    
# ----------------------------------------------------------------------------------

# 2. Combinations code in string

# s= "abc"
# n = len(s)
# for i in range(n):
#     for j in range(i + 1, n):
#         print(s[i] + s[j])


# ---------------------------------------------------------------------------------------

# 3. Valid Parenthesis code in string

# def is_valid_parentheses(s):
#     stack = []
#     mapping = {')': '(', '}': '{', ']': '['}

#     for char in s:
#         if char in mapping.values():  # opening bracket
#             stack.append(char)
#         elif char in mapping:  # closing bracket
#             if not stack or stack[-1] != mapping[char]:
#                 return False
#             stack.pop()
#         else:
#             return False  # invalid character
#     return not stack

# # Example usage:
# print(is_valid_parentheses("()[]{}"))  # True
# print(is_valid_parentheses("(]"))      # False


# s = "()[]{}"
# stack = []
# mapping = {')': '(', '}': '{', ']': '['}

# valid = True
# for char in s:
#     if char in mapping.values():
#         stack.append(char)
#     elif char in mapping:
#         if not stack or stack[-1] != mapping[char]:
#             valid = False
#             break
#         stack.pop()
#     else:
#         valid = False
#         break

# print(valid)  # True

# -------------------------------------------------------------------------------

# 4. Anagram code in string

# s1 = "lisaen"
# s2 = "silent"

# if len(s1) != len(s2):
#     print("Not equal len of string ")
# else:
#     freq1 = {}
#     for ch in s1:
#         if ch in freq1:
#             freq1[ch] += 1
#         else:
#             freq1[ch] =1
#     freq2 = {}        
#     for ch in s2:
#         if ch in freq2:
#             freq2[ch] += 1
#         else:
#             freq2[ch] = 1
#     if freq1 == freq2:
#         print('anagram')
#     else:
#         print('not anagram')


# ----------------------------------------------------------------------------------

# 5. Separate the nums and alpha characters and also sum of all nums in the string

# s= "abc123xyz45"
# nums= ""
# alp= ""
# total = 0
# for i in s:
#     if i.isdigit():
#         nums +=i
#         total += int(i)
        
#     else:
#         alp += i
# print(nums)
# print(alp)
# print(total)