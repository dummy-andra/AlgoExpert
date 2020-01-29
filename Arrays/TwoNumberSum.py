"""
Two Number Sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
If any two numbers in the input array sum up to the target sum, the function should return them in an array.
If no two numbers sum up to the target sum, the function should return an empty array.

Assume that there will be at most one pair of numbers summing up to the target sum.

Sample input: [3, 5, -4, 8, 11, 1, -1, 6], 10
Sample output: [-1, 11]
"""


# O(n^2) time | O(1) space
def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i+1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []


# O(n) time | O(n) space
def twoNumberSum2(array, targetSum):
    a = []
    for i in array:
        temp = targetSum - i
        if temp in a:
            return [temp, i]
        else:
            a.append(i)
    return []


# O(n log(n)) time | O(1) space
def twoNumberSum3(array, targetSum):
    array.sort()
    left = 0
    right = len(array)-1
    while right > left:
        currentSum = array[left] + array[right]
        if currentSum > targetSum:
            right -= 1
        elif currentSum < targetSum:
            left += 1
        else:
            return [array[left], array[right]]
    return []


arr = input("")
array = [int(i) for i in arr.split()]
target = int(input(""))
print(twoNumberSum3(array, target))
