lst = [
  {"a": 1, "b": 3},
  {"a": 3, "b": 2},
  {"a": 2, "b": 40},
  {"a": 4, "b": 12}
]

sort_by = "b"

def sort_list(sort_by, lst):
    temp = {}
    for j in range(len(lst)):
        print(lst[len(lst)-1])
        print(lst[j])
        if lst[len(lst)-1][sort_by] > lst[j][sort_by]:
            temp = lst[j][sort_by]
            lst[j][sort_by] = lst[len(lst)-1][sort_by]
            lst[len(lst)-1][sort_by] = temp
    return lst
print(sort_list(sort_by, lst))