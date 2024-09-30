from cryptography.fernet import Fernet

# Şifreleme fonksiyonu
def crypter(value):
    key = Fernet.generate_key()  # Anahtar oluştur
    cipher = Fernet(key)  # Anahtarı kullanarak şifreleme objesi oluştur

    encrypted_data = cipher.encrypt(value.encode())  # Veriyi şifrele

    # Şifrelenmiş veriyi ve anahtarı debug.txt dosyasına yaz
    with open("debug.txt", "wb") as file:
        file.write(key + b"\n" + encrypted_data)  # Anahtarı ve şifreli veriyi dosyaya yaz

# Şifre çözme fonksiyonu
def uncrypter():
    with open("debug.txt", "rb") as file:  # Dosyayı oku
        key = file.readline().strip()  # İlk satırda anahtarı al
        encrypted_data = file.read()  # Geri kalanında şifrelenmiş veriyi al

    cipher = Fernet(key)  # Anahtarla şifre çözme objesi oluştur
    decrypted_data = cipher.decrypt(encrypted_data).decode()  # Şifreyi çöz ve decode et

    return decrypted_data