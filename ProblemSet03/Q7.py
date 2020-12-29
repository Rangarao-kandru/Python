7)Write a function named using_only() that takes a word and a string of letters, and that returns True if the word contains only 
letters in the list. Can you make a sentence using only the letters acefhlo? Other than "Hoe alfalfa?"

def using_only(word,string):
    for word in string:
        if word in string:
            return True
        else:
            return False


word=input("Enter the word ")
string=input("Eneter the string ")
print(using_only(word,string))

