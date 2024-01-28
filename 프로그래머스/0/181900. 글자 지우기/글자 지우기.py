def solution(my_string, indices):
    arr_string=list(my_string)
    for idx in indices:
        arr_string[idx]=''
    return ''.join(arr_string)