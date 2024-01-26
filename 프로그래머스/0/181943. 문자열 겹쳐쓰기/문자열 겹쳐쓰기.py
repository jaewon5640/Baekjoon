def solution(my_string, overwrite_string, s):
    list_my_string = list(my_string)
    list_my_string[s:s+len(overwrite_string)] = list(overwrite_string)
    return ''.join(list_my_string)