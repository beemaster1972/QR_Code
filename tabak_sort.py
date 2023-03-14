import qrcode as qr
import os
import re
from fpdf import FPDF
from barcode import EAN13
from barcode.writer import ImageWriter

with open('tabak_km.txt', mode='r', encoding='UTF8') as f:
    src_km = f.readlines()
    tabak_km = [s.strip().split('\t') for s in src_km]
    tabak_km = {km[2][1:14]:km[2] for km in tabak_km if km[1] == 'Нет'} # and not re.match(r'^029',km[2])]
pdf = FPDF(orientation='Landscape')
pdf.add_page()
#with open('tabak_sort.txt', mode='r', encoding='UTF8') as f:
x, y, row, page = 1, 1, 1, 1
w1, h1, w2, h2 = 10, 10, 20, 10
for key, val in tabak_km.items():
    # f.write(f'{key} \t {val}\n')
    # pdf.code39('*'+key+'*', x, y)
    if not os.path.exists('sort/'+key+'.png'):
        shtrih = EAN13(key, writer=ImageWriter())
        shtrih.save('sort/'+key)
    img = qr.make(val)
    pdf.image(img.get_image(), x, y, w=w1, h=h1, title=key)
    x += w1 + 10
    pdf.image('sort/'+key+'.png', x, y, w=w2, h=h2)
    x = x + w2 + 10 if x <= pdf.epw - (w1 + 10) else 0
    y = y + h1 + 10 if x == 0 else y
    row += 1 if x == 0 else 0
    #print(x, y, pdf.eph - (h1 + 1))
    if y > pdf.eph - h1:
        row = 1
        x, y = 0, 0
       # pdf.output('tabak-' + str(page) + '.pdf')
        pdf.add_page()
        page += 1

pdf.output('tabak_sort.pdf')



# page_num = 1
# for ind, km in enumerate(tabak_km):
#     if not os.path.exists('QR/page'+str(page_num)):
#         os.makedirs('QR/page'+str(page_num))
#     print('Генерирую -->', ind, km)
#     img = qr.make(km)
#     img.save('QR/page'+str(page_num)+'/'+str(page_num)+'-'+str(ind)+'.png')
# #<<<<<<< HEAD
#    # if not ((ind+1) % 234):
# #=======
#     if not ((ind+1) % 250):
# #>>>>>>> c026499600ab701072802cbf7d4306ef74587147
#         page_num += 1
#         #break
# print('Всего страниц', page_num)