def remove_subset(data,min_val,max_val):
    remaining_data =[]
    for val in data:
        for i in val:
            if i not in range(min_val,max_val+1):
                remaining_data.append(i)
    return remaining_data
                



data = [[2],[3],[1,3],[4,5,6]]
min_val = 2
max_val = 5
print("Remaining data are: ",remove_subset(data,min_val,max_val))
