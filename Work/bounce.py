# bounce.py
#
# Exercise 1.5
count = 0
origin_hight = 100
while count<10:
    count += 1
    bound_hight = origin_hight * (3/5)
    origin_hight = bound_hight
    print(count,end=" ")
    print(bound_hight)
    print(round(bound_hight,3))
