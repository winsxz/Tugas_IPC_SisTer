# import library socket karena menggunakan IPC socket
import socket

# definisikan IP server tujuan file akan diupload
ip = '127.0.0.1'

# definisikan port number proses di server
port = 12345

# definisikan ukuran buffer untuk mengirim
buffersize = 1024

# buat socket (apakah bertipe UDP atau TCP?)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan koneksi ke server
s.connect((ip,port))

# buka file bernama "hasil_download.txt bertipe byte
# masih hard code, file harus ada dalam folder yang sama dengan script python
file = open('hasil_download.txt', 'wb')
data = s.recv(buffersize)
#print('SENDING')

# loop forever
while 1:
    # terima pesan dari client
    
    # tulis pesan yang diterima dari client ke file kita (result.txt)
    file.write(data)
    data = s.recv(buffersize)
    # berhenti jika sudah tidak ada pesan yang dikirim
    if not data: break
    
# tutup file_hasil_download.txt    
file.close()

#tutup socket
s.close()
print('File has been downloaded!')
