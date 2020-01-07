test_set = int(input())+1

def include_text(str1_li, str2_li):
    # print(f'@@@@@@@@@@@@@@@@ str2_li={str2_li}')
    ans = 1
    if str2_li.count(str1_li[0]) > 0:
        start_index = str2_li.index(str1_li[0])
        end_index = len(str1_li) + start_index
        j = 0
        for i in range(start_index, end_index) :
            # print(f"aaa={i}")
            try : 
                if str2_li[i] != str1_li[j] :
                    # print(f"call back={i}")
                    str2_li.pop(start_index)
                    ans = include_text(str1_li, str2_li)
            except:
                ans = 0
            j+=1
    elif str2_li.count(str1_li[0]) == 0 :
        ans = 0
    return ans
for T in range(1,test_set):
    str1_li = list(input())
    str2_li = list(input())

    res = include_text(str1_li, str2_li)

    print('#{} {}'.format(T,res))
    # print()
