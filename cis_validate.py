from cCIS import CIS, PDF

cis = CIS('no_valid_cis.txt')
non_valid_cis = cis.get_cis()
cis.set_filename('tabak_km.txt')
cis.set_numcolumn(numcolumn=-1)
tabak_cis = cis.get_cis()
cis.set_numcolumn(2)
all_cis = cis.get_cis()

for ind, km in enumerate(non_valid_cis):
    cis_ind = all_cis.index(km)
    tabak_cis.pop(cis_ind)

pdf = PDF('tabak_km.pdf')
print(type(tabak_cis))
pdf.fill_pages(tabak_cis, 'Tabak ', column=2)
