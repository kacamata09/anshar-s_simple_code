class ClassKu:
    def __enter__(self):
        print("Entering the class")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the class")

with ClassKu() as class_ku:
    print("Inside the class")
    
# Setelah blok with selesai, metode __exit__() akan dipanggil
