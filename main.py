hari_kerja = 19
hari_kerja_perbulan = 30
jam_lembur = 10
gaji_lembur_perjam = 150000
gaji = 4500000

totalGaji = (hari_kerja/hari_kerja_perbulan)*gaji
gajiLembur = jam_lembur*gaji_lembur_perjam

totalGaji+gajiLembur
totalGaji = "{:,.0f}".format(totalGaji+gajiLembur)

print("Rp", totalGaji)
