def twoSum(nums: list[int], target: int) -> list[int]:
    counter = 0
    n = len(nums)
    dict = {}

    for i in range(n):
        dict[nums[i]] = i
        counter += 1
    
    for i in range(n):
        if ((target - nums[i]) in dict.keys() and dict[target - nums[i]] != i):
            print(counter)
            return [i, dict[target - nums[i]]]
        counter += 1

print(twoSum([2,7,11,15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
    
