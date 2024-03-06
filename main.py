hari_kerja = 19
hari_kerja_perbulan = 30
hari_lembur = 10
gaji_lembur = 150000
gaji = 4500000

totalGaji = (hari_kerja/hari_kerja_perbulan)*gaji
gajiLembur = hari_lembur+gaji_lembur

totalGaji+gajiLembur
totalGaji = "{:,.0f}".format(totalGaji+gajiLembur)

print("Rp", totalGaji)
