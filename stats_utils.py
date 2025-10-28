def anakyzelist(nums):
    d = {}
    for i in nums:
        if i not in d:
            d[i] = 0
        d[i] += 1
    
    n = len(nums)

    mean = sum(nums) / n

    if n%2 == 0:
        median = nums[n//2]
    else:
        median = nums[n//2] + nums[n//2 + 1]
        median = median//2
    
    z = 0
    for i in nums:
        k = d[i]
        if k > z:
            z = k
            mode = i

    return [mean,median,mode]

