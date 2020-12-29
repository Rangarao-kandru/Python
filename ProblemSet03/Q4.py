4)Modify the above program to print only the words that have no “e” and compute the percentage of the words in the list have no “e.”

def  has_no_e(a):
    word=a.split(" ")
    li = []
    for a in word:
        if 'e' not  in word:
            li.append(word)
    percentage = 100*(len(li)/100)
    print(percentage)
a='Hello this is abi working on python programee'
res=has_no_e(a)
print(res)
