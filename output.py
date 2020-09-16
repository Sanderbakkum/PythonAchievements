Last login: Wed Sep 16 13:58:26 on ttys000
sanderbakkum@MacBook-Pro-van-Sander ~ % cd School                
sanderbakkum@MacBook-Pro-van-Sander School % cd PythonAchievements 
sanderbakkum@MacBook-Pro-van-Sander PythonAchievements % python3
Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 - 10
90
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> print('Mijn naam is Sander')
Mijn naam is Sander
>>> naam = 'Sander'
>>> print(naam)
Sander
>>> print(naam.upper())
SANDER
>>> print(naam[0:2])
Sa
>>> print(naam[::-1])
rednaS
>>> leeftijd = 16
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo Sander ben je al 16 jaar?
>>> leeftijd = leeftijd + 1 
>>> leedtijd
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'leedtijd' is not defined
>>> leeftijd
17
>>> leeftijd-=1
>>> leeftijd
16
>>> if leeftijd < 18:
... hoelang_tot18jaar = 18 - leeftijd
  File "<stdin>", line 2
    hoelang_tot18jaar = 18 - leeftijd
    ^
IndentationError: expected an indented block
>>> if leeftijd < 18:
... hoelang_tot18jaar = 18 - leeftijd
  File "<stdin>", line 2
    hoelang_tot18jaar = 18 - leeftijd
    ^
IndentationError: expected an indented block
>>> if leeftijd < 18:
... hoelang_tot18jaar = 18 - leeftijd
  File "<stdin>", line 2
    hoelang_tot18jaar = 18 - leeftijd
    ^
IndentationError: expected an indented block
>>> if leeftijd < 18:
... hoelang_tot18jaar = 18 - leeftijd print('Over ' + str(hoelang_tot18jaar) + ' Jaar wordt je 18')
  File "<stdin>", line 2
    hoelang_tot18jaar = 18 - leeftijd print('Over ' + str(hoelang_tot18jaar) + ' Jaar wordt je 18')
    ^
IndentationError: expected an indented block
>>> if leeftijd < 18:
... hoelang_tot18jaar = 18 - leeftijd
  File "<stdin>", line 2
    hoelang_tot18jaar = 18 - leeftijd
    ^
IndentationError: expected an indented block
>>> if leeftijd < 18:
...     hoelang_tot18jaar = 18 - leeftijd
...     print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
... 
Over 2 jaar wordt je 18
>>> elif leeftijd > 18:
  File "<stdin>", line 1
    elif leeftijd > 18:
    ^
SyntaxError: invalid syntax
>>>     hoelang_al18jaar = leeftijd - 18
  File "<stdin>", line 1
    hoelang_al18jaar = leeftijd - 18
    ^
IndentationError: unexpected indent
>>>     print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
  File "<stdin>", line 1
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
    ^
IndentationError: unexpected indent
>>> if leeftijd < 18:
...     hoelang_tot18jaar = 18 - leeftijd
...     print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
... elif leeftijd > 18:
...     hoelang_al18jaar = leeftijd - 18
...     print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
... else:
...     print('Je bent precies ' + str(leeftijd) + ' jaar')
... 
Over 2 jaar wordt je 18
>>> from random import randint
>>> randint(o,1000)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'o' is not defined
>>> randint(0,1000)
898
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
467
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 467
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2020-09-16 14:20:33.203599
>>> datum.strftime('%A %d %B %Y')
'Wednesday 16 September 2020'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'woensdag 16 september 2020'
>>> locale,setlocale(locale.LC_TIME, 'it_IT')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'setlocale' is not defined
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'Mercoledì 16 Settembre 2020'
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> 
