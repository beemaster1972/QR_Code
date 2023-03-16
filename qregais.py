import qrcode as qr
# import os
# import re
from fpdf import FPDF
# from pdf417 import encode, render_image

with open('egais_km.txt', mode='r', encoding='utf-8-sig') as f:
    src_km = f.readlines()
    egais_km = [s.strip().split('\t') for s in src_km[1:]]

page_num = 1
pdf = FPDF(format='A4', unit='mm', orientation='Landscape')
pdf.set_font('helvetica', size=10.0)
pdf.add_page()
print(pdf.epw, pdf.eph)
x, y = 1, 1
width, height,count_of_codes = 20, 20, 0
for ind, km in enumerate(egais_km):
    # if not os.path.exists('QR/page'+str(page_num)):
    #     os.makedirs('QR/page'+str(page_num))
    print('Генерирую -->', ind, km[0])
    img = qr.make(km[0]) # render_image(encode(km[0]))
    pdf.image(img.get_image(), x, y, w=width, h=height)  # .get_image()
    count_of_codes += 1
    x = x + width+1 if x <= pdf.epw - width else 0
    y = y + height+1 if x == 0 else y
    if y > (pdf.eph+30 - height):
        x, y = pdf.epw/2, pdf.eph+30 -1
        print(x, y)
        pdf.text(x, y, 'EGAIS Page '+str(page_num)+' total codes on page ' + str(count_of_codes))
        page_num += 1
        pdf.add_page()
        x, y, count_of_codes = 1, 1, 0
pdf.text(pdf.epw/2, pdf.eph+30 - 1,'EGAIS Page '+str(page_num)+' total codes on page '+ str(count_of_codes))
pdf.output('egais_km.pdf')
# egais_km = [km for km in egais_km if re.match(r'^\d{14}', km[0])]
# print(len(egais_km))
# for ind, km in enumerate(egais_km):
#     if len(km) == 2:
#         km.append(0)
# egais_km = [km for km in egais_km if km[2]]
# print(len(egais_km))
# page_num = 1
# for ind, km in enumerate(egais_km):
#     if not os.path.exists('QR_egais/page'+str(page_num)):
#         os.makedirs('QR_egais/page'+str(page_num))
#     print('Генерирую -->',page_num, ind, km[0])
#     img = qr.make(km[0])
#     img.save('QR_egais/page'+str(page_num)+'/'+str(page_num)+'-'+str(ind)+'.png')
#     #img.drawrect()
#     if not ((ind+1) % 100):
#         page_num += 1
#         #break
# print('Всего страниц', page_num)
