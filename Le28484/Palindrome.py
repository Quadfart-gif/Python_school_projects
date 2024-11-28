
def palindromeChecker(word:str):
    CurrentList = list(word)
    Current_list_clone = list(word)
    print(list(word))
    Current_list_clone.reverse()
    print("This is my reversed list", Current_list_clone)
    if CurrentList == Current_list_clone:
        print("word is a palindrome")
    else:
        print("it is not a palindrome")
palindromeChecker("abba")