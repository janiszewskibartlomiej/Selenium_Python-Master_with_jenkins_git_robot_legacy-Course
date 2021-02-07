```python
1. PIP

pip install -U nazwa_biblioteki   > instaluje jezeli nie ma juz zaintalowanej bioblioteki 
a jezeli jest juz zaintalowana to upgrade ta biblioteke
 
pip list >  pokazuje wszytskie dostepne/zainstalowane biblioteki

2. Locators

id, name, class name, css, xpath, link, REgEx 
```

##  Preferred selector order: id > name > css > xpath

``` python
3. CSS Locator

* id > #email or input#email
* class > .inputtext or input.inputtext
* attribute any e.g. 'type' >[type='email'] or with <tag> input[id='email']
* łączone e.g. id + attribute> #pass[type='password']
* tag + id + attribute > input#pass[type='password']
* class + attribute .inputtext[type='email']
* tag + class + attribute input.inputtext[type='email']

4. XPath Locators
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

5. bibliotek faker do generowania danych personlanych 
 from faker import Faker
 
 faker = Faker()
 faker.name()
 faker.email()
 faker.city()
 faker.pnonenumber()
 
 
6. range od 10 do 1 - decrement
    for i in range(10,0, -1)
       print(i)
       
7. funcje wbudowane

lista.insert(index, "cos do dodania" )
lista[index] = "cos do dodnia"
lista.remove(55) >> usunie pierwsza napodkna cyfre 55 - tylko pierwsza
lista.count(szukanyWartość)
lista.index(szukanaWartość)
 
8. Konstruktor nic nie moze zwracać

9. file: 

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

 10. configuration file:
 
 Config.cfg
 [DEV]
 username=test
 password=tesing
 
 from configparser import ConfigParser
 
 Creating Object >> config = ConfigParser()
 read from congig file >> config.read("path/Config.cft")  >> potrafi być problem z lokalizacją leratywną w zalezności gdzie odpala się dana metoda
 get data >> config.get("Name_of_section", "name_of_variable")    w mim wypadku config.get("DEV", "username") 
 
 11. nadpisywanie metod dziedziczących:
 
 wystraczy stworzy metode o tej samej nazwie i z tymi samymi parametrami w clasie głównej którą wołamy i  wten sposób nadpiszemy metodę z dziedziczenia np z inną logiką.
 czyli class A:  def sub(self, a, b): return b - a     class B(A): def sub(self, b, a): return b - a
 
 12. praca z plikami excel:
 
 #odczyt danych
 
 workbook = xlrd.open_workbook(
    "D:\...")

# ilość kart
print(workbook.nsheets)

# ustawienie level na danej karcie
worksheet = workbook.sheet_by_index(1)

print(worksheet.nrows)  # ilosc wierszy
print(worksheet.ncols)  #ilosc kolumn

worksheet = workbook.sheet_by_name("Styczeń")
print(worksheet.nrows)  # ilosc wierszy
print(worksheet.ncols)  #ilosc kolumn

# pobieranie danych

workcell = worksheet.cell(rowx=70, colx=3)
print(workcell)
print(workcell.value)

# pobieranie wszystkich danych

row = worksheet.nrows
column = worksheet.ncols

for i in range(0, row):
    for j in range(0, column):
        wc = worksheet.cell(i, j)
        print(wc.value)

 
 
 # object of workbook >> zapis

wk = xlwt.Workbook()

ws = wk.add_sheet("Testing")
ws.write(0, 0, "Testing Word") # row, column, data to write
ws.write(0, 1, "Testing Word 2")

# zapis workbook  ta biblioteka moze zapisywac w 2 formatach

wk.save("D:/GITHUB/Selenium_Python_beginner_to_advanced_with_jenkins_git_robot_legacy-Course/write_excel_first1.xls")

 #### openpyxl:
 
 import openpyxl

# load workbook

wk = openpyxl.load_workbook(
    "D:/..../Bd2019.xlsx")

# wszytskie nazwy kart
print(wk.sheetnames)

print("Aktywne karty: " + wk.active.title)

# tworzenie obiektu karty > a raczej przejscie na konkretną kartę

sh = wk['Luty']
print(sh.title)

# pobieranie komurki  - u mnie to nie dzila bo pokazuje funkcje liczaca
print(sh["D71"])
print(sh["D71"].value)

# rozwiazanie >> wb = openpyxl.load_workbook(filename, data_only=True)
# The data_only flag helps.

c1 = sh.cell(17, 4)  # row, column nr a nie index!!!
print(c1.value)

c2 = sh.cell(row=74, column=3)  # badz poprzez prametryzowanie
print(c2.value)
print(c2.row)
print(c2.column)

# odczyt calosci z wokrbook

# find rows info

rows = sh.max_row
columns = sh.max_column

print("rows: ", rows)
print("columns: ", columns)

for row in sh["A1":"AN257"]:  # [start - lewy gorny rog : prawy dolny rog]
    for c in row:
        print(c.value)
 

 # writing
 
 
wk = openpyxl.Workbook()
sh = wk.active
sh.title = "Testing_write"
print(sh.title)

sh["A4"].value = "test to write cell"

wk.create_sheet(title="Testing2")
sh1 = wk["Testing2"]
sh1["A3"] = "+91-85492145"

# remove sheet
wk.remove(wk["Testing_write"])

wk.save("D:/.../test_write_openpyxl.xlsx")
 
 
 13. Komendy webdriver - istotnijesze dla mnie:
 
 dobra praktyka jest ustawianie path z dwoma znakami "\\" np>> path="C:\\Users\\TestingWorld\\Downloads\\chromedriver_win32 (3)\\chromedriver.exe"
 
 act = ActionChains(driver)

    # Click operation
    act.click().perform()
    act.click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

    # Context Click(Right Click)
    act.context_click().perform()
    act.context_click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

    # double click
    act.double_click().perform()
    act.double_click(driver.find_element_by_xpath("//a[text()='Login']")).perform()
    
    # press CTRL + literka "a"
    act.key_down(Keys.CONTROL).send_keys("a").perform()
    
    #selecty
    element = Select(driver.find_element_by_name("sex"))
    element.select_by_index(index=>liczba)
    element.select_by_value("value"=>text)
    element.select_by_visible_text(text)
    
    element.first_selected_oprtion.text
    element.options  >> wszytskie opcje ale zeby zobaczyć trzeba wolac text na konkretnej ocji np [i.text for i in element.options]
    element.all_all_selected_options   >> to na listach wszytskie zaznaczone
    
    element.deselect_..... >> do usuąniecią zaznaczenia ale dział tylko z listą
    
    element.move_to_element().perform() >> hover
    
    driver.title 
    driver.page_source 
    na kazydm elemencie webdriver mozna zawolac element.text
    element.get_attribute("nazwa_atrybutu" albo każdy innerText)
    
    
    driver.execute_script("JS code")
    
14 pytest:

pytest -k nazwa_pliku lub nazwa_testu    flaga k po nazwie szuka
pytest -v >> verbose wiecej informacji na temat testu
pytest -s >> drukuje printy z kodu  do konsoli
pytest -vv >> wiecej informacji z printem calego stringa a nie tylko czesci przy np assercji

@pytest.mark.skip("message) z ta flaga jest pomijane

@pytest.mark.skipif(a>100, reason = "message")  >> jezeli ten warunek jest spelniony to bedzie skip i dostajemy message

grupowanie testow otagowanie >> @pytest.mark.nazwa_grupy   np smoke

pytest -m smoke -v   >> flaga m mowi o uruchomieniu tagu o nazwie somke

uruchomie wszytskich testow poza danym tagiem >> python -m "not smoke" -v

@pytest.fixture()
def set_path():
global driver >> trzeba ustawić aby ta zmienna byla widoczna w danych testach
path_to_chrome_driver= ...
driver = ...
    
def test_123(set_path):  wykona sie fixture set_path a pote def 123

zeby start drivera byl tylko raz i zakonczenie tylko raz na konciu po yield mozmey skorzystac z :
@pytest.fxture(scope="module")
def set_path():
path_to_chrome_driver= ...
driver = ...

assert driver.title == "test title"

pytest -s >> to jest iterator i printuje wynik detali
    
15. Waits:

można ustawic globalny wait ale jest nie doskonaly w moim przekonaiu. = implicitly_wait() 

@pytest.fixture()
def driver():
    firefox_driver = webdriver.Firefox(
        executable_path="\\geckodriver.exe")
    firefox_driver.set_page_load_timeout(30)  >> ładowanei strony max 30 sek

    yield firefox_driver
    firefox_driver.quit()


def test_1(driver):
   
    driver.get("http://cadillac.pl")
    wait = WebDriverWait(driver, 30).until(ec.url_contains(url="/cadillac")) czy url in current_url
    print(wait)  # true
    driver.get("http://cadillac.com")
    wait2 = WebDriverWait(driver, 30).until(ec.url_to_be(url="https://www.cadillac.com/"))  czy url == current_url
    print(wait2)  # true
    assert wait2 is True

16. handles

popup
allwindows = driver.window_handles
    mainWin=""
    for win in allwindows:
        driver.switch_to.window(win)
        if(driver.current_url=='http://www.thetestingworld.com/testings/manage_customer.php'):
            driver.find_element_by_xpath("//button[text()='Start Download']").click()
            time.sleep(5)
            driver.close()
        elif(driver.current_url=='http://www.thetestingworld.com/testings/dashboard.php'):
             mainWin=win


    driver.switch_to.window(mainWin)
    
       # jak mamy cos w iframe to uzywamy
       driver.switch_to.frame("nazwa_iframe")
       
       driver.switch_to.default_content()   >>> do przelącenia się na rodzica window

17. logging module

logger = logging.getLogger(str(__name__))
logger.setLevel(logging.INFO)

# Create a file handler
handler_warn = logging.FileHandler('warning_log.txt')
handler_warn.setLevel(logging.WARNING)

handler_info = logging.FileHandler('info_log.txt')
handler_info.setLevel(logging.INFO)

# create a logging format

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler_warn.setFormatter(formatter)
handler_info.setFormatter(formatter)

# add the handler to the logger

logger.addHandler(handler_warn)
logger.addHandler(handler_info)

logger.info('Information')
logger.warning('warning')

18. Allure report

pip install allure-pytest

npm install -g allure-commandline --save-dev

pytest --alluredir ./reports/20200730/allure

wejsc do katalogu w ktorym ma byc wygenerowany raport >>reports\20200730\HTML_report>allure generate D:\...\h_v9\reports\20200730\allure --clean

19. Importy - problemy:

odpalenie z konsoli moze okazac sie niemozliwe poniewaz importy nie beda wykonywane bo import szuka pakietow a nie folderów w tum celu trzeba dodać w danym katalogu:
__init__.py i w nim zaiportować dany plik z bierzacego katalogu >> np from . import test_....

"./tests/..."  kropka w tym wypadku oznacza nasz root 

scieszka do drivera powinna byc user\\folder\\  z 2 back slash  lub /user/folder/... slash

20. Data Driven Testing:

@pytest.fixture(params=["firefox_driver", "chrome_driver"])
def driver(request):
    global driver
    if request.param == "chrome_driver":
        path = "D:\\GITHUB\\Selenium_Python_beginner_to_advanced_with_jenkins_git_robot_legacy-Course\\drivers\\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=path)

    if request.param == "firefox_driver":
        path = "D:\\GITHUB\\Selenium_Python_beginner_to_advanced_with_jenkins_git_robot_legacy-Course\\drivers\\geckodriver.exe"
        driver = webdriver.Firefox(executable_path=path)

    driver.maximize_window()
    yield driver
    driver.close()


def data_generator():
    li = [("user1", "pass1"), ("user2", "pass2"), ("user3", "pass3")]
    return li


@pytest.mark.parametrize('enter_username_and_password', data_generator())
def test_validation(enter_username_and_password, driver):
    driver.get("http://www.theTestingWorld.com/testings")
    driver.find_element_by_xpath("//label[text()='Login']").click()
    driver.find_element_by_name("_txtUserName").send_keys(enter_username_and_password[0])
    driver.find_element_by_name("_txtPassword").send_keys(enter_username_and_password[1])

21. Gherkin language:

nazwa_pliku.feature

extension to notepad++  https://github.com/AndyLPK247/automation-panda-resources



Feature: Scenario: Given: When: Then: And: But:

Feature: Nazwa feature >> define End to End scenario
         jakis opis - description
         
     Scenario: nazwa tests cases
     
          Given dane początkowe >> nasz init
     
przykład:

Feature: Google Searching
  As a web surfer, I want to search Google, so that I can learn new things.
  
  Scenario: Simple Google search
    Given a web browser is on the Google page
    When the search phrase "panda" is entered
    Then results for "panda" are shown
    And the related results include "Panda Express"
    But the related results do not include "pandemonium"

Background
A Background allows you to add some context to the scenarios that follow it. It can contain one or more Given steps, which are run before each scenario, but after any Before hooks.
A Background is placed before the first Scenario/Example, at the same level of indentation.
Background is also supported at the Rule level, for example:

Feature: Overdue tasks
  Let users know when tasks are overdue, even when using other
  features of the app

  Rule: Users are notified about overdue tasks on first use of the day
    Background:
      Given I have overdue tasks

    Example: First use of the day
      Given I last used the app yesterday
      When I use the app
      Then I am notified about overdue tasks

    Example: Already used today
      Given I last used the app earlier today
      When I use the app
      Then I am not notified about overdue tasks



Scenario Outline

The Scenario Outline keyword can be used to run the same Scenario multiple times, with different combinations of values.
Scenario outlines allow us to more concisely express these scenarios through the use of a template with < >-delimited parameters:

Scenario Outline: eating
  Given there are "<start>" cucumbers
  When I eat "<eat>" cucumbers
  Then I should have "<left>" cucumbers

  Examples:
    | start | eat | left |
    |    12 |   5 |    7 |
    |    20 |   5 |   15 |

Keywords
Each line that isn’t a blank line has to start with a Gherkin keyword, followed by any text you like. The only exceptions are the feature and scenario descriptions.

The primary keywords are:

Feature
Rule (as of Gherkin 6)
Example (or Scenario)
Given, When, Then, And, But for steps (or *)
Background
Scenario Outline (or Scenario Template)
Examples
There are a few secondary keywords as well:

""" (Doc Strings)
| (Data Tables)
@ (Tags)
# (Comments)
"test"  (steps argument) exp  User enter "test" in search field   >> w automacie string test bedzie wprowadzony w inputcie
"""

pip install behave   dokumentaja https://behave.readthedocs.io/en/latest/gherkin.html

przyklady >> https://automationpanda.com/2017/01/27/bdd-101-gherkin-by-example/

             https://docs.behat.org/en/v2.5/guides/1.gherkin.html
             

	![](https://github.com/janiszewskibartlomiej/Selenium_Python-Master_with_jenkins_git_robot_legacy-Course/blob/master/2020-10-09_23h17_10.png)
	![](https://github.com/janiszewskibartlomiej/Selenium_Python-Master_with_jenkins_git_robot_legacy-Course/blob/master/2020-10-09_23h27_24.png)
	![](https://github.com/janiszewskibartlomiej/Selenium_Python-Master_with_jenkins_git_robot_legacy-Course/blob/master/2020-10-09_23h37_38.png)
	![](https://github.com/janiszewskibartlomiej/Selenium_Python-Master_with_jenkins_git_robot_legacy-Course/blob/master/2020-10-09_23h38_48.png)
 
MOJ PRZYKŁAD

Feature: define End to End scenario
          ta i kolejne linijki to jest description of feature
  Scenario:  to jest nazwa test case of the feature
      Given  initial point przed test case running
      
22. BEHAVE

features
 - steps
   - step_definition.py
-environment.py
- *.feature

odpalic mozna np > `behave features`

Przekazywanie zmiennych pomiedzy funkcjami testowymi poprzez obiekt context  np context.driver = Chrome()

odpalanie scenario po tagu [tag nadany `@smoke`]  behave --tags=smoke,kolejnyTag

aby odpalic testy nalerzce do obu tagow to trzeba behave --tags=smoke --tags=koljnyTagZTegoSamegoTestu

## environment file >> 
def before_all(context):
context.driver = Chrome()

def after_all(context):
context.driver.close()

jeden driver na wszytskie testy i dna metoda close()

alternatywan to podzial na *feature*:

def before_feature(context, feature):
context.driver = Chrome()

def after_feature(context, feature):
context.driver.close()

lub *scenario*:

def before_scenario(context, scenario):
context.driver = Chrome()

def after_scenario(context, scenario):
context.driver.close()

mozemy rowniez uzwyac metod before i after jako tagow:

def before_tag(context, tag):
context.driver = Chrome()

def after_tag(context, tag):
context.driver.close()

*Rapoty*

pip install allure-behave

odpalamy testy z flaga zapisy danych chyba w json

`behave -f allure_behave.formatter:AllureFormater -o pathToLocation`

a nastepnie tworzymy html z konsoli

`allure serve pathTolocationGeneratedData`

23. GIT

git diff nazwaPliku.xxx  

git checkout -- nazwaPliku.xx >> przelaczamy sie na plik przed zmianami

git remote -v >> pokazuje zdalne repo ploczaczone z lokalnym

git remote add origin "adres url"

git push origin master  - wrzucmy na zdlane repo

24. Jenkins

start server jenkins >> `java -jar "nazwaPliku_war.tmp" --httpPort=8080

konfiguracja java w http://localhost:8086/configureTools > JDK instalation trzeba ppodac nazwe dowolna i path to jdk folder

w tej samej lokalizacji config dodac path to git.exe

dodat pythona do jenkins poprzez http://localhost:8080/configure  zaznaczyc Environment variables i doac path do katalu instalacji python a druga do katalogu skrypt w python

http://localhost:8086/pluginManager/available  dodac allure

potem zaciagnac allure comandline

i w http://localhost:8086/configureTools/ dodac nazwe ALLURE i direction path 

w configu projektu dodajemy post-buid-Actions i wpisujemy katalog gdzie sa generowane raporty Reports bo w konsoli dodajemy pytest --alluredir=./Reports test_scenarios


w konsoli wpisujemy komendy:

set Path=%PYTHON_HOME%;%Path%
rmdir /s /q Reports   # usuwamy aby dane sie nie dopisywaly w danym buildzie
rmdir /s /q allure-report  # usuwamy aby dane sie nie dopisywaly w danym buildzie
pip install -r requirements-test.txt
pip install allure-robotframework

robot  --listener allure-robotframework TestCases

exit 0 # konczy bild jest potrzeny bo potem morze byc generowany raport
----
cd test_scenarios

pytest --alluredir=.Reports

envy dodalem za pomoca konsoli  echo klucz=wartosc >> .env

25. Robot framework

trzeba w pycharm zaintalowac plugin 'IntelliBot @SeleniumLibrary'

pip install robotframework 

pip install robotframework-seleniumlibrary

pliki.robot

https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html

wzorce w resources/plik.robot

26 pip install  requests, jsonpath

#send get request
response = requests.get(url)

# response content
response.content

response.headers
response.headers.get('Date')    #get specific header
response.headers.get('Server')


# Fetch cookies
response.cookies

# fetch encoding
response.encoding

# time response
response.elapsed

response.status_code

# convert to json form

json_response = json.loads(response.text)

# Featch value using json path
pip install jsonpath

value = jsonpath.jsonpath(json_response, 'search_key')

# delete
response = requests.delete(url)
response.status_code

# post

file = open('....json' 'r')
json_input = file.read()
request_json = json.loads(json_path)

response = requests.post(url, request_json)

# update
odczyt i parsowanie takie jak post  jedynie moetode zmiemiamy na `put`

response = requests.put(url, request_json)

```
