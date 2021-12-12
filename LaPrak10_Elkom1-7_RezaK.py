list_nama, list_nilai = [], []

while True:
	print("""\nP R O G R A M  L I S T
 1. Input Data
 2. View Data
 3. Hitung Nilai Rata-Rata Praktikum Tiap Mahasiswa
 4. Hitung Nilai Rata-Rata Tiap Praktikum 
 5. Mencari Nilai Rata-Rata Praktikum Mahasiswa
 6. Update Nilai Praktikum Mahasiswa 
 7. Exit""")
 
	menu = int(input("Pilih menu yang tersedia: "))
	
	if menu == 1:
		print("\n[ 1. INPUT DATA ]")
		nama = str(input("Masukkan nama mahasiswa/i: "))
		nilai1 = int(input("Masukkan nilai praktikum 1: "))
		nilai2 = int(input("Masukkan nilai praktikum 2: "))
		nilai3 = int(input("Masukkan nilai praktikum 3: "))
		list_nama.append(nama)
		list_nilai.append([nilai1, nilai2, nilai3])
		
	elif menu == 2:
		print("\n[ 2. VIEW DATA ]")
		print(" NAMA | PRAK 1 | PRAK 2 | PRAK 3 ")
		print("---------------------------------")
		for nama in list_nama:
			nilai1 = list_nilai[list_nama.index(nama)][0]
			nilai2 = list_nilai[list_nama.index(nama)][1]
			nilai3 = list_nilai[list_nama.index(nama)][2]
			print(f"{nama}\t{nilai1}\t{nilai2}\t{nilai3}")
			
	elif menu == 3:
		print("\n[ 3. HITUNG RATA-RATA PRAK TIAP MAHASISWA/I]")
		for nama in list_nama:
			data_nilai = list_nilai[list_nama.index(nama)]
			rerata = sum(data_nilai) / len(data_nilai)
			print(f"{nama}\t = {rerata}")
			
	elif menu == 4:
		print("\n[ 4. HITUNG RATA-RATA TIAP PRAK")
		prak1, prak2, prak3 = [], [], []
		for nilai in list_nilai:
			prak1.append(nilai[0])
			prak2.append(nilai[1])
			prak3.append(nilai[2])
		rerata1 = sum(prak1) / len(prak1)
		rerata2 = sum(prak2) / len(prak2)
		rerata3 = sum(prak3) / len(prak3)
		print(f"Rerata Prak 1 = {rerata1}")
		print(f"Rerata Prak 2 = {rerata2}")
		print(f"Rerata Prak 3 = {rerata3}")
		
	elif menu == 5:
		print("\n[ 5. MENCARI NILAI RATA-RATA PRAK MAHASISWA/I")
		nama = input("Masukkan nama mahasiswa/i: ")
		nilai = list_nilai[list_nama.index(nama)]
		rerata = sum(nilai) / len(nilai)
		print(f"Rerata nilai praktikum {nama} = {rerata}")
		
	elif menu == 6:
		print("\n[ 6. UPDATE NILAI PRAK MAHASISWA/I")
		nama = input("Masukkan nama mahasiswa/i: ")
		nilai_ke = int(input("Ingin update nilai praktikum ke-: "))
		nilai_baru = int(input("Nilai baru: "))
		list_nilai[list_nama.index(nama)][nilai_ke - 1] = nilai_baru
		
	elif menu == 7:
		print("\n[ 7. EXIT ]")
		print ("T E R I M A  K A S I H ! !")
		break