
movies = [
    "The Holy Grail", 1975, "Terry Jones & Terry Gillam", 91,
    ["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Fric Idle", "Terry Jones"]]

]


# 递归调用
def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)


print(print_lol(movies))