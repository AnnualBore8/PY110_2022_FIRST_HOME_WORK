# Решение 1 (Я знаю, что криво, но в изолированной ситуации оно работает)

# def remove_parentheses(text: str) -> str:
#     open_chart = text.find('(')
#     close_chart = text.rfind(')')
#     l_str = text[0:open_chart]
#     r_str = text[close_chart + 1:]
#     new_str = l_str + r_str
#     a = '  '
#     if len(new_str) == 0:
#         new_str = a
#         print(new_str)
#     return new_str

# Решение 2

def remove_parentheses(text):
    while ')' in text:
        r = text.find(')')
        l = text[:r+1].rfind('(')
        trash = text[l:r+1]
        text = text.replace(trash, '')
    return text

# Решение 3 (подглядел, что можно через данную функцию)

# import re
#
#
# def remove_parentheses(text):
#     n = 1  # run at least once
#     while n:
#         text, n = re.subn(r'\([^()]*\)', '', text)  # remove non-nested/flat balanced parts
#     return text


assert remove_parentheses("example(unwanted thing)example") == "exampleexample"
assert remove_parentheses("example (unwanted thing) example") == "example  example"
assert remove_parentheses("a (bc d)e") == "a e"
assert remove_parentheses("a(b(c))") == "a"
assert remove_parentheses("hello example (words(more words) here) something") == "hello example  something"
assert remove_parentheses("(first group) (second group) (third group)") == "  "
