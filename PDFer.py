import os
from PIL import Image
from fpdf import FPDF
pdf = FPDF()
sdir = "C:\Users\AFK\PycharmProjects\downloader/"
w,h = 0,0

for i in range(1, 238):
    fname = sdir + "aima-3ed-solution-manual-%.d.jpg" % i
    print("Trying to open {} ... ".format(fname))
    if os.path.exists(fname):
        if i == 1:
            cover = Image.open(fname)
            w,h = cover.size
            print("W: {} H: {}".format(w,h))
            pdf = FPDF(unit = "pt", format = [w,h])
        image = fname
        print(image)
        pdf.add_page()
        pdf.image(image,0,0,w,h)
    else:
        print("File not found:", fname)
    print("processed %d" % i)
pdf.output("aima-3ed-solution-manual.pdf", "F")
print("done")