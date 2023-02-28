import qrcode as qr
import os

with open('tabak_km.txt', mode='r', encoding='UTF8') as f:
    src_km = f.readlines()
    tabak_km = [s.split('\t') for s in src_km]
    tabak_km = [km[2] for km in tabak_km if (km[1] == 'Нет' and not km[3] ) or (km[1] == 'Да')]

page_num = 1
for ind, km in enumerate(tabak_km):
    if not os.path.exists('QR/page'+str(page_num)):
        os.makedirs('QR/page'+str(page_num))
    print('Генерирую -->', ind, km)
    img = qr.make(km)
    img.save('QR/page'+str(page_num)+'/'+str(ind)+'.png')
    if not ((ind+1) % 234):
        page_num += 1
        #break
print('Всего страниц', page_num)