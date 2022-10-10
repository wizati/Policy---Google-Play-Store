import time

from selenium import webdriver
from selenium.webdriver.common.by import By
#Provide two values and click calculate button(auto filling) (3 marks)
#Clear the values after performing each computation(2 mark)
#Come back to the Home page using the back command(3 marks)
#Use forward to go to https://www.mathsisfun.com/(2 marks)
#Use To command to go to https://testsheepnz.github.io/BasicCalculator.html(2 marks)
#Refresh the Browser using Refresh command (1 mark)
#Use TestNG(2 marks)
path = "c:\chromedriver.exe"
driver = webdriver.Chrome(path)

def setup(url):
    driver.get(url)

def EnterValues(val1,val2):
    FirstNum = driver.find_element(By.ID,"number1Field")
    SecondNum = driver.find_element(By.ID,"number2Field")

    driver.execute_script("arguments[0].setAttribute('value',arguments[1])",FirstNum,val1)
    driver.execute_script("arguments[0].setAttribute('value',arguments[1])",SecondNum,val2)

def ClickCalculate():
    login = driver.find_element(By.ID,"calculateButton")
    login.click()

def Clear():
    driver.execute_script("arguments[0].setAttribute('value',arguments[1])",FirstNum,"")
    driver.execute_script("arguments[0].setAttribute('value',arguments[1])",SecondNum,"")

def backpage():
    driver.back()
def forwardpage():
    driver.forward()
setup("https://testsheepnz.github.io/BasicCalculator.html")
setup("https://www.mathsisfun.com/")
input()
print("Backward")
backpage()
input()
print("Forward")
forwardpage()
input()
print("Refresh")
driver.refresh()
input()
setup("https://testsheepnz.github.io/BasicCalculator.html")
input()
print("Entering Values")

EnterValues(10,10)
ClickCalculate()
input()
Clear()
print("Clear")


