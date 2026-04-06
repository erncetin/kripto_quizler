# her kareye 1 bit koy
# ilk şekil 24 bit, ikinci 21 bit
from aes_deneme import encrypt, decrypt, Mode
import matplotlib.pyplot as plt
import numpy as np

# https://github.com/rafael2903/AES-128-cipher
# İLK İNPUT AESLENECEK VERİ, İKİNCİ İNPUY ŞEKİL. 1 VE 2 OLACAK ŞEKİLDE
def mod_alma(algoritma_sonuc, sekil):
    counter = 0
    temp_list = []
    if sekil == 1:
        # range kısmını değiştir
        for i in range(128):
            counter = i % 24
            #print(f"Temp_list = {temp_list}")
            #print(f"i = {i}, counter = {counter}")
            if i < 24:
                temp_list.append(algoritma_sonuc[i])
            else:
                temp_list[counter] ^= algoritma_sonuc[i]
            
    
    elif sekil == 2:
        # range kısmını değiştir
        for i in range(128):
            counter = i % 21
            #print(f"Temp_list = {temp_list}")
            #print(f"i = {i}, counter = {counter}")
            if i < 21:
                temp_list.append(algoritma_sonuc[i])
            else:
                temp_list[counter] ^= algoritma_sonuc[i]


    return temp_list

def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m



text = input()
plain_text = text.encode("utf-8")
sekil = int(input())


key = bytes.fromhex("2b7e151628aed2a6abf7158809cf4f3c")
iv = bytes.fromhex("00112233445566778899aabbccddeeff")

# Encoding
cipher_text = encrypt(plain_text, key, Mode.CTR, iv)

# Decoding
plain_text = decrypt(cipher_text, key, Mode.CTR, iv)




scale = 16 ## equals to hexadecimal

num_of_bits = 8

binary_repr = int(bin(int(cipher_text.hex(), scale))[2:].zfill(num_of_bits))

res = list(map(int, str(binary_repr)))

mylist = mod_alma(res, sekil)

print(mylist)

if sekil == 1:
    sekilldolu = [
        [0,1], [0,3], 
        [1,1], [1,3],
        [2,1], [2,2], [2,3],
        [3,2],
        [4,1], [4,2], [4,3], [4,4],
        [5,2],
        [6,0],[6,1],[6,2],[6,3],
        [7,2],
        [8,0],[8,1],[8,2],[8,3],[8,4],[8,5]

    ]
else:
    sekilldolu = [
        [0,0], [0,1],[0,2],[0,7],[0,8],[0,9], 
        [1,2], [1,3],[1,4],[1,5],[1,6],[1,7],
        [2,2],[2,7],
        [3,1], [3,2],[3,3], [3,5],[3,6],[3,7],[3,8]

    ]

if sekil == 1:
    array = np.zeros([9,6])
else:
    array = np.zeros([4,10])


c = 0
for i in sekilldolu:
    if mylist[c] == 1:
        array[i[0], i[1]] = 10
    else:
        array[i[0], i[1]]= 3
    c +=1

plt.matshow(array)
plt.show()
