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
