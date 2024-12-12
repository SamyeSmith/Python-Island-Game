mrange = 5
bs_x = 1
bs_search_list =[]
x = 0

get_t_y = 3


# for i in range(mrange + 1):
#     bs_search_list.append(i)
#     i += 1
#     bs_y = bs_search_list[x]
#     print(bs_y)
#     x += 1
# print(bs_search_list)
# bs_search_list.sort()
# print(bs_search_list)
for i in range(mrange):
                        bs_search_list.append(i) # making the list that will be used for BS search
                        i += 1
                        low = 0
                        high = len(bs_search_list)
                        v = 0
                        # bs_y = bs_search_list[x]
                        # print(bs_y)
                        # x += 1

                        # if v == 0:
while high >= low:

                    mid = (high + low) // 2

                    if bs_search_list[mid] == get_t_y:
                        print (f"Treasure is on y: {get_t_y}")
                        break

                    elif bs_search_list[mid] > get_t_y:
                        high = mid - 1

                    else:
                        low = mid + 1

                    # if bs_x == power.get_p_x() and target == power.get_p_y():
                    #     print (f"Power found at {bs_x}, {i}.")
                    #     v =+ 1
                    
                    # elif bs_x == trap.get_tr_x() and target == trap.get_tr_y():
                    #     print (f"Trap found at {bs_x}, {i}.")
                    #     v =+ 1
                    

                    # else:
                    #     i += 1