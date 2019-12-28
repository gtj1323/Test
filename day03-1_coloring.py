test_count = int(input())+1
for T in range(1, test_count):
    array = []
    for i in range(10):
        array.append(list([0,0] for i in range(10)))
    
    coloring_time = int(input())
    
    for i in range(coloring_time):
        [r1, c1, r2, c2, color] = list(map(int, input().split()))
        r2+=1
        c2+=1
        count=0
        for r in range(r1,r2):
            for c in range(c1,c2):
                if color==1:
                    array[r][c][0]=1
                elif color==2:
                    array[r][c][1]=1

    for r in range(10):
        for c in range(10):
            if array[r][c][0]+array[r][c][1]==2:
                count+=1
    print('#{} {}'.format(T,count))