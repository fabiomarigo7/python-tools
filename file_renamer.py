import os 
from numpy import log10

def renameAllFiles():
    try:
        fileName = os.path.basename(__file__)
        lista_nomi = os.listdir()
        lista_nomi.remove(fileName)
        if lista_nomi:
            s = input('Write the prefix for all files: ')
            n_tot = len(lista_nomi)
            z = int(log10(n_tot))+1
            n=1
            for el in lista_nomi:
                ext = el.split('.')[-1].lower()
                m = str(n)
                os.rename(el, s+'_'+m.zfill(z)+'.'+ext)
                n += 1
            finish = input('The operation has been done successfully! Press enter to close.')
        else:
            input('Folder is empty!')
        
    except Exception as e: 
        input(e)    

if __name__=="__main__":
    print('=== file renamer ===\n\n')
    renameAllFiles()
