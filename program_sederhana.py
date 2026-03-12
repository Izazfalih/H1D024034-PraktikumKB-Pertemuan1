import math
import datetime

data_luas = []

print("Program Menghitung Luas Lingkaran")

r = float(input("Masukkan jari-jari lingkaran: "))

luas = math.pi * r * r
data_luas.append(luas)

print("Luas lingkaran:", luas)

if luas > 100:
    print("Luas lingkaran besar")
else:
    print("Luas lingkaran kecil")

waktu = datetime.datetime.now()
print("Waktu perhitungan:", waktu)

print("Data luas yang pernah dihitung:", data_luas)