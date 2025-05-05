from fpdf import FPDF
import os
import shutil

pdf = FPDF()
pdf.set_auto_page_break(0)

images = os.listdir("File Images")

for image in images:
	#with open("File Images/output_pdf/business_studies_project.pdf","wb") as f:
	pdf.add_page()
	pdf.image("File Images/"+image,w=200,h=200)

pdf.output('business_studies_project.pdf')