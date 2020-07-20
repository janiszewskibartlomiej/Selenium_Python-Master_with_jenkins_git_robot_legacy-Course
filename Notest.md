```python
#### 1. PIP

pip install -U nazwa_biblioteki   > instaluje jezeli nie ma juz zaintalowanej bioblioteki 
a jezeli jest juz zaintalowana to upgrade ta biblioteke
 
pip list >  pokazuje wszytskie dostepne/zainstalowane biblioteki

#### 2. Locators

id, name, class name, css, xpath, link, REgEx


#### 3. CSS Locator

* id > #email or input#email
* class > .inputtext or input.inputtext
* attribute any e.g. 'type' >[type='email'] or with <tag> input[id='email']
* łączone e.g. id + attribute> #pass[type='password']
* tag + id + attribute > input#pass[type='password']
* class + attribute .inputtext[type='email']
* tag + class + attribute input.inputtext[type='email']

#### 4. XPath Locators
* zaczynamy zawsze od //
* single attribute > //tag_name[@atrrybute_name='value_attribute']
* przykład > //input[@type='submit']
* multiple attributes [OR] > FB login page > //input[@name='email' or @aria-label="Adres e-mail lub numer telefonu"]
* multiple attributes [AND] > //select[@name='birthday_day' and @title='Dzień']
* use '*' zamiast nazwy tagow lub nazw atrybutów > //*[@*='birthday_day' and @*='Dzień']  natomiast trzeba z tym uważaponiewaz może być parę wyników.
* using innertext trzeba używać kompletnego tekstu słowo klucz = text() >  FB rejestracja > //div[text()='Zarejestruj się.']
* using partial innertext - składnia jest trochę inna > FB rejestracja > //div[contains(text(),'się.')]  dla mie jest to funkcja o nazwie 
* contains ktora przyjmuje 2 parametry > typ szukany i wartosć
* partial value of attribute FB login > //input[contains(@type,'word')]
* lokalizacja po dzieciach vv w dół > //table[@role='presentation']/tbody/tr[2]/td[1]/input  (dugi elemnt to normalnie 2)
* lokalizacja po rodzicach ^^ w górę > słowo kluczowe parent:: FB rejestracja  > //div[@class='_5dbb']/parent::div[@class='mbm _br- _a4y']
* lokalizacja siblings - na tej samej lini/wcienciu - rodzeństwo jako `drugie` - following-sibling::>  //input[@id='tab2']/following-sibling::label
* lokalizacja siblings - na tej samej lini/wcienciu - rodzeństwo jako pierwsze - preceding-sibling::>  //input[@id='tab2']/preceding-sibling::label
* łączenie różnych metod > //input[@id='pass']/parent::td/precending-sibling::td/input
 przykłąd FB rej > //div[@class='_5dbb']/parent::div/preceding-sibling::div/div

#### 5. bibliotek faker do generowania danych personlanych 
 from faker import Faker
 
#### 6. range od 10 do 1 - decrement
    for i in range(10,0, -1)
       print(i)
       
#### 7. funcje wbudowane

lista.insert(index, "cos do dodania" )
lista[index] = "cos do dodnia"
lista.remove(55) >> usunie pierwsza napodkna cyfre 55 - tylko pierwsza
lista.count(szukanyWartość)
lista.index(szukanaWartość)
 
#### 8. Konstruktor nic nie moze zwracać

#### 9. file: 

opennig mode:

r, w, a, r+ [read and write], w+ [write and read], a+ [append and read]

reading file:

file = open("fiel.py", mode="r")

file.read()  >> czyta cały plik
file.readline() >> czyta jedną linię > pierwszą
file.readline() >> czyta jedną linię > drugą bo drugi raz wywołaliśmy
file.read(10)  >> czyta pierwsze 10 znaków z pliku

czytanie każdego znaku z pliku:

for i in file.read():
    prit(i)
    
czytanie kazdej lini z pliku one by one:

line = file.readline()

while line:
    print(line)
    line = file.readline()
    
zapis:

file = open("fiel.py", mode="w")
file.write("Tekst do zapisu")
file.close()

mode="a" >> dokąda za każdym razem nowe dane do pliku

funcja tell():

file.readline()
print(file.tell())  >> wydrukuje liczbe znnakow odczytanych np 16 czyli tak naprwde pozycje kursora po odczycie znakow
file.readline()
print(file.tell())  >> wydrukuje liczbe znnakow odczytanych - wszytskich np 32 g[sumuje liczbe znakow]

seek() function is used to change the position of the File Handle to a given specific position. File handle is like a cursor, which defines from where the data has to be read or written in the file.

Syntax: f.seek(offset, from_what), where f is file pointer

Parameters:
Offset: Number of postions to move forward
from_what: It defines point of reference.

The reference point is selected by the from_what argument. It accepts three values:

0: sets the reference point at the beginning of the file
1: sets the reference point at the current file position
2: sets the reference point at the end of the file
By default from_what argument is set to 0.

# in binary mode 
f = open("data.txt", "rb") 
  
# sets Reference point to tenth 
# position to the left from end 
f.seek(-10, 2) 
  
# prints current position 
print(f.tell()) 
  
# Converting binary to string and  
# printing 
print(f.readline().decode('utf-8')) 

 #### 10. configuration file:
 
 Config.cfg
 [DEV]
 username=test
 password=tesing
 
 from configparser import ConfigParser
 
 Creating Object >> config = ConfigParser()
 read from congig file >> config.get("path/Config.cft")
 get data >> config.get("Name_of_section", "name_of_variable")    w mim wypadku config.get("DEV", "username") 
```
