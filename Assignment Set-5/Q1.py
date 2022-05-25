# Assignment on function arguments (mutable & immutable) - Level 1- Q1

def find_pairs_of_numbers(num_list,n):
    #Remove pass and write your logic here
    count = 0
    for num1 in num_list:
        for num2 in num_list:
            if (num1 + num2) == n:                
                count = count + 1
    return int(count/2)

num_list=[1, 2, 4, 5, 6]
n=6
print(find_pairs_of_numbers(num_list,n))


