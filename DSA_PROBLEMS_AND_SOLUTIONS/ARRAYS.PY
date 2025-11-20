# 1. TWO SUM
# 2. BEST TIME TO BUY AND SELL STOCK
# 3. FIND THE DUPLICATE NUMBERS
# 4. MERGE INTERVALS
# 5. SET MATRIX ZEROES
# 6. MAXIMUM SUBARRAY (KADANE'S  ALGORITHM)
# 7. PRODUCT OF ARRAY EXCEPT SELF
# 8. ROTATE IMAGES
# 9. SEARCH IN ROTATED SORTED ARRAY
# 10. FIND THE INTERSECTION OF TWO ARRAYS
# 11. 3 SUM
# 12. SUBARRAY SUM EQUALS K
# 13. MISSING NUMBER IN ARRAY
# 14. FLATTEN A MULTI-DIMENSIONAL ARRAY
# 15. FIND SINGLE VALUES IN THE ARRAY OR UNIQUE VALUES IN THE ARRAY
# 16. MOVES ZEROES TO END
                                          



# 1. 2 sum

# def two_sum(nums, target):
#     num_map = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in num_map:
#             return (num_map[complement], i)
#         num_map[num] = i
#     return None

# nums = [2, 7,2,7, 11, 15]
# target = 9
# print(two_sum(nums, target))


# def two_sum1(nums, target):
#     left, right = 0, len(nums) - 1
#     while left < right:
#         current_sum = nums[left] + nums[right]
#         if current_sum == target:
#             return (left, right)
#         elif current_sum < target:
#             left += 1
#         else:
#             right -= 1
    # return None

# print(two_sum1(sorted(nums), target))


# def sum(nums,target):
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if nums[i] + nums[j] == target:
#                 return (i,j)
# print(sum(nums,target))


# -------------------------------------------------------------------------------------------------------------------------------------------


# 2. BEST TIME TO BUY AND SELL STOCK


# def maxProfit(prices):
#     min_price = float('inf')
#     max_profit = 0

#     for price in prices:
#         if price < min_price:
#             min_price = price
#         else:
#             max_profit = max(max_profit, price - min_price)

#     return max_profit

# prices= [2,3,4,5,56,6,7,99]
# print(maxProfit(prices))



# -------------------------------------------------------------------------------------------------------------------

# 3. FIND THE DUPLICATE NUMBERS

# def duplicates(nums):
#     data = []
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] == nums[j]:
#                 data.append(nums[i])
#                 break   # avoid adding the same duplicate multiple times
#     return data

# nums = [1,2,34,4,4,6,3,5,3,2,4,2,34,4,3,2,2232,3,444,46]
# print(duplicates(nums))



# ----------------------------------------------------------------------------------------------------------------



# 4. MERGE INTERVALS


# def merge(intervals):   
#     merged = []
#     current_start, current_end = intervals[0]

#     for start, end in intervals[1:]:
#         if start <= current_end:          # overlap
#             current_end = max(current_end, end)
#         else:                              # no overlap -> push current and move on
#             merged.append([current_start, current_end])
#             current_start, current_end = start, end

#     # push the last interval
#     merged.append([current_start, current_end])
#     return merged


# intervals = [[1,3],[4,6],[2,5],[6,7],[13,12],[9,10]]
# print(merge(intervals))


# ---------------------------------------------------------------------------------------------------------------------

