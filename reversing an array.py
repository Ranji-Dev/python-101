def reverse(nums):
    start_index = 0
    end_index = len(nums)-1

    while end_index>start_index:
        nums[start_index],nums[end_index] = nums[end_index], nums[start_index]
        start_index = start_index+1
        end_index = end_index-1

if __name__ == '__main__':
    n=[800,'dog', 23.56,3+2j]
    reverse(n)
    print(n)

