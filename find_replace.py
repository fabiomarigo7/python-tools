import os, re

def findReplace():
    s1 = ''
    s2 = ''
    while(True):
        list = os.listdir()
        print('-------------------------------------')
        print("@ Write the string you want to replace\n")
        s1 = input().lower()

        if (s1.strip() == ''): 
            print('@ Please choose valid string!\n')
            pass
        else:
            print("\n@ Write the new string you want to put\n")
            s2 = input().lower()
            for el in list:
                if (el != "find_replace.py"):
                    full_text = open(el).read()
                    new_text = re.sub(s1, s2, full_text)
                    open(el, 'w').write(new_text)
            print('\n@ The operation has been done successfully!\n')
       
if __name__=="__main__":
    print('=== find and replace ===\n\n')
    findReplace()
