10.Two words are anagrams if you can rearrange the letters from one to spell the other. Write a function called is_anagram that takes two strings and returns True if they are anagrams.

def is_anagram(a,b):
    sort1=sorted(a)
    sort2=sorted(b)
    if sort1==sort2:
        return True
    else:
        return False

print(is_anagram("add","dad"))

Output:

True