import luas
import volume

def test_luas_prisma_segitiga():
    luas_prismasegitiga = luas.PrismaSegitiga()
    hasil = luas_prismasegitiga.hitung(6, 7, 5, 3, 4)
    print ("Luas Prisma Segitiga = ", hasil)
    
def test_volume_prisma_segitiga():
    volume_prismasegitiga = volume.VolumePrismaSegitiga()
    hasil = volume_prismasegitiga.hitung(6, 7)
    print("Volume Prisma Segitiga = ", hasil)

test_luas_prisma_segitiga()