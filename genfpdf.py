from fpdf import FPDF
import qrcode

pdf = FPDF()
pdf.add_page()
pdf.interleaved2of5("1337", x=50, y=50, w=4, h=20)
pdf.output("interleaved2of5.pdf")
# pdf.close()

pdf = FPDF()
pdf.add_page()
pdf.code39("*fpdf2*", x=30, y=50, w=4, h=20)
pdf.output("code39.pdf")
# pdf.close()

pdf = FPDF()
pdf.add_page()
img = qrcode.make("https://docs-python.ru/packages/modul-fpdf2-python/")
pdf.image(img.get_image(), x=50, y=50)
pdf.output("qrcode.pdf")