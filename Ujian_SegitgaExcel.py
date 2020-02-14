
def segitiga(x):
    a = ''
    b = 0
    kata = x.replace(' ', '')
    pola = list(map(lambda row: row * (row + 1)/2, range(len(kata))))
    pola = list(map(int, pola))
    if len(kata) not in pola:
        print('Karakter tidak memenuhi syarat pola')
    else:
        for i in range(pola.index(len(kata))):
            for j in range(pola[i], pola[i + 1]):
                a += f"{kata[j]} "
                b += 1
            a += '\n'
        print(a)
print(segitiga('Purwadhika'))

import xlsxwriter
book = xlsxwriter.Workbook('Ujian_SegitigaExcel.xlsx')
sheet = book.add_worksheet('sheet1')
d = 0
for k in x:
    sheet.write(d, 0, a)
    row += 1
book.close()