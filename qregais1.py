import qrcode as qr
import os
import re

with open('egais.txt', mode='r', encoding='UTF8') as f:
    egais_km = f.readlines()
#      egais_km = [s.strip().split('\t') for s in src_km]
#
# egais_km = [km for km in egais_km if re.match(r'^\d{14}', km[0])]
# print(len(egais_km))
# for ind, km in enumerate(egais_km):
#     if len(km) == 2:
#         km.append(0)
# egais_km = [km for km in egais_km if km[2]]
# print(len(egais_km))
page_num = 1
for ind, km in enumerate(egais_km):
    if not os.path.exists('QR_egais/page'+str(page_num)):
        os.makedirs('QR_egais/page'+str(page_num))
    print('Генерирую -->',page_num, ind, km)
    img = qr.make(km)
    img.save('QR_egais/page'+str(page_num)+'/'+str(page_num)+'-'+str(ind)+'.png')
    #img.drawrect()
    if not ((ind+1) % 100):
        page_num += 1
        #break
print('Всего страниц', page_num)
