from fpdf import FPDF
import os
pdf = FPDF()
# imagelist is the list with all image filenames


try:
    pageNum=1
    while (True):
        
        pdf.add_page()
        pdf.image(str(pageNum)+".png",0,0,210,297)
        os.remove(str(pageNum)+".png")
        pageNum+=1
        
except FileNotFoundError:
    pdf.output("yourfile.pdf", "F")
    
    
    