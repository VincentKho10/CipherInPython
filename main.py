import json
from random import shuffle

def keyCiphers(txt, ke):
    text = txt.lower()
    key = ke.lower()
    result = ""
    for i in range(len(text)):
        result += caesarEncrypt(text[i], ord(key[i])-97)
    return result

def keyDeCiphers(txt, ke):
    text = txt.lower()
    key = ke.lower()
    result = ""
    for i in range(len(text)):
        result += caesarEncrypt(text[i], (ord(key[i])-97)*-1)
    return result

def transpositionCipher(text):
    li = [i for i in range(len(text))]
    shuffle(li)
    encrypted = ""
    for i in li:
        encrypted += text[i]
    return {"idx": li, "data": encrypted}

def transpositionDeCipher(text,idx):
    decrypted = ""
    for i in range(len(text)):
        pos = idx.index(i)
        decrypted += text[pos]
    return decrypted

def caesarEncrypt(text, rot):
    result=""
    for i in range(len(text)):
        if(text[i] != " "):
            old_char_pos = ord(text[i])-97
            new_char_pos = old_char_pos+rot
            new_char_pos %= 26
            result+=chr(new_char_pos+97)
        else:
            result+=" "
    return result

def caesarDecrypt(text, rot):
    result=""
    for i in range(len(text)):
        if(text[i] != " "):
            old_char_pos = ord(text[i])-97
            new_char_pos = old_char_pos-rot
            new_char_pos %= 26
            result+=chr(new_char_pos+97)
        else:
            result+=" "
    return result

def main():
    # caesarencrypted = caesarEncrypt("kazakstan", 5)
    # print("encrypted :"+caesarencrypted)
    # caesardecrypted = caesarDecrypt(caesarencrypted, 5)
    # print("decrypted :"+caesardecrypted)

    # trspcip = transpositionCipher("olaf")
    # print(trspcip)
    # trspdcip = transpositionDeCipher(trspcip["data"], trspcip["idx"])
    # print(trspdcip)

    keycip = keyCiphers("ILOVEPITTSBURGH", "PICOCTFPICOCTFP")
    print(keycip)
    keydecip = keyDeCiphers(keycip, "PICOCTFPICOCTFP")
    print(keydecip)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
