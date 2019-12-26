test_count = int(input())+1
for i in range(1, test_count):
    count = int(input())
    li = list(map(int,input().split()))
    degree = max(li)-min(li)
    st='#{} {}'.format(i,degree)
    print(st)