from cryptography.fernet import Fernet
import os

# Genera una clave secreta
clave = Fernet.generate_key()
cipher = Fernet(clave)

# Solicitar el texto a cifrar
texto = input("\nTexto que desea cifrar : ")

# Crear directorio si no existe
if not os.path.exists("archivos"):
    os.makedirs("archivos")

# Cifrar el Texto
mensaje = texto.encode()
print("-----------------------------------")
print("Texto a Cifrar:", texto)
print("-----------------------------------")

mensaje_cifrado = cipher.encrypt(mensaje)
print("Texto Cifrado:", mensaje_cifrado)

# Guardar el mensaje cifrado en un archivo
with open("archivos/cifrado.txt", "wb") as file:
    file.write(mensaje_cifrado)

# Descifrar el Texto
mensaje_descifrado = cipher.decrypt(mensaje_cifrado).decode()
print("Texto Descifrado:", mensaje_descifrado)

# Guardar el Texto descifrado en un archivo
with open("archivos/descifrado.txt", "w") as file:
    file.write(mensaje_descifrado)