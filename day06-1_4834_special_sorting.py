"""
3
10
1 2 3 4 5 6 7 8 9 10
10
67 39 16 49 60 28 8 85 89 11
20
3 69 21 46 43 60 62 97 64 30 17 88 18 98 71 75 59 36 9 26
"""
def get_list_txt(li):
    txt=""
    length = len(li)
    for i in range(length):
        txt += (" "+str(li[i]))
    return txt

def get_special(li):
    ans=[]
    for i in range(5):
        ans.append(li[i])
        ans.append(li[i*(-1)-1])
    return ans

Ts=int(input())+1

for T in range(1,Ts):
    num=int(input())
    li=list(map(int,input().split()))
    li.sort(reverse=True)
    ans=get_special(li)
    txt=get_list_txt(ans)
    print('#{}{}'.format(T,txt))
