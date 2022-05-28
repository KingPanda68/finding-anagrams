# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(str1, str2):
    # [assignment] Add your code here
    if(sorted(str1) == sorted(str2)):
        print("True")
    else:
        print("False")


str1 = "deal"
str2 = "lead"

print("string value1:", str1)
print("string value2:", str2)
find_anagram(str1, str2)
# return True
