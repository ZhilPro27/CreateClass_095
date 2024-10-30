class PersegiPanjang:
    def __init__(self, p, l) :
        self.p = p
        self.l = l
    
    def keliling(self):
        return 2*self.p + 2*self.l
    
    def luas(self):
        return self.p*self.l

    def __str__(self):
        return "Persegi Panjang, panjang " + str(self.p) + " cm, dan lebar " + str(self.l) + " cm"

def main():
    try:
        panjang = float(input("Masukkan Panjang: "))
        lebar = float(input("Masukkan Lebar: "))
        if panjang <= 0 or lebar <= 0:
            print("Nilai Harus Positif")
            return
        PP = PersegiPanjang(panjang, lebar)
        print(PP)
        print("Keliling: ", PP.keliling())
        print("Luas: ", PP.luas())
    except ValueError:
        print("Nilai Harus Sesuai")

main()
