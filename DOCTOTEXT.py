from docx import Document
filename=input("Enter doc file name")
document=Document(filename)
filename=filename.strip('.docx') #not able to remove .docx 
f=open(filename+".txt","+w")
for para in document.paragraphs:
    print(para.text)
    f.write(para.text)
    f.close()
print("DOC FILE successfully converted to TEXT FILE")
    
