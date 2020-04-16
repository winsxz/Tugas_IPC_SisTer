# import library socket karena menggunakan IPC socket
import socket

# definisikan IP untuk binding
ip = '10.20.32.13'

# definisikan port untuk binding
port= 12345

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
print('Connection address:', addr)


# buka file bernama "file_didownload.txt
# masih hard code, file harus ada dalam folder yang sama dengan script python
file = open('file_didownload.txt', 'rb')

try:
    # baca file tersebut sebesar buffer 
    byte = file.read(buffersize)
    
    # selama tidak END OF FILE; pada pyhton EOF adalah b''
    while byte != b'':
        # kirim hasil pembacaan file dari server ke client
        #print('SENDING')
        con.send(byte)
        # baca sisa file hingga EOF
        byte = file.read(buffersize)
        
finally:
    print ("end sending")
    
    # tutup file jika semua file telah  dibaca
    file.close()

# tutup socket
s.close()

# tutup koneksi
s.close()
