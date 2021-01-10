import luas

def test_luas_prisma_segitiga():
    luas_prismasegitiga = luas.PrismaSegitiga()
    hasil = luas_prismasegitiga.hitung(6, 7, 5, 3, 4)
    print ("Luas Prisma Segitiga = ", hasil)

test_luas_prisma_segitiga()