import os

s = ''

print('=== find word ===\n\n')

while (True):
    n = 0
    list = os.listdir()
    
    print('-------------------------------------')
    print("@ Write the string you are looking for")
    print("@ Or write Q to quit\n")
    s = input().lower()
    print('')
    
    if (s == 'q' or s=='Q'):
        break;
    
    elif (s.strip() == ''): 
        print('@ Please write a valid string!\n')
        pass
    else:
        for el in list:
            if (el != "@ find word.py"):
                if s in open(el).read().lower() or s in el.lower():
                    print(el)
                    n += 1
        print('\n@ The operation has been done successfully!')
        print('@ '+str(n)+' files contain the string.\n')
        
