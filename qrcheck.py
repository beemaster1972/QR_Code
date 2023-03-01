import qrcode as qr
import os
spr_km = dict()
with open('tabak_km.txt', mode='r', encoding='UTF8') as f:
    src_km = f.readlines()
# <<<<<<< HEAD
    tabak_km = [s.strip().split('\t') for s in src_km[1:]]
    # tabak_km = [km[2] for km in tabak_km if (km[1] == 'Нет' and not km[3] ) or (km[1] == 'Да')]
    keys = [x[3] if len(x) == 4 else 'NonAgregat' for x in tabak_km]

    spr_km = dict.fromkeys(keys,[])
    for ind, km in enumerate(tabak_km):
        km_agregat = km[3] if len(km) == 4 else 'NonAgregat'
        spr_km[km_agregat].append(km[2])
    kol_km = [len(km) for km in spr_km.values()]
# =======
    tabak_km = [s.split('\t') for s in src_km]
    # tabak_km = [km[2] for km in tabak_km if (km[1] == 'Нет' and not km[3] ) or (km[1] == 'Да')]
    spr_km = {km[3]:[].append(km[2]) for km in tabak_km}
# >>>>>>> c026499600ab701072802cbf7d4306ef74587147
    print(len(spr_km))
# page_num = 1
# for ind, km in enumerate(tabak_km):
#     if not os.path.exists('QR/page'+str(page_num)):
#         os.makedirs('QR/page'+str(page_num))
#     print('Генерирую -->', ind, km)
#     img = qr.make(km)
#     img.save('QR/page'+str(page_num)+'/'+str(ind)+'.png')
#     if not ((ind+1) % 234):
#         page_num += 1
#         #break
# print('Всего страниц', page_num)