#this program tells if we take any input such as letter,digits,spaces,punctuation and all it will reverse
#the convert it inot string then reverse it and campare is it same if they are same means it is palindrome
def is_palindrome(s):
    cleaned=""
    for char in s:
        if char.isalnum():
            cleaned+=char.lower()
    return cleaned==cleaned[::-1]
s=str(input("enter the string: "))
print(is_palindrome(s))




