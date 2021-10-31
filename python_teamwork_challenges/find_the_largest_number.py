def largest_number(list) :
    max_number = list[0]
    for i in list :
        if max_number < i :
            max_number = i
    return max_number

array = [1,2,3,6,7,12]
print(f"In the given list the largest number is {largest_number(array)}")