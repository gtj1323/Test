'''
3
3 10 5
1 3 5 7 9
3 10 5
1 3 7 8 9
5 20 5
4 7 9 14 17

T 노선수
K 이동할 수 있는 정류장 수, N 종점 번호, M 충전기가 설치된 정류장 수
충전기가 설치된 정류장 번호
'''
T = int(input())+1

for i in range(1,T):
    [K, N, M] = list(map(int,input().split()))
    charger_locations = list(map(int,input().split()))
    
    charge_station = 0
    count = 0
    while charge_station + K < N :
        set1 = set(range(charge_station,charge_station+K+1))
        set2 = set(charger_locations)
        temp_set_max = max(set1 & set2)
        if temp_set_max == charge_station:
            count=0
            break
        charge_station = temp_set_max
        count+=1
    print('#{} {}'.format(i, count))