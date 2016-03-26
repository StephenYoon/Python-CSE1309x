def MY_2D_LIST(n):
    my_list = []
    for row in range(n):
        newrow = [1]
        for col in range(1, row+1):
            newcell = newrow[col-1] * float(row+1-col)/col
            newrow.append(int(newcell))
        my_list.append(newrow)
    return my_list

print(MY_2D_LIST(8))
