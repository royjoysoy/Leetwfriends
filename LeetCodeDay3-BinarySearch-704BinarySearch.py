def BS(nums, target):
    
    mid_num = len(nums) // 2

    if nums[mid_num] == target:
        print(mid_num)
        return mid_num
    
    while nums[mid_num] != target:
        mid_num = len(nums) // 2
        if nums[0] == target:
            print("0")
            return 0
        elif nums[mid_num] < target:
              nums = nums[mid_num:len(nums)-1]
        
        elif nums[mid_num] > target:
            nums = nums[0:mid_num]
   
        else:
            return -1

lst = [9,10,11,12,13,14,15,16,17,18,19,20]

# lst = [1,3,5,7,9,10]
target = 9
BS(lst, target)