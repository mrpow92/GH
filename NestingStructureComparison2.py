# Complete the function/method (depending on the language) to return true/True 
# when its argument is an array that has the same nesting structures 
# and same corresponding length of nested arrays as the first array.

def same_structure_as(original,other):
    if isinstance(original, list) and isinstance(other, list):
        #WENN ES 2 LISTEN SIND
        return check_inner_list(original, other)

    elif not isinstance(original, list) and not isinstance(other, list):
        #WENN BEIDES KEINE LISTEN SIND
        return True 

    elif (not isinstance(original, list) and isinstance(other, list)) or (isinstance(original, list) and not isinstance(other, list)):
        ###Wenn eins eine List und das andere nicht 
        return False
    else: 
        return True 




def check_inner_list(original, list_other):
    print(type(original), type(list_other))
    print(len(original), len(list_other))
    if isinstance(original, list) and isinstance(list_other, list):
        
        if len(original) == len(list_other):
            if len(original)==1 and not isinstance(original,list) and isinstance(list_other, list): 
                return True
            zipped = zip(original,list_other)
        else: 
            return False 
        for element, element_other in zipped:
            if isinstance(element, list) and isinstance(element_other, list):
                if not check_inner_list(element, element_other):
                    return False
            elif (isinstance(element, list) and not isinstance(element_other, list)) or (not isinstance(element, list) and isinstance(element_other, list)):
                return False
            elif not isinstance(element, list) and not isinstance(element_other, list):
                print("beides keine Listen")
            else:
                return False 
        return True
    elif type(original) == type(list_other):
        return True
    else:
        return False


#from solution import same_structure_as
import codewars_test as test

test.assert_equals(same_structure_as([[[],[]]],[[1,1]]), False, "[[[],[]]] not  same as [2,[2,2]]")
# test.assert_equals(same_structure_as([1,[1,1]],[[2,2],2]), False, "[1,[1,1]] not same as [[2,2],2]")
# test.assert_equals(same_structure_as([[[],[]]],[[[],[]]]), True , "[[[],[]]]  same as [[[],[]]]")
#test.assert_equals(same_structure_as( [-11, -2, 18, 17, -2, [[11, [-6, 6]], [-18, 5], -6, 20], [[13, 13], 14, -3, -12], 8, -3, -15, 13, 3] ,  [-6, 15, 19, [8, -17, 1, [[-9, 15], 2, -13, -9]], [18, [-16, 12]], -4, 7, -15, 6, -8, -16, [-13, 19, -3, 10]]), False , "[[[],[]]]  same as [[[],[]]]")