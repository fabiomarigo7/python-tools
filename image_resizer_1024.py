import PIL
import os
from PIL import Image

def resizeImage(infile, output_dir=""):
    outfile = os.path.splitext(infile)[0]+"_resized"
    extension = os.path.splitext(infile)[1]

    if ((extension == ".jpg") or (extension == ".jpeg") or (extension == ".JPG") or (extension == ".JPEG")):

        if infile != outfile:
            try :
                im = Image.open(infile)
                im.thumbnail([1024,1024], Image.ANTIALIAS)
                im.save(output_dir+'//'+outfile+extension,"JPEG")
            except IOError:
                print("cannot reduce image for ", infile)

if __name__=="__main__":
    output_dir = "resized"
    dir = os.getcwd()

    if not os.path.exists(os.path.join(dir,output_dir)):
        os.mkdir(output_dir)

    for file in os.listdir(dir):
        resizeImage(file,output_dir)                
