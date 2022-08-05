import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(executable_path='./chromedriver.exe')

driver.get("https://www.facebook.com/")
DELAY = 10 # seconds

# Login
emailInput = driver.find_element(By.ID, "email")
emailInput.send_keys("programmer.cr.j@gmail.com")
passInput = driver.find_element(By.ID, "pass")
passInput.send_keys("fb.MSjmj1234")
loginBtn = driver.find_element(By.NAME, 'login')

loginBtn.click()

try:
    myElem = WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.ID, 'ssrb_root_start')))
except TimeoutException:
    print("Loading took too much time!")

# Group

driver.get("https://www.facebook.com/groups/484490482920762")




joinBtn = WebDriverWait(driver, DELAY).until(lambda d: d.find_elements(By.CSS_SELECTOR, 'span.a8c37x1j.ni8dbmo4.stjgntxs.l9j0dhe7.ltmttdrg.g0qnabr5'))[0]
if joinBtn.text == "Join Group":
    joinBtn.click()
    sleep(5)



eventsTab = WebDriverWait(driver, DELAY).until(lambda d: d.find_element(By.LINK_TEXT, 'Events'))

eventsTab.click()


createEvent = WebDriverWait(driver, DELAY).until(lambda d: d.find_element(By.LINK_TEXT, 'Create Event')) 
createEvent.click()


createEvent = WebDriverWait(driver, DELAY).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.oajrlxb2.gs1a9yip.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2.goun2846.ccm00jje.s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9.mg4g778l.pfnyh3mw.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.hpfvmrgz.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr.f1sip0of.du4w35lb.n00je7tq.arfg74bv.qs9ysxi8.k77z8yql.btwxx1t3.abiwlrkh.p8dawk7l.lzcic4wl.j83agx80.sn7ne77z.k4urcfbm'))) 
sleep(2)
ActionChains(driver).move_to_element(createEvent).click(createEvent).perform()
# createEvent.click()



eventNameInput = WebDriverWait(driver, DELAY).until(lambda d: d.find_element(By.CLASS_NAME, 'nfbje2wv'))
eventNameInput.send_keys("Test Event")


eventDateInput = WebDriverWait(driver, DELAY).until(lambda d: d.find_element(By.CSS_SELECTOR, 'input.oajrlxb2.f1sip0of.hidtqoto.e70eycc3.lzcic4wl.g5ia77u1.gcieejh5.bn081pho.humdl8nn.izx4hr6d.rq0escxv.oo9gr5id.jagab5yi.knj5qynh.fo6rh5oj.osnr6wyh.hv4rvrfc.dati1w0a.p0x8y401.k4urcfbm'))


for _ in range(20):
    eventDateInput.send_keys(Keys.BACK_SPACE)
eventDateInput.send_keys("10 Aug 2022")


eventTimeInput = WebDriverWait(driver, DELAY).until(lambda d: d.find_elements(By.CSS_SELECTOR, 'input.oajrlxb2.f1sip0of.hidtqoto.e70eycc3.lzcic4wl.g5ia77u1.gcieejh5.bn081pho.humdl8nn.izx4hr6d.rq0escxv.oo9gr5id.jagab5yi.knj5qynh.fo6rh5oj.osnr6wyh.hv4rvrfc.dati1w0a.p0x8y401.k4urcfbm'))[1]


for _ in range(20):
    eventTimeInput.send_keys(Keys.BACK_SPACE)
eventTimeInput.send_keys("20:34")



nextBtn = WebDriverWait(driver, DELAY).until(lambda d: d.find_elements(By.CSS_SELECTOR, "span.d2edcug0.hpfvmrgz.qv66sw1b.c1et5uql.lr9zc1uh.a8c37x1j.fe6kdd0r.mau55g9w.c8b282yb.keod5gw0.nxhoafnm.aigsh9s9.d3f4x2em.iv3no6db.gfeo3gy3.a3bd9o3v.lrazzd5p.bwm1u5wc"))[2]
# for i, b in enumerate(nextBtn):
#     print(i, b.text)
ActionChains(driver).move_to_element(nextBtn).click(nextBtn).perform()



location = WebDriverWait(driver, DELAY).until(lambda d: d.find_elements(By.CSS_SELECTOR, "span.d2edcug0.hpfvmrgz.qv66sw1b.c1et5uql.lr9zc1uh.a8c37x1j.fe6kdd0r.mau55g9w.c8b282yb.keod5gw0.nxhoafnm.aigsh9s9.d3f4x2em.mdeji52x.jagab5yi.g1cxx5fr.ekzkrbhg.oo9gr5id.hzawbc8m"))[2]
ActionChains(driver).move_to_element(location).click(location).perform()



linkInput = WebDriverWait(driver, DELAY).until(lambda d: d.find_element(By.CSS_SELECTOR, "input.oajrlxb2.f1sip0of.hidtqoto.e70eycc3.lzcic4wl.g5ia77u1.gcieejh5.bn081pho.humdl8nn.izx4hr6d.rq0escxv.oo9gr5id.qc3s4z1d.knj5qynh.fo6rh5oj.osnr6wyh.hv4rvrfc.dati1w0a.p0x8y401.k4urcfbm.iu8raji3.nfbje2wv")) 
ActionChains(driver).move_to_element(linkInput).send_keys_to_element(linkInput, "https://www.youtube.com/results?search_query=code+with+harry+python").perform()


nextBtn = WebDriverWait(driver, DELAY).until(lambda d: d.find_elements(By.CSS_SELECTOR, "span.d2edcug0.hpfvmrgz.qv66sw1b.c1et5uql.lr9zc1uh.a8c37x1j.fe6kdd0r.mau55g9w.c8b282yb.keod5gw0.nxhoafnm.aigsh9s9.d3f4x2em.iv3no6db.gfeo3gy3.a3bd9o3v.lrazzd5p.bwm1u5wc"))[2]
ActionChains(driver).move_to_element(nextBtn).click(nextBtn).perform()


descriptionInput = WebDriverWait(driver, DELAY).until(lambda d: d.find_element(By.CSS_SELECTOR, "textarea.oajrlxb2.f1sip0of.hidtqoto.g5ia77u1.gcieejh5.bn081pho.humdl8nn.izx4hr6d.rq0escxv.oo9gr5id.j83agx80.jagab5yi.knj5qynh.fo6rh5oj.oud54xpy.l9qdfxac.lzcic4wl.ni8dbmo4.stjgntxs.hv4rvrfc.dati1w0a.ieid39z1.k4urcfbm")) 
ActionChains(driver).move_to_element(descriptionInput).send_keys_to_element(descriptionInput, "test desc").perform()



nextBtn = WebDriverWait(driver, DELAY).until(lambda d: d.find_elements(By.CSS_SELECTOR, "span.d2edcug0.hpfvmrgz.qv66sw1b.c1et5uql.lr9zc1uh.a8c37x1j.fe6kdd0r.mau55g9w.c8b282yb.keod5gw0.nxhoafnm.aigsh9s9.d3f4x2em.iv3no6db.gfeo3gy3.a3bd9o3v.lrazzd5p.bwm1u5wc"))[2]
ActionChains(driver).move_to_element(nextBtn).click(nextBtn).perform()

nextBtn = WebDriverWait(driver, DELAY).until(lambda d: d.find_elements(By.CSS_SELECTOR, "span.d2edcug0.hpfvmrgz.qv66sw1b.c1et5uql.lr9zc1uh.a8c37x1j.fe6kdd0r.mau55g9w.c8b282yb.keod5gw0.nxhoafnm.aigsh9s9.d3f4x2em.iv3no6db.gfeo3gy3.a3bd9o3v.lrazzd5p.bwm1u5wc"))[2]
ActionChains(driver).move_to_element(nextBtn).click(nextBtn).perform()



sleep(10)
createEvent = WebDriverWait(driver, DELAY).until(lambda d: d.find_element(By.LINK_TEXT, 'Edit')) 
createEvent.click()

sleep(1)
nextBtn = WebDriverWait(driver, DELAY).until(lambda d: d.find_elements(By.CSS_SELECTOR, "div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.d2edcug0.hpfvmrgz.rj1gh0hx.buofh1pr.g5gj957u.ph5uu5jm.b3onmgus.e5nlhep0.ecm0bbzt"))[0]
# for i, n in enumerate(nextBtn):
#     print(i, n.text)
    
# exit()
ActionChains(driver).move_to_element(nextBtn).click(nextBtn).perform()

nextBtn = WebDriverWait(driver, DELAY).until(lambda d: d.find_elements(By.CSS_SELECTOR, "div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.d2edcug0.hpfvmrgz.rj1gh0hx.buofh1pr.g5gj957u.ph5uu5jm.b3onmgus.e5nlhep0.ecm0bbzt"))[0]
ActionChains(driver).move_to_element(nextBtn).click(nextBtn).perform()


nextBtn = WebDriverWait(driver, DELAY).until(lambda d: d.find_elements(By.CSS_SELECTOR, "div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.d2edcug0.hpfvmrgz.rj1gh0hx.buofh1pr.g5gj957u.ph5uu5jm.b3onmgus.e5nlhep0.ecm0bbzt"))[0]
ActionChains(driver).move_to_element(nextBtn).click(nextBtn).perform()



imageDel = WebDriverWait(driver, DELAY).until(lambda d: d.find_element(By.CSS_SELECTOR, ".j83agx80.b5fwa0m2.pmk7jnqg.plgsh5y4")) 
ActionChains(driver).move_to_element(imageDel).click(imageDel).perform()

imageInp = WebDriverWait(driver, DELAY).until(lambda d: d.find_element(By.CSS_SELECTOR, "input.mkhogb32"))
imageInp.send_keys(os.getcwd() + "\\images\\test event2.jpg")


# driver.implicitly_wait(10)
sleep(10)
nextBtn = WebDriverWait(driver, DELAY).until(lambda d: d.find_elements(By.CSS_SELECTOR, "div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.d2edcug0.hpfvmrgz.rj1gh0hx.buofh1pr.g5gj957u.ph5uu5jm.b3onmgus.e5nlhep0.ecm0bbzt"))[0]
ActionChains(driver).move_to_element(nextBtn).click(nextBtn).perform()

