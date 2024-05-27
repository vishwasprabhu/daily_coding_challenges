### 1. [Fixed Sliding window pattern](https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75)
```
def pattern1_maxsum(nums: List[int], k: int) -> int:
    left = 0
    currmax, ansmax = 0, -inf
    for right in range(len(nums)):
        currmax += nums[right] #Add to curr sum
        if (r-l+1==k): #Window condition met
            ansmax = max(ansmax, currmax) 
            currmax -= nums[left]
            left += 1 #Slide the window
    return ansmax
```

### 2. [Replace shinking/expanding window pattern](https://leetcode.com/problems/max-consecutive-ones-iii/?envType=study-plan-v2&envId=leetcode-75)
```
def pattern2_longest1s(nums: List[int], k: int) -> int:
    left, currzeros = 0, 0
    ansmax = 0
    for right in range(nums):
        if nums[right] == 0:
            currzeros += 1
        while(curzeros > k):
            if nums[left]==0:
                currzeros -= 1
            left += 1
        ansmax = max(ansmax, right-left+1)
    return ansmax
```
### 3. [Delete shirking/expanding window pattern](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=study-plan-v2&envId=leetcode-75)
```
def patter3_longest1s(nums: List[int], k: int) -> int:
    left, currzeros = 0, 0
    ansmax = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            currzeros += 1
        while currzeros > k:
            if nums[left] == 0:
                currzeros -= 1
            left += 1
        ansmax = max(ansmax, right-left+1-k) #deleting k zeros
    return ansmax
```
