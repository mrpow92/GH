def rgb(r, g, b):
    return ccH(r)+ccH(g)+ccH(b)

def ccH(x):
    if x<0: return '00'
    elif x>=255: return 'FF'
    else:
        z = str(hex(x))[2:].upper()
        return z if len(z)>1 else "0"+z
import codewars_test as test


test.assert_equals(rgb(0,0,0),"000000", "testing zero values")
test.assert_equals(rgb(1,2,3),"010203", "testing near zero values")
test.assert_equals(rgb(255,255,255), "FFFFFF", "testing max values")
test.assert_equals(rgb(254,253,252), "FEFDFC", "testing near max values")
test.assert_equals(rgb(-20,275,125), "00FF7D", "testing out of range values")