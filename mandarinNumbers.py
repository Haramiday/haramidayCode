def to_mandarin(number):
    '''
    This function  ​takes in an​ ​integer less than or equal to 99​ ​as its parameter​
    and ​returns the mandarin version as a string 
    '''

    floor_division=number//10
    remainder = number %10
    word=[] #list for the word
    pinyin = {'Yi':1,'Er':2,'San':3,'Si':4,'Wu':5,'Liu':6,'Qi':7,'Ba':8,'Jiu':9,'Shi':10}
    
    if number > 99:
        return 'Number must be less than or equal to 99'

    else:
        for i in pinyin:
            if number <= 10 and number == pinyin[i]:
                return i
            else:
                if floor_division == pinyin[i]:
                    word.insert(0,i.capitalize())#the floor division is always at the beginning
                if pinyin[i] == remainder:
                    word.append(i.lower())
                if pinyin[i] == 10:
                    word.insert(1,i.lower())#10 is always at the middle
                    
        return ' '.join(word) #joins the elements in the list with a space
            

print(to_mandarin(40))
print(to_mandarin(44))
print(to_mandarin(99))
