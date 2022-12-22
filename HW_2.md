6 kuy


Удалите скобки
В этом ката вам дается строка, например:


"example(unwanted thing)example"
Ваша задача — удалить все, что находится внутри скобок, а также сами скобки.


Приведенный выше пример вернет:


"exampleexample"
Примечания
Кроме круглых скобок в строке могут встречаться только буквы и пробелы. Не беспокойтесь о других скобках, подобных "[]"и "{​​​​​​​}​​​​​​​"поскольку они никогда не появятся.
Может быть несколько скобок.
Скобки могут быть вложенными.


assert remove_parentheses("example(unwanted thing)example") == "exampleexample"
assert remove_parentheses("example (unwanted thing) example") == "example  example"
assert remove_parentheses("a (bc d)e") == "a e"
assert remove_parentheses("a(b(c))") == "a"
assert remove_parentheses("hello example (words(more words) here) something") == "hello example  something"
assert remove_parentheses("(first group) (second group) (third group)") == "  "



5 kuy


Цифровой переводчик Base64
Наша стандартная система нумерации (Base 10). Это включает в себя от 0 до 9. Двоичный (Base 2), только 1 и 0. И шестнадцатеричное (основание 16) (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F). Шестнадцатеричная буква «F» имеет (основание 10) значение 15. (Основание 64) имеет 64 отдельных символа, которые преобразуются в значение (основание 10) от 0 до 63.


####Напишите метод, который будет преобразовывать строку из (Base 64) в целочисленное значение (Base 10).


(Base 64) символы от меньшего к большему будут


ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
Где «А» равно 0, а «/» равно 63.


Так же, как и в стандарте (основание 10), когда вы достигаете самого большого отдельного целого числа 9, следующее число добавляет дополнительное место и начинается с начала 10; так же (Base 64), когда вы дойдете до 63-й цифры '/', а следующее число добавляет дополнительное место и начинается с начала «BA».


Пример:


base64_to_base10("/") # => 63
base64_to_base10("BA") # => 64
base64_to_base10("BB") # => 65
base64_to_base10("BC") # => 66
Напишите метод base64_to_base10, который будет принимать строковое число (Base 64) и выводить его значение (Base 10) в виде целого числа.


test.assert_equals(base64_to_base10("A"  ), 0    )
test.assert_equals(base64_to_base10("/"  ), 63   )
test.assert_equals(base64_to_base10("BA" ), 64   )
test.assert_equals(base64_to_base10("//" ), 4095 )
test.assert_equals(base64_to_base10("WIN"), 90637)
















