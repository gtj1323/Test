def binary_search(key, start, last, count):
    if start>last :
        return False
    else :
        count+=1
        middle = (start+last)//2
        # print(f'count={count}    {start}/{middle}/{last}')
        if key==middle :
            return count
        elif key<middle :
            # middle-=1
            return binary_search(key, start, middle, count)
        else :
            # middle+=1
            return binary_search(key, middle, last, count)

test_count=int(input())+1

for T in range(1, test_count):
    [last, page_A, page_B] = list(map(int,input().split()))
    start=1
    count_A = 0
    count_B = 0
    # print("A")
    A = binary_search(page_A, start, last, count_A)
    # print("B")
    B = binary_search(page_B, start, last, count_B)
    
    if A==False or B==False :
        if A==False and B==False :
            ch=0
        elif A==False and B!=False:
            ch='B'
        elif A!=False and B==False:
            ch='A'
    elif A>B :
        ch='B'
    elif A<B :
        ch='A'
    else :
        ch=0
    
    print('#{} {}'.format(T,ch))
    