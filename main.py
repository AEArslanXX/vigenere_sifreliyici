#şifreleyici fonksiyon
def encrypt(key_,text_):
    #alfabeler
    tr_alphabet = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "r", "s", "ş", "t", "u", "ü", "v", "y", "z"]

    #anahtar sözcüğü , indeksi ve uzunluğu
    key = key_
    key_len = len(key)
    #şifrelenecek kelime , indeksi ve uzunluğu
    text = text_.replace(" ","")
    text_index = []
    text_len = len(text)

    for b in text:
        if b in tr_alphabet:
            index = tr_alphabet.index(b)
            text_index.append(index)
        else:
            text_index.append(0)

    #şifreleme
    def encrypts():
        t = 0
        key_word_group = []
        key_ = "" 
        for c in key:
            key_word_group.append(c)
        while True:
            if t > key_len-1:
                t = 0
            key_ += key_word_group[t]
            t += 1
            if len(key_) == text_len:
                break
        return key_

    #tekrarlanmış anahtarı şifreleme
    key_indeks = []
    for d in encrypts():
        index_key = tr_alphabet.index(d) + 1
        key_indeks.append(index_key)
            
    #şifrelenmiş metni oluşturma
    encrypted_text_indeks = []
    encrypted_text = []
    for e in range(len(key_indeks)):
        encrypted_text_indeks.append(key_indeks[e] + text_index[e])

    for f in range(len(encrypted_text_indeks)):
        num = encrypted_text_indeks[f]
        if encrypted_text_indeks[f] > len(tr_alphabet):
            num %= 29
            encrypted_text.append(tr_alphabet[num])
        else:
            encrypted_text.append(tr_alphabet[num])

            
    return "".join(encrypted_text)
def decipher(key_,text_):
        #alfabeler
    tr_alphabet = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "r", "s", "ş", "t", "u", "ü", "v", "y", "z"]

    #anahtar sözcüğü , indeksi ve uzunluğu
    key = key_
    key_len = len(key)
    #şifrelenecek kelime , indeksi ve uzunluğu
    text = text_.replace(" ","")
    text_index = []
    text_len = len(text)

    for b in text:
        if b in tr_alphabet:
            index = tr_alphabet.index(b)
            text_index.append(index)
        else:
            text_index.append(0)

    #şifreleme
    def encrypt():
        t = 0
        key_word_group = []
        key_ = "" 
        for c in key:
            key_word_group.append(c)
        while True:
            if t > key_len-1:
                t = 0
            key_ += key_word_group[t]
            t += 1
            if len(key_) == text_len:
                break
        return key_

    #tekrarlanmış anahtarı şifreleme
    key_indeks = []
    for d in encrypt():
        index_key = tr_alphabet.index(d) + 1
        key_indeks.append(index_key)
            
    #şifrelenmiş metni oluşturma
    encrypted_text_indeks = []
    encrypted_text = []
    for e in range(len(key_indeks)):
        encrypted_text_indeks.append((text_index[e] - key_indeks[e]))

    for f in range(len(encrypted_text_indeks)):
        num = encrypted_text_indeks[f]%29
        encrypted_text.append(tr_alphabet[num])

            
    return "".join(encrypted_text)

print(encrypt("egemen","merhaba dünya"))
print(decipher("egemen","skvüföfjcçdo"))