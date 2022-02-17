from django.test import TestCase


ans = input("input: ")

num = int(ans)


for i in range(1, num+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()









