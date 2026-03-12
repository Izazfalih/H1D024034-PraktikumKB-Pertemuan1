#Percabangan
beratBadan = int(input("Masukan berat anda: "))

if beratBadan > 80:
    print("Anda gendut")
elif 55 < beratBadan <= 80:
    print("Anda normal")
else:
    print("Anda kurus")

#Perulangan
for i in range(1, 15):
    print("Real Madrid Raja UCL")

#While
i = 1

while i <= 5:
    print("Perulangan ke-", i)
    i += 1

#Break
for i in range(1, 10):
    if i == 8:
        break
    print(i)

#continue
for i in range(1, 10):
    if i == 5:
        continue
    print(i)

def sapa():
    nama = input("Masukkan nama: ")
    print("Halo", nama)

sapa()