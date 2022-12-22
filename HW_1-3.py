def encryptor(key, plain_text):
    encrypted = ""
    plain_text = plain_text.lower()
    for c in plain_text:

        if c.islower():
            # вычесть юникод 'a', чтобы получить индекс в диапазоне [0-25)
            c_index = ord(c) - ord('a')
            c_shifted = (c_index + key) % 26 + ord('a')
            c_new = chr(c_shifted)
            encrypted += c_new
        else:
            # если нет ни алфавита, ни числа, оставьте все как есть
            encrypted += c
    return encrypted.title()


assert encryptor(13, '') == ''
assert encryptor(13, 'Caesar Cipher') == 'Pnrfne Pvcure'
assert encryptor(-5, 'Hello World!') == 'Czggj Rjmgy!'
assert encryptor(27, 'Whoopi Goldberg') == 'Xippqj Hpmecfsh'

print(encryptor(13, ''))
print(encryptor(13, 'Caesar Cipher'))
print(encryptor(-5, 'Hello World!'))
print(encryptor(27, 'Whoopi Goldberg'))

# неудачная попытка
# # def encryptor(key, text):
# #     letters = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z]
# #     text = list(text)
#
# task_key = 2
# a = 'hello world'
# a = a.split(' ')
# print(a)
# char_list_1 = []
#
# # for len_ in range(len(a)):
# #     for i in a[len_]:
# #         char_list_1.append(i)
# # print(char_list_1)
#
# letters = 'abcdefghijklmnopqrstuvwxyz'
#
# for i in a[0]:
#     char_list_1.append(i)
# print(char_list_1)
# char_list_11 = []
# for r in char_list_1:
#     char_index = letters.index(r)
#     char_list_11.append(char_index)
# print(char_list_11)
#
# char_list_111 = []
# for t in char_list_11:
#     new_char_index = (t + task_key) % len(letters)
#     char_list_111.append(new_char_index)
# print(char_list_111)
#
# for y in char_list_111:
#
# # char_index = letters.index()
