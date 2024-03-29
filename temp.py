from threading import Thread
from PyQt6 import QtCore, QtGui, QtWidgets
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from datetime import datetime, timedelta

def run():
    driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    DELAY = 10
    
    accountsData = pd.read_csv("./accounts.csv")
    failedAccounts = pd.DataFrame([])
    groupsEventCreated = pd.DataFrame([])
    groupsData = pd.read_csv("./groups-data.csv")
    
    for i, accountsRow in accountsData.iterrows():
        email = accountsRow[0]
        password = accountsRow[1]
        
        driver.get("https://www.facebook.com/")
        # Login
        emailInput = driver.find_element(By.ID, "email")
        emailInput.send_keys(email)
        passInput = driver.find_element(By.ID, "pass")
        passInput.send_keys(password)
        loginBtn = driver.find_element(By.NAME, 'login')

        loginBtn.click()

        try:
            myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span')))
        except TimeoutException:
            failedAccounts = failedAccounts.append(accountsRow)
            accountsData.drop(i, inplace=True)
            driver.delete_all_cookies()
            continue

        for i, groupRow in groupsData.iterrows():
            groupLink = groupRow[0]
            driver.get(groupLink)
            try:
                joinBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/span/span')))
                print(joinBtn.text)
                if joinBtn.text.lower() == "join group":
                    joinBtn.click()
                    sleep(5)
            except TimeoutException as e:
                print(e)
                pass

            eventsTab = WebDriverWait(driver, DELAY).until(lambda d: d.find_element(By.LINK_TEXT, 'Events'))

            eventsTab.click()


            createEvent = WebDriverWait(driver, DELAY).until(lambda d: d.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div/div/div/div[1]/span/div/div[2]/div/div[2]/div/a/div/div[1]/div/span/span')) 
            createEvent.click()


            createEvent = WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[1]'))) 
            sleep(2)
            ActionChains(driver).move_to_element(createEvent).click(createEvent).perform()
            # createEvent.click()



            eventNameInput = WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[3]/div[1]/div[2]/div/div[2]/div[1]/div/label/div/div/input')))

            eventNameInput.send_keys("ev name")


            eventDateInput = WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[3]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div/div[1]/div/label/div/div[2]/div/input')))

            # if(self.eventDate.toPlainText() != ""):
            #     for _ in range(20):
            #         eventDateInput.send_keys(Keys.BACK_SPACE)
            #     eventDateInput.send_keys(self.eventDate.toPlainText())


            # eventTimeInput = WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[3]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div/label/div/div/div/input')))

            # if():
            #     for _ in range(20):
            #         eventTimeInput.send_keys(Keys.BACK_SPACE)
            #     eventTimeInput.send_keys(self.eventTime.toPlainText())
            # else:
            #     for _ in range(20):
            #         eventTimeInput.send_keys(Keys.BACK_SPACE)
            #     eventTimeInput.send_keys(str(datetime.strftime(datetime.now()+ timedelta(hours=1), "%H:%M")))
                


            nextBtn = WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[5]/div/div/div[2]/div/div/div[1]/div/span ")))

            # for i, b in enumerate(nextBtn):
            #     print(i, b.text)
            ActionChains(driver).move_to_element(nextBtn).click(nextBtn).perform()



            for i in range(5):
                location = WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[3]/div[1]/div[2]/div/div[{i+1}]/div/div/div[1]/div[2]/div[1]/div/div/div[1]/span")))
                if(location.text == "External link"):
                    ActionChains(driver).move_to_element(location).click(location).perform()
                    break
                



            linkInput = WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.oajrlxb2.f1sip0of.hidtqoto.e70eycc3.lzcic4wl.g5ia77u1.gcieejh5.bn081pho.humdl8nn.izx4hr6d.rq0escxv.oo9gr5id.qc3s4z1d.knj5qynh.fo6rh5oj.osnr6wyh.hv4rvrfc.dati1w0a.p0x8y401.k4urcfbm.iu8raji3.nfbje2wv"))) 
            
            ActionChains(driver).move_to_element(linkInput).send_keys_to_element(linkInput, "https://www.dede.com/").perform()

            nextBtn = WebDriverWait(driver, DELAY).until(lambda d: d.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[5]/div/div/div[2]/div/div/div[1]/div/span "))

            ActionChains(driver).move_to_element(nextBtn).click(nextBtn).perform()


            descriptionInput = WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[3]/div[1]/div[2]/div/div/div/label/div/div/textarea"))) 
            ActionChains(driver).move_to_element(descriptionInput).send_keys_to_element(descriptionInput, "desc").perform()


            nextBtn = WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[5]/div/div/div[2]/div/div/div[1]/div/span")))

            ActionChains(driver).move_to_element(nextBtn).click(nextBtn).perform()
            
            
            nextBtn = WebDriverWait(driver, DELAY).until(lambda d: d.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[5]/div/div/div[2]/div/div/div[1]/div/span "))


            ActionChains(driver).move_to_element(nextBtn).click(nextBtn).perform()



            sleep(10)
            createEvent = WebDriverWait(driver, DELAY).until(lambda d: d.find_element(By.LINK_TEXT, 'Edit')) 
            createEvent.click()

            sleep(1)
            nextBtn = WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[5]/div/div/div/div/div")))
            # for i, n in enumerate(nextBtn):
            #     print(i, n.text)
                
            # exit()
            ActionChains(driver).move_to_element(nextBtn).click(nextBtn).perform()
            
            nextBtn = WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[5]/div/div/div[2]/div/div")))
            ActionChains(driver).move_to_element(nextBtn).click(nextBtn).perform()

            nextBtn = WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[5]/div/div/div[2]/div/div")))

            ActionChains(driver).move_to_element(nextBtn).click(nextBtn).perform()



            imageDel = WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div"))) 
            ActionChains(driver).move_to_element(imageDel).click(imageDel).perform()

            imageInp = WebDriverWait(driver, DELAY).until(lambda d: d.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div[1]/input"))
            imageInp.send_keys('D:\Main\code\testing\python\test event2.jpg')


            sleep(10)
            updateBtn = WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[5]/div/div/div[2]/div/div")))

            ActionChains(driver).move_to_element(updateBtn).click(updateBtn).perform()
            groupsEventCreated = groupsEventCreated.append(groupRow)
            
        
        
        logout1 = WebDriverWait(driver, DELAY).until(lambda d: d.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/span/div/div[1]"))
        ActionChains(driver).move_to_element(logout1).click(logout1).perform()
        
        logout2 = WebDriverWait(driver, DELAY).until(lambda d: d.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[5]/div/div[1]"))
        ActionChains(driver).move_to_element(logout2).click(logout2).perform()


    # driver.quit()
    
    # currentTime = str(datetime.strftime(datetime.now(), "%Y-%m-%d__%H-%M-%S"))
    # os.makedirs(currentTime)
    # accountsData.to_csv(f'{currentTime}/attempted_accounts.csv', index = False, header=True, encoding='utf-8') 
    # failedAccounts.to_csv(f"{currentTime}/failed_accounts.csv", index = False,header=True, encoding='utf-8')
    # groupsData.to_csv(f'{currentTime}/attemptedGroups.csv', index = False, header=True, encoding='utf-8') 
    # groupsEventCreated.to_csv(f'{currentTime}/groupsEventCreated.csv', index = False, header=True, encoding='utf-8') 

# Thread(target=run).start()
run()