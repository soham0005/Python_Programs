# Question-> Sort The Given Array of 0,1,2 without using sort() and extra space
'''
Brute Force Approach:- sort the Array----> O(n logn) ----> O(1);

Another Brute Force:- Count the occurrence and fill the array with those:--->O(2N) --->O(N).

Optimum Solution:-- Using Dutch National Flag  O(n)---->O(1)

Use 3 pointers:-low,mid,high,
Initially set low,mid to 0 and high to size-1.
We assume that
     all elements to left of low are 0.
     all elements to high are 1
     everything between low and mid-1 is 1

Traverse Array, 
whenever mid points to 0,swap values of low and mid and increment low,mid
whenever mid points points to 2,swap with high and decrement high
for mid pointing to 1,just increment the mid
Loop until mid<=high


'''
def sortUsingDutch(nums):
    low = 0
    high = len(nums)-1
    mid = 0
    while (mid <= high):
        if (nums[mid] == 0):
            nums[low],nums[mid] = nums[mid],nums[low]
            low+=1
            mid+=1
        elif (nums[mid] == 1):
            mid += 1
        elif nums[mid] == 2:
            nums[mid],nums[high] = nums[high],nums[mid]
            high-=1
    return nums

ans = sortUsingDutch([2, 0, 2, 1, 1, 0])
print(ans)
