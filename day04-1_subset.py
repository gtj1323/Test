# 1~12까지 원소로 가지는 리스트 생성
full_set = list(range(1,13,1))
length = len(full_set)

total_count = int(input())+1

for T in range(1,total_count):
    [N, K] = list(map(int, input().split()))
    count=0
    
    for i in range(1<<length): # 부분집합 갯수.
        if N==list(bin(i)).count('1'): # 원소의 수가 N과 같으면.
            subset_sum = 0
            for j in range(length): # 원소의 수 만큼 비트 비교.
                if i & (1<<j):
                    subset_sum += full_set[j]
            if subset_sum==K:
                count+=1
    print('#{} {}'.format(T,count))