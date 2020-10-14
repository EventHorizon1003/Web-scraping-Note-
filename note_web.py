# Note about Web scraping
# Several modules are used in this note:
# 1) webbrowser: open a browser to a specific page
# 2) Requests: Downloads file and web pages from the Internet
# 3) Beautiful Soup: Parses HTML,
# 4) Selenium : launches and control a web browser. It also able to fill ....
#               forms and simulate mouse clicks in this browser
#--------------------------------------------------------------------

import webbrowser
#----------------------------------------------------------------
# Open a browser to a specific page -> webbrowser.open("<URL>")
# See the maplt.py
#---------------------------------------------------------------

import requests
#--------------------------------------------------------------------------
#1) Downloading files from the web -> requests / urllib2
#   var.text
#   eg: var = requests.get("<URL>") -> Return a response object
#   eg: type(var) -> type of data
#   eg: var.status_code == requests.codes.ok -> "OK" in HTTP protocol is 200
#   eg: len(var.text)
#   eg: print(res.text)
#   noteFunction1
#2) raise_for_status() to see the the status of ResObj
#   this function is similar to the var.status_code == requests.codes.ok
#   It can ensure that a program halt if a bad download occur
#   noteFunction2()
#3) Saving downloaded files to the hard drive -> open() / write()
#   *** the file must fill in write binary mode by passing 'wb' on the open()
#   eg: obj = open('<name>','wb')
#   eg: use for loop to limit the size of the file
#   noteFunction3()
#-------------------------------------------------------------------------

import bs4
#--------------------------------------------------------------------------
#1) Parse HTML -> Beautiful Soup (bs4)
#   eg: obj = bs4.BeautifulSoup(<-.text>,'html.parser')
#2) Finding an element from a Beautiful Soup object -> select()
#   Examples of Css selectors :
#   soup.select('div') - all elements named <div>
#   soup.select('#author') - The element with an id attribute of author
#   soup.select('.notice') - all elements that use a Css class attribute named notice
#   soup.select('div span') - all elements named <span> that are within an element named <div>
#   soup.select('div >span') - similarly with the 'div span' ; but with no other element in between
#   soup.select('input[name]') - all <input> that have a name attribute with any value
#   soup.select('input[type='buttton']') - all elements named <input> that have an attribute named type with value button
#       select() will return a list of Tag objects : list will contain one Tag object for every match
#       tag values can pass to the str() to show the HTML tags
#   *** To get rid of the warning pass the "html.parser" in the second argument to the function ***
#   See noteFunction5() / noteFunction6()
#   str(SoupObj) -> show the html tag
#   SoupObj.getText() -> show the text of the object
#------------------------------------------------------------------------------

import selenium
#-------------------------------------------------------------------------------
# Controlling the browser -> selenium module
# For example: clicking the links , filling the login information
# The way of importing selenium is :
#   from selenium import webdriver
#   browser = webdriver.Firefox() # return the object
#   browser.get（address） # Website
#   Obj = browser.find_element_by_link_text(<elem>)
#       Obj.find_element_by_id(<elem>)
#   Obj.click() # click the link
#       Obj.send_keys("") # send the keystrokes to the webPage
#       Obj.submit()
#   Sending special keys
#       from selenium.webdriver.common.keys import Keys
#       Obj from the (browser.find_element_by____)
#       Obj.send_keys(Keys.<>)
#   Clicking Browser Buttons
#    eg:browser.quit()
#       browser.refresh()
#       browser.forward()
#       browser.back()


def noteFunction1() :
    a = 'http://www.youtube.com'
    b = 'http://www.face2bofok.com'
    RObj = requests.get(a)
    print(RObj.status_code) # True mean 200 == 'ok'
    print(RObj.status_code == requests.codes.ok)
    type(RObj)
    len(RObj.text)
    print(RObj.text)

def noteFunction2() :
    b = 'http://www.favefo.com'
    c = 'http://inventwithpython.com/page_that_does_not_exist'
    d = 'http://www.youtube.com'
    res = requests.get(d)
    try :
        res.raise_for_status()
        print(res.raise_for_status()) # print None
        print(res.status_code)  # print 200 mean 'ok'
    except Exception as err :
        print("There was a problem : %s" %(err))

def noteFunction3() :
    a = 'http://www.youtube.com'
    res = requests.get(a)
    res.raise_for_status()
    fileObj = open('youtube.txt','wb') # write in binary format
    for chunk in res.iter_content(100000): # limit to 100000 bytes
        fileObj.write(chunk)

def noteFunction4() :
    res = requests.get("http://nostarch.com")
    res.raise_for_status()
    noStarchSoup = bs4.BeautifulSoup(res.text) # return a beautiful object
    print(type(noStarchSoup))

def noteFunction5() :
    a = 'C:\\Users\\ACER\\Desktop\\Python\\Revisiom\\example.html'
    exampleFile = open(a)
    exampleSoup = bs4.BeautifulSoup(exampleFile.read()) # return object
    elems = exampleSoup.select('#author') # return the list of tag object in var
    print(type(elems)) # type : tag
    print(elems[0].getText()) # the author
    print(str(elems[0])) # convert to the HTML
    print(elems[0].attrs) # assign the class ="<name>" in the list : { 'class/id' : ['name']}


def noteFunction6() :

    a = 'C:\\Users\\ACER\\Desktop\\Python\\Revisiom\\example.html'
    exampleFile = open(a)
    exampleSoup = bs4.BeautifulSoup(exampleFile.read(),"html.parser")  # return object
    pElems = exampleSoup.select('p')
    print(str(pElems[0])) # print the html tag
    print(pElems[0].getText()) # print the first element in text
    print(pElems[1].getText())
    print(pElems[2].getText())
    for l in range(0,3):
        print(pElems[l].attrs) # print the list of the attribute
    for l in range(0,3):
        print(str(pElems[l])) # print the elements
import selenium
def noteFunction7() :
    from selenium import webdriver
    browser = webdriver.Firefox()
    print(type(browser))  # reveal the data type
    browser.get("http://inventwithpython.com")
    try:
        elem = browser.find_elements_by_link_text("Read It Online")
        print("Found <%s> element with that class name!" %(elem.tag_name))
        elem.click()
    except :
        print("Was not able to find an element with that name.")


def fun(n):
    if n == '1' :
        noteFunction1()
    elif n == '2' :
        noteFunction2()
    elif n == '3' :
        noteFunction3()
    elif n == '4' :
        noteFunction4()
    elif n == '5' :
        noteFunction5()
    elif n == '6' :
        noteFunction6()
    elif n == '7' :
        noteFunction7()

while True :
    print("\nWhat u wanna me to show ? ")
    a = input()
    fun(a)