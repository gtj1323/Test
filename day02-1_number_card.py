T=int(input())+1

for i in range(1, T):
    langth = int(input())
    cards_list = list(map(int,list(input())))
    cards_set = set(cards_list)
    
    count=0
    card_num=1
    for j in cards_set:
        temp_count = cards_list.count(j)

        if count < temp_count:
            count = temp_count
            card_num = j
        elif count == temp_count and card_num < j:
            card_num = j
    
    print('#{} {} {}'.format(i, card_num, count))