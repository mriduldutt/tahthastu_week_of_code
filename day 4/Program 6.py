r1=int(input('Enter the words array size :-'))

wordsarr=[]

chararr=[]

print('Enter words seprated by enter key')

for i in range(r1):

    word=input('Enter word:-')

    wordsarr.append(word)

r2=int(input('Enter the char array size:-'))

print('Enter characters seprated by enter key')

for i in range(r1):

    char=input('Enter character:')

    chararr.append(char)

for i in wordsarr:

    flag=1

    for j in range(len(i)):

        if(i[j] not in chararr):

            flag=0

            break

    if(flag==1):

        print(i)
