# Complete the function/method (depending on the language) to return true/True 
# when its argument is an array that has the same nesting structures 
# and same corresponding length of nested arrays as the first array.

def same_structure_as(original,other):
    print("test")




from solution import same_structure_as
import codewars_test as test

test.assert_equals(same_structure_as([1,[1,1]],[2,[2,2]]), True, "[1,[1,1]] same as [2,[2,2]]")
test.assert_equals(same_structure_as([1,[1,1]],[[2,2],2]), False, "[1,[1,1]] not same as [[2,2],2]")