import os
import img2pdf


def imgs_to_pdf():
    # print(os.listdir("Images"))  # print img names from Images dir
    imgs_list = sorted(os.listdir("Images"))
    
    # creating PDF file        
    with open("File with images.pdf", "wb") as f:
        f.write(img2pdf.convert(imgs_list))
    
    
if __name__ == '__main__':
    imgs_to_pdf()
    
