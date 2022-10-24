def binary_search(arr,target_element):
    if len(arr) == 1 and arr[0] == target_element:
        return "Found at {0} index".format(arr[0])
    if len(arr) > 1 :
        mid_value = arr[len(arr)//2]
        left = [x for x in arr if x < mid_value]
        right = [x for x in arr if x > mid_value]
        if target_element == mid_value:
            return "Found at {0} index".format(arr.index(target_element))
        elif target_element < mid_value:
            return binary_search(left,target_element)
        else:
            return binary_search(right,target_element)
    else:
        return "Not Found"

print(binary_search([7,2,1,5,8,6],6))

