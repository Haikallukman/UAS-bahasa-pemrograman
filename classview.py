
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
