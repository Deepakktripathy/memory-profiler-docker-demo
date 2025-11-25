from memory_profiler import profile

log_file = open('memory_profile.log', 'w')
@profile(stream=log_file)


def ex(listsize):
    mylist = ['hi'] * listsize
    mylist2 = ['hello'] * (listsize * 2)
    del mylist2
    return mylist


print(ex(10))
print(ex(100))
print(ex(1000))
