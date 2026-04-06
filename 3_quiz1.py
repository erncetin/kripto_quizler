# her kareye 1 bit koy
# ilk şekil 24 bit, ikinci 21 bit
from aes_deneme import encrypt, decrypt, Mode
a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1]



def mod_alma(algoritma_sonuc, sekil):
    counter = 0
    temp_list = []
    if sekil == 1:
        # range kısmını değiştir
        for i in range(28):
            counter = i % 24
            print(f"Temp_list = {temp_list}")
            print(f"i = {i}, counter = {counter}")
            if i < 24:
                temp_list.append(algoritma_sonuc[i])
            else:
                temp_list[counter] ^= algoritma_sonuc[i]
            
    
    elif sekil == 2:
        # range kısmını değiştir
        for i in range(26):
            counter = i % 21
            print(f"Temp_list = {temp_list}")
            print(f"i = {i}, counter = {counter}")
            if i < 24:
                temp_list.append(algoritma_sonuc[i])
            else:
                temp_list[counter] ^= algoritma_sonuc[i]

        pass


    return temp_list





mylist = mod_alma(a, 1)

print(mylist)




plain_text = b"plain text"
key = bytes.fromhex("2b7e151628aed2a6abf7158809cf4f3c")
iv = bytes.fromhex("00112233445566778899aabbccddeeff")

# Encoding
cipher_text = encrypt(plain_text, key, Mode.CTR, iv)

# Decoding
plain_text = decrypt(cipher_text, key, Mode.CTR, iv)

print(cipher_text)
print(plain_text)


print(plain_text.hex())