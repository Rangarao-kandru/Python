6)Modify your program to prompt the user to enter a string of forbidden letters and then print the number of words that don’t 
contain any of them. Can you find a combination of 5 forbidden letters that excludes the smallest number of words?

def avoids():
    string=input("Enter a string of forbidden letters: ")
    string1=string[:5]
    print(string1)
    line_list=open("words.txt")
    mylist=[]
    count=0
    flag = True
    for line in line_list:
        sentence=line.strip()
        list1=sentence.split(" ")
        for i in list1:
            if string1 in i:
                print(i)
        for i in list1:
            for j in i:
                if j not in string:
                    flag=True
                    continue
                else:
                    flag=False
                    break
            if flag==True:
                mylist.append(i)
                count+=1
    print(mylist)
    print(count)
avoids()
Output:
Enter a string of forbidden letters: situate
situa
situation,
['by', 'of', 'for', 'of', 'on', 'of', 'of', 'of', 'for', 'So,', 'of', 'of', 'of', '"O', 'of', 'I', 'If', 'do', 'I', 'of', 'of', '"O', 'of', 'no', 'from', 'I', 'from', 'worry', 'by', 'of', 'of', 'for', 'of', 'of', 'by', 'of', 'from', 'of', 'of', 'of', 'who', 'of', 'of', 'for', 'on', 'of', 'of', 'of', '"Now', 'for', 'of', 'go', 'And', 'All', 'on', 'from', 'of', 'of', 'for']
59

