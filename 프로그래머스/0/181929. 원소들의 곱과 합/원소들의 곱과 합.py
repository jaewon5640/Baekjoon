from functools import reduce
def solution(num_list):
    square_sum,multi_sum=(0,1)
    for num in num_list:
        multi_sum *= num
        square_sum += num
    square_sum*=square_sum
    if multi_sum<square_sum:
        return 1
    else:
        return 0