file_pantun = open("pantun.txt","r")
pantun = file_pantun.readlines()
for teks in pantun:
   print (teks)
file_pantun.close()

file_pantun = open("pantun.txt","r")
pantun = file_pantun.read()
for teks in pantun:
   print (teks)
file_pantun.close()  

judul = input("judul: ")
pengarang = input("pengarang: ")
thnterbit = input("thnterbit: ")

teks = "judul: {}\npengarang: {}\nthnterbit: {}".format(judul,pengarang,thnterbit)
file_bio = open("dataperpus.txt","w")
file_bio.write(teks)
file_bio.close()

judul = input("judul: ")
pengarang = input("pengarang: ")
thnterbit = input("thnterbit: ")

teks = "\njudul: {}\npengarang: {}\nthnterbit: {}\n---".format(judul,pengarang,thnterbit)
file_bio = open("dataperpus.txt","a")
file_bio.write(teks)
file_bio.close()