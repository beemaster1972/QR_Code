
with open('egais_remains.txt', mode='r', encoding='UTF8') as f:
    src_km = f.readlines()
    src_km = [s.strip().split('\t') for s in src_km]
    egais = {km[1]:km[3] for km in src_km}
with open('egais_remians_final.txt', mode='w', encoding='UTF8') as f:
    for key, val in egais.items():
        f.write(f'{key}\t\t{val}\n')
        print(f'{key}\t\t{val}\n')
# print(egais)