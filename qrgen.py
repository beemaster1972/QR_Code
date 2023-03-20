import qrcode as qr
import os
import re
from fpdf import FPDF
from cCIS import CIS, PDF

cis = CIS('tabak_km.txt', numcolumn=-1)
tabak_cis = cis.get_cis()
cis_tabak = [km[2]+'\n' if km[1] == 'Нет' else km[2][2:]+'\n' for km in tabak_cis]
with open('cis_valid.txt', mode='w', encoding='utf-8-sig') as f:
    f.writelines(cis_tabak)

# with open('tabak_km.txt', mode='r', encoding='utf-8-sig') as f:
#     src_km = f.readlines()
#     tabak_km = [s.strip().split('\t') for s in src_km]
#     tabak_km = [km[2] for km in tabak_km[1:]] # if km[1] == 'Нет'] # and not re.match(r'^029',km[2])]
#
# page_num = 1
# pdf = FPDF(format='A4', unit='mm', orientation='Landscape')
# pdf.set_font('helvetica', size=10.0)
# pdf.add_page()
# print(pdf.epw, pdf.eph)
# x, y = 1, 1
# width, height,count_of_codes = 12, 12, 0
# for ind, km in enumerate(tabak_km):
#     # if not os.path.exists('QR/page'+str(page_num)):
#     #     os.makedirs('QR/page'+str(page_num))
#     #print('Генерирую -->', ind, km)
#     img = qr.make(km)
#     pdf.image(img.get_image(), x, y, w=width, h=height)
#     count_of_codes += 1
#     x = x + width+1 if x <= pdf.epw - width else 0
#     y = y + height+1 if x == 0 else y
#     if y > (pdf.eph+30 - height):
#         x, y = pdf.epw/2, pdf.eph+30 -1
#         print(x, y)
#         pdf.text(x, y, 'Page '+str(page_num)+' total codes on page ' + str(count_of_codes))
#         page_num += 1
#         pdf.add_page()
#         x, y, count_of_codes = 1, 1, 0
# pdf.text(pdf.epw/2, pdf.eph+30 - 1,'Page '+str(page_num)+' total codes on page '+ str(count_of_codes))
# pdf.output('tabak_km.pdf')
    #img.save('QR/page'+str(page_num)+'/'+str(page_num)+'-'+str(ind)+'.png')
#<<<<<<< HEAD
   # if not ((ind+1) % 234):
#=======
#     if not ((ind+1) % 250):
# #>>>>>>> c026499600ab701072802cbf7d4306ef74587147
#         page_num += 1
#         #break
# print('Всего страниц', page_num)