class buku:
    nama = ''
    alamat = ''
    judul = ''

    def __init__(self, judul): #method constructor
        self.judul = judul

    def get_nama(self, nama):
        self.nama = nama

    def get_alamat(self, alamat):
        self.alamat = alamat

    def hasil(self):
        print('judul buku adalah %s\nnama peminjam %s\nalamat peminjam %s' % (self.judul, self.nama, self.alamat))


t =buku('Laskar Pelangi')
t.get_nama('Asril')
t.get_alamat('Jeneponto')
t.hasil()
print(' ')

t =buku('Mariposa')
t.get_nama('Habir')
t.get_alamat('Pabiringa')
t.hasil()