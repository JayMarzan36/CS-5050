


# Not complete still needs work

input_1 = [1,4,5,8]

input_2 = [2,4,6,7]



def merge_sort(input_1, input_2):
    result = []
    
    done = False
    
    index = 0
    
    while(not done):
        
        if len(result) == (len(input_1) + len(input_2)):
            break
        
        
        if index <= 0:
            continue
        else:
            if input_1[index] > input_2[index - 1]:
                result.append(input_2[index - 1])
        
        
        if input_1[index] < input_2[index]:
            result.append(input_1[index])
        
        index += 1
    
    
    return result

print(merge_sort(input_1, input_2))