# import library socket karena menggunakan IPC socket
import socket

# definisikan IP untuk binding
ip = '10.20.32.13'

# definisikan port untuk binding
port = 12345

# definisikan ukuran buffer untuk menerima pesan
buffersize = 1024

# buat socket (bertipe UDP atau TCP?)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan binding ke IP dan port
s.bind((ip, port))

# lakukan listen
s.listen(5)

#  siap menerima koneksi
con, addr = s.accept()
print ('Connection address:', addr)

# buka/buat file bernama hasil_upload.txt untuk menyimpan hasil dari file yang dikirim server
# masih hardcoded nama file, bertipe byte
file = open('hasil_upload.txt', 'wb')


# loop forever
while 1:
    # terima pesan dari client
    data = con.recv(1024)
    
    # tulis pesan yang diterima dari client ke file kita (result.txt)
    file.write(data)
    
    # berhenti jika sudah tidak ada pesan yang dikirim
    if not data: break
    
# tutup file result.txt    
file.close()

#tutup socket
s.close()

# tutup koneksi
s.close()
