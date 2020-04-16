# import library socket karena akan menggunakan IPC socket
import socket

# definisikan alamat IP binding  yang akan digunakan 
ip = '127.0.0.1'

# definisikan port number binding  yang akan digunakan 
port = 12345

# definisikan ukuran buffer untuk mengirimkan pesan
buffersize = 1024

# buat socket bertipe TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan bind
s.bind((ip, port))

# server akan listen menunggu hingga ada koneksi dari client
s.listen(5)
print('test')

# lakukan loop forever
while 1:
	# menerima koneksi
	con, addr = s.accept()    	
	
	# menampilkan koneksi berupa IP dan port client yang terhubung menggunakan print
	print('Koneksi dari:', addr)

	# menerima data berdasarkan ukuran buffer
	data = con.recv(buffersize)
    
	# menampilkan pesan yang diterima oleh server menggunakan print
	print('Pesan:', data.decode())
	
	# mengirim kembali data yang diterima dari client kepada client
	forward = data
	con.send(forward)

# tutup koneksi	
s.close()
