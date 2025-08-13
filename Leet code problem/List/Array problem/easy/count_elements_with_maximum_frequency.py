#  Count Elements With Maximum Frequency
'''
You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.
'''
def  maxFrequencyElements(my_list):
    my_dict={}
    for num in my_list:
        my_dict[num]=my_dict.get(num, 0)+1
    max_freq= max(my_dict.values())
    
    total= sum(v for v in my_dict.values() if max_freq==v)

    return total




nums = [1,2,2,3,1,4]
print(maxFrequencyElements(nums))