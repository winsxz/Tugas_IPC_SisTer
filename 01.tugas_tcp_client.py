# import library socket karena akan menggunakan IPC socket
import socket

# definisikan tujuan IP server
ip = '127.0.0.1'

# definisikan port dari server yang akan terhubung
port = 12345

# definisikan ukuran buffer untuk mengirimkan pesan
buffersize = 1024

# definisikan pesan yang akan disampaikan
Pesan = 'TCP Woy'

# buat socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# lakukan koneksi ke server dengan parameter IP dan Port yang telah didefinisikan
s.connect((ip, port))

# kirim pesan ke server
s.send(Pesan.encode())

# terima pesan dari server
data = s.recv(buffersize)

# tampilkan pesan/reply dari server
print('Pesan:', data.decode())

# tutup koneksi
s.close()


