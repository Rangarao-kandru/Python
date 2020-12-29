8)Write a function called is_abecedarian that returns True if the letters in a word appear in alphabetical order (double letters are ok).
How many abecedarian words are there? (i.e) "Abhor" or "Aux" or "Aadil" should return "True" Banana should return "False"


def is_abecedarian():
    word=input("Enter a word:")
    word_sort=sorted(word)
    after_sort="".join(word_sort)
    if word==after_sort:
        return True
    else:
        return False


print(is_abecedarian())

def is_abecedarian():
    word=input("Enter a word:")
    flag=True
    for i in range(len(word)):
        for j in range(i+1,len(word)):
            if word[i]<=word[j]:
                continue
            else:
                flag=False
                break

    if flag:
        return True
    else:
        return False

print(is_abecedarian())

Output:

Enter a word:aadil
True
Enter a word:banana
False
