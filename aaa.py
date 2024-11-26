from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
from csv import reader

driver = webdriver.Edge()

driver.get("https://www.ranorex.com/web-testing-examples/vip/")

with open('MOCK_DATA.csv',newline='') as csvfile:
    info = reader(csvfile,delimiter=',', quotechar='|')
    for row in info:
        firstname = driver.find_element('id', 'FirstName')
        firstname.send_keys(row[0])
        lastname = driver.find_element('id', 'LastName')
        lastname.send_keys(row[1])
        if row[2].lower() == 'female':
            femaleSelect = driver.find_element(By.CSS_SELECTOR,'input[value=female]').click()
        else:
            maleSelect = driver.find_element(By.CSS_SELECTOR, 'input[value=male]').click()
        
        categoryElement = driver.find_element(By.ID, 'Category')
        category = Select(categoryElement)
        options = category.options
        selectedOption = category.all_selected_options

        match row[3]:
            case 'Others':
                category.select_by_value('Other')
            case 'Music':
                category.select_by_value('Music')
            case 'Movie':
                category.select_by_value('Movie')
            case 'Science':
                category.select_by_value('Science')
            case 'Sport':
                category.select_by_value('Sport')
            case 'Politics':
                category.select_by_value('Politics')


        addButton = driver.find_element('id', 'Add')
        addButton.click()

sleep(120)