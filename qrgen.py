import qrcode as qr
import os
import re

with open('tabak_km2.txt', mode='r', encoding='UTF8') as f:
    src_km = f.readlines()
    tabak_km = [s.strip().split('\t') for s in src_km]
    tabak_km = [km[2] for km in tabak_km if km[1] == 'Нет' and not re.match(r'^029',km[2])]

page_num = 1
for ind, km in enumerate(tabak_km):
    if not os.path.exists('QR/page'+str(page_num)):
        os.makedirs('QR/page'+str(page_num))
    print('Генерирую -->', ind, km)
    img = qr.make(km)
    img.save('QR/page'+str(page_num)+'/'+str(page_num)+'-'+str(ind)+'.png')
#<<<<<<< HEAD
   # if not ((ind+1) % 234):
#=======
    if not ((ind+1) % 250):
#>>>>>>> c026499600ab701072802cbf7d4306ef74587147
        page_num += 1
        #break
print('Всего страниц', page_num)