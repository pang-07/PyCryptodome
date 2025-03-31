import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from dotenv import load_dotenv

# โหลดค่าจากไฟล์ .env
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY").encode()[:32]  # ใช้แค่ 32 ไบต์
IV = os.getenv("IV").encode()[:16]  # ใช้แค่ 16 ไบต์

# ✅ ฟังก์ชันเข้ารหัส
def encrypt_image(input_image, output_file):
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, IV)

    with open(input_image, 'rb') as f:
        image_data = f.read()

    encrypted_data = cipher.encrypt(pad(image_data, AES.block_size))

    with open(output_file, 'wb') as f:
        f.write(encrypted_data)

    print(f"✅ ไฟล์ {input_image} ถูกเข้ารหัสเป็น {output_file}")

# 🔓 ฟังก์ชันถอดรหัส
def decrypt_image(input_file, output_image):
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, IV)

    with open(input_file, 'rb') as f:
        encrypted_data = f.read()

    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    with open(output_image, 'wb') as f:
        f.write(decrypted_data)

    print(f"✅ ไฟล์ {input_file} ถูกถอดรหัสเป็น {output_image}")

# 🔥 โปรแกรมหลัก
if __name__ == "__main__":
    print("\n🔹 เลือกโหมดที่ต้องการ:")
    print("1. เข้ารหัสรูปภาพ (Encrypt)")
    print("2. ถอดรหัสรูปภาพ (Decrypt)")

    choice = input("🔸 กรุณาเลือก (1 หรือ 2): ").strip()

    if choice == "1":
        input_image = input("🔹 กรุณาใส่ชื่อไฟล์รูปภาพ: ").strip()
        output_file = input_image + ".bin"
        encrypt_image(input_image, output_file)
    elif choice == "2":
        input_file = input("🔹 กรุณาใส่ชื่อไฟล์ที่เข้ารหัส: ").strip()
        output_file = input_file.replace(".bin", "")
        decrypt_image(input_file, output_file)
    else:
        print("❌ ตัวเลือกไม่ถูกต้อง")
