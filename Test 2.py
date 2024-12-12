mrange = 5
bs_x = 1
bs_search_list =[]
x = 0


for i in range(mrange + 1):
    bs_search_list.append(i)
    i += 1
    bs_y = bs_search_list[x]
    print(bs_y)
    x += 1
print(bs_search_list)
bs_search_list.sort()
print(bs_search_list)