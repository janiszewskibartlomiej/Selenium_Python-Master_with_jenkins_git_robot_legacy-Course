```python
####1. PIP

pip install -U nazwa_biblioteki   > instaluje jezeli nie ma juz zaintalowanej bioblioteki 
a jezeli jest juz zaintalowana to upgrade ta biblioteke
 
pip list >  pokazuje wszytskie dostepne/zainstalowane biblioteki

####2. Locators

id, name, class name, css, xpath, link, REgEx


####3. CSS Locator

id > #email or input#email
class > .inputtext or input.inputtext
attribute any e.g. 'type' >[type='email'] or with <tag> input[id='email']
łączone e.g. id + attribute> #pass[type='password']
tag + id + attribute > input#pass[type='password']
class + attribute .inputtext[type='email']
tag + class + attribute input.inputtext[type='email']

####4. XPath Locators
zaczynamy zawsze od //
single attribute > //tag_name[@atrrybute_name='value_attribute']
przykład > //input[@type='submit']
multiple attributes [OR] > FB login page > //input[@name='email' or @aria-label="Adres e-mail lub numer telefonu"]
multiple attributes [AND] > //select[@name='birthday_day' and @title='Dzień']
use * zamiast nazwy tagow lub nazw atrybutów > //*[@*='birthday_day' and @*='Dzień']  natomiast trzeba z tym uważaponiewaz może być parę wyników.
using innertext trzeba używać kompletnego tekstu słowo klucz = text() >  FB rejestracja > //div[text()='Zarejestruj się.']
using partial innertext - składnia jest trochę inna > FB rejestracja > //div[contains(text(),'się.')]  dla mie jest to funkcja o nazwie contains ktora przyjmuje 2 parametry > typ szukany i wartosć
partial value of attribute FB login > //input[contains(@type,'word')]
lokalizacja po parent > //table[@role='presentation']/tbody/tr[2]/td[1]/input  (dugi elemnt to normalnie 2)
```
