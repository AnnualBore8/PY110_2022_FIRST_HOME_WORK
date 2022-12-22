# Решение очень похоже на шифр цезаря из первого домашнего задания.
# только там, из-за формулировки задания можно было сделать проще, чем тут

def encryptor(plain_text, key=13):
    ROT13 = ""

    for letter in plain_text:

        if letter.islower():
            letter_index = ord(letter) - ord('a')
            letter_shifted = (letter_index + key) % 26 + ord('a')
            letter_new = chr(letter_shifted)
            ROT13 += letter_new

        elif letter.isupper():
            letter_index = ord(letter) - ord('A')
            letter_shifted = (letter_index + key) % 26 + ord('A')
            letter_new = chr(letter_shifted)
            ROT13 += letter_new

        else:
            ROT13 += letter
    return ROT13


print(encryptor("EBG13 rknzcyr."))
print(encryptor("This is my first ROT13 excercise!"))


assert encryptor("EBG13 rknzcyr.") == "ROT13 example."
assert encryptor("This is my first ROT13 excercise!") == "Guvf vf zl svefg EBG13 rkprepvfr!"