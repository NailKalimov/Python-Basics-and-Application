"""Library:
https://education.yandex.ru/handbook/python/article/stroki-kortezhi-spiski
https://docs.python.org/3.5/library/re.html"""
# Tasks
""" 0
Есть строка s = "abcdefghijk".
В поле ответа через пробел запишите строки (без кавычек), полученные в результате следующих операций:

# s = 'abcdefghijk'
s[3:6]
s[:6]
s[3:]
s[::-1]
s[-3:]
s[:-6]
s[-1:-10:-2]
"""
""" 6
Вам дана последовательность строк.
В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿ и выведите полученные строки.

Sample Input:
I need to understand the human mind
humanity

Sample Output:
I need to understand the computer mind
computerity
"""
""" 1
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
Примечание:
Считать все строки по одной из стандартного потока ввода вы можете, например, так
import sys
for line in sys.stdin:
    line = line.rstrip()
    # process line

Sample Input:
catcat
cat and cat
catac
cat
ccaatt

Sample Output:
catcat
cat and cat
"""
""" 2
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве слова.

Примечание:
Для работы со словами используйте группы символов \b и \B.
Описание этих групп вы можете найти в документации(https://docs.python.org/3.5/library/re.html).
Sample Input:
cat
catapult and cat
catcat
concat
Cat
"cat"
!cat?

Sample Output:
cat
catapult and cat
"cat"
!cat?
"""
""" 3
Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.
Sample Input:
zabcz
zzz
zzxzz
zz
zxz
zzxzxxz

Sample Output:
zabcz
zzxzz
"""
""" 4 
Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\﻿".
Sample Input:
\w denotes word character
No slashes here
Sample Output:
\w denotes word character
"""
""" 5
Вам дана последовательность строк.
Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).

Sample Input:
blabla is a tandem repetition
123123 is good too
go go
aaa

Sample Output:
blabla is a tandem repetition
123123 is good too
"""
""" 7
Вам дана последовательность строк.
В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен), 
на слово "argh".
Примечание:
Обратите внимание на параметр count у функции sub.
Sample Input:
There’ll be no more "Aaaaaaaaaaaaaaa"
AaAaAaA AaAaAaA

Sample Output:
There’ll be no more "argh"
argh AaAaAaA
"""
""" 8
Вам дана последовательность строк.
В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
Буквой считается символ из группы \w.
Sample Input:
this is a text
"this' !is. ?n1ce,

Sample Output:
htis si a etxt
"htis' !si. ?1nce,
"""
""" 9
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w.
Sample Input:
attraction
buzzzz

Sample Output:
atraction
buz
"""
""" *
Осуществите алгоритм преобразования строки следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются 
на этот символ и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную 
последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.

Sample Input 1:
aaaabbcaa
Sample Output 1:
a4b2c1a2

Sample Input 2:
abc
Sample Output 2:
a1b1c1
"""
""" **
Задача сложнее остальных задач из этого раздела, и идея ее решения выходит за рамки простого понимания 
регулярных выражений как средства задания шаблона строки. Мы решили включить данную задачу в урок, чтобы 
показать, что регулярным выражением можно проверить не только "внешний вид" строки, но и заложенный в 
ней смысл. 
Вам дана последовательность строк.
Выведите строки, содержащие двоичную запись числа, кратного 3.
Двоичной записью числа называется его запись в двоичной системе счисления.
Примечание 2:
﻿Данная задача очень просто может быть решена приведением строки к целому числу и проверке остатка от деления 
на три, но мы все же предлагаем вам решить ее, не используя приведение к числу.
Sample Input:
0
10010
00101
01001
Not a number
1 1
0 0

Sample Output:
0
10010
01001
"""
# ANSWERS:
# 1
import sys
import re

pattern = r"cat"
for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(pattern, string=line)) >= 2:
        print(line)

# 2
import sys
import re

pattern = r"\bcat\b"
for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(pattern, string=line)) != 0:
        print(line)
# 3
import sys
import re

pattern = r"z...z"
for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(pattern, string=line)) != 0:
        print(line)
# 4
from sys import stdin
from re import findall

pattern = r"\\"
for line in stdin:
    line = line.rstrip()
    if len(findall(pattern, string=line)) != 0:
        print(line)
# 5
from sys import stdin
from re import findall, match

pattern = r"\b(\w+)\1\b"
for line in stdin:
    if match(pattern,line.rstrip()) is not None:
        print(line.rstrip())
# 6
from sys import stdin

for line in stdin:
    print(line.replace("human", "computer").rstrip())

# 7
from sys import stdin
import re

pattern = r"\b[a|A]+\b"
for line in stdin:
    print(re.sub(pattern, "argh", line.rstrip(), count = 1))
    #print(line.replace("human", "computer").rstrip())

# 8
from sys import stdin
import re

pattern = r"(\w)(\w)(\w*)"
for line in stdin:
    print(re.sub(pattern, r"\2\1\3", line.rstrip()))
# 9
from sys import stdin
import re

pattern = r"(\w)\1+"
for line in stdin:
    print(re.sub(pattern, r"\1", line.rstrip()))
