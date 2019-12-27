total=int(input())+1

for T in range(1,total):
    [N, M] = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    
    count = N-M+1

    max = 0
    min = 10000*N
    for i in range(count):
        temp_sum=0
        for j in range(M):
            temp_sum += num_list[i+j]
        if max <= temp_sum :
            max = temp_sum
        if min >= temp_sum :
            min = temp_sum
    gap = max - min
    print('#{} {}'.format(T, gap))