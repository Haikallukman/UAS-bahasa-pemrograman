# Program Kalkulator sederhana
## Dokumentasi pembuatan program
https://youtube.com/shorts/1fwiqCNuDrY?si=8RGeCJ61y0AWC2VH

## Penjelasan program
### 1. Class Operations: Kelas ini menangani operasi matematika dasar seperti penjumlahan, pengurangan, perkalian, dan pembagian. Setiap operasi disediakan sebagai metode statis.
### 2. Class InputValidation: Kelas ini digunakan untuk memvalidasi input dari pengguna, memastikan bahwa input yang diberikan adalah angka. Jika bukan angka, input akan ditolak.
### 3. Class Calculator: Kelas ini menangani alur kalkulator, termasuk meminta input pengguna, memilih operasi yang diinginkan, dan menampilkan hasil operasi.
### 4. Fungsi Main: Fungsi utama yang menjalankan program kalkulator. Pengguna akan diminta untuk memasukkan dua angka dan memilih operasi. Setelah selesai, pengguna dapat memilih untuk melakukan perhitungan lagi atau keluar.
## Demo program kalkulator sederhana

```python
# Class untuk menangani operasi matematika dasar
class Operations:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b

# Class untuk memvalidasi input
class InputValidation:
    @staticmethod
    def validate_number(value):
        """Memeriksa apakah input adalah angka"""
        try:
            return float(value)
        except ValueError:
            return None

# Class untuk kalkulator yang menangani input dan operasi
class Calculator:
    def __init__(self):
        self.operations = Operations()
        self.validator = InputValidation()

    def get_input(self):
        """Meminta input pengguna dan memvalidasi"""
        while True:
            num1 = input("Masukkan angka pertama: ")
            num1 = self.validator.validate_number(num1)
            if num1 is not None:
                break
            else:
                print("Input tidak valid, masukkan angka yang benar.")
        
        while True:
            num2 = input("Masukkan angka kedua: ")
            num2 = self.validator.validate_number(num2)
            if num2 is not None:
                break
            else:
                print("Input tidak valid, masukkan angka yang benar.")
        
        return num1, num2

    def choose_operation(self):
        """Meminta pengguna untuk memilih operasi"""
        print("\nPilih operasi:")
        print("1. Penjumlahan (+)")
        print("2. Pengurangan (-)")
        print("3. Perkalian (*)")
        print("4. Pembagian (/)")
        
        while True:
            choice = input("Masukkan pilihan (1/2/3/4): ")
            if choice in ['1', '2', '3', '4']:
                return choice
            else:
                print("Pilihan tidak valid, coba lagi.")

    def perform_operation(self, choice, num1, num2):
        """Menjalankan operasi berdasarkan pilihan pengguna"""
        if choice == '1':
            result = self.operations.add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = self.operations.subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = self.operations.multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == '4':
            result = self.operations.divide(num1, num2)
            print(f"{num1} / {num2} = {result}")

# Fungsi utama untuk menjalankan kalkulator
def main():
    print("Selamat datang di Kalkulator Sederhana!")
    calculator = Calculator()
    
    while True:
        num1, num2 = calculator.get_input()
        choice = calculator.choose_operation()
        calculator.perform_operation(choice, num1, num2)
        
        # Menanyakan apakah ingin melanjutkan atau tidak
        continue_calculating = input("\nApakah Anda ingin melakukan perhitungan lain? (y/n): ").lower()
        if continue_calculating != 'y':
            print("Terima kasih telah menggunakan kalkulator!")
            break

# Menjalankan program
if __name__ == "__main__":
    main()
```
## Output Program
```
PS C:\Users\Haikal LNH\Desktop\New Delhi> & "C:/Users/Haikal LNH/AppData/Local/Programs/Python/Python313/python.exe" "e:/program kalkulator sederhana uas"
Selamat datang di Kalkulator Sederhana!
Masukkan angka pertama: 5 
Masukkan angka kedua: 5

Pilih operasi:
1. Penjumlahan (+)
2. Pengurangan (-)
3. Perkalian (*)
4. Pembagian (/)
Masukkan pilihan (1/2/3/4): 3
5.0 * 5.0 = 25.0

Apakah Anda ingin melakukan perhitungan lain? (y/n): n
Terima kasih telah menggunakan kalkulator!
PS C:\Users\Haikal LNH\Desktop\New Delhi> 
```
