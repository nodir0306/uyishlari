def like(lst:list):
    if len(lst) == 0:
        return "no one like this"
    words =  ""
    for i in lst:
        words += i
        if i != lst[len(lst)-1]:
            words += " and "
    words += " like this "
    return words
lst = list(input().split())
print(like(lst))