import qrcode as qr
import os
import re

with open('egais_km.txt', mode='r', encoding='UTF8') as f:
    src_km = f.readlines()
    egais_km = [s.strip().split('\t') for s in src_km]

egais_km = [km[0] for km in egais_km if re.match(r'^\d{14}', km[0])]
print(len(egais_km))

page_num = 1
for ind, km in enumerate(egais_km):
    if not os.path.exists('QR_egais/page'+str(page_num)):
        os.makedirs('QR_egais/page'+str(page_num))
    print('Генерирую -->', ind, km)
    img = qr.make(km)
    img.save('QR_egais/page'+str(page_num)+'/'+str(ind)+'.png')
    if not ((ind+1) % 250):
        page_num += 1
        #break
print('Всего страниц', page_num)
