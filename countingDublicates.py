import string
def duplicate_count(text):
    text=text.lower()
    allchars, dublicates = string.ascii_lowercase+string.digits, 0 
    for char in text:
        if char in allchars: 
            if text.count(char.lower()) > 1:
                dublicates += 1
                allchars = allchars.replace(char, "")
    return dublicates






import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(duplicate_count(""), 0)
        test.assert_equals(duplicate_count("abcde"), 0)
        test.assert_equals(duplicate_count("abcdeaa"), 1)
        test.assert_equals(duplicate_count("abcdeaB"), 2)
        test.assert_equals(duplicate_count("Indivisibilities"), 2)