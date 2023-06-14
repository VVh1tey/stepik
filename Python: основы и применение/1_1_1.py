def sum_v1() -> int:
    n,res = int(input()), 0
    while(n):
        res += int(input())
        n-=1
    print(res)
def sum_v2() -> int:
    print(sum([int(input()) for i in range(int(input()))]))
sum_v1()
#sum_v2()
