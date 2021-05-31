from selenium import webdriver
import time 
import sys

driver = webdriver.Firefox()
pincode = str(sys.argv[1])
dose = int(sys.argv[2])
age = int(sys.argv[3])
print("Fetching results...")

if dose == 1:
    if age in range(18, 45):
        path = "https://www.vaccinateme.in/covid/list?dose=dose_1&min_age_limit=18&pincode="+pincode+"&type=pincode"
    elif age in range(45, 100):
        path = "https://www.vaccinateme.in/covid/list?dose=dose_1&min_age_limit=45&pincode="+pincode+"&type=pincode"
elif dose == 2:
    if age in range(18, 45):
        path = "https://www.vaccinateme.in/covid/list?dose=dose_2&min_age_limit=18&pincode="+pincode+"&type=pincode"
    elif age in range(45, 100):
        path = "https://www.vaccinateme.in/covid/list?dose=dose_2&min_age_limit=45&pincode="+pincode+"&type=pincode"


driver.get(path)
driver.set_window_size(1024, 768)
time.sleep(5)
print("\nFollowing are the slots...\n")
found = 0
try:
    for i in range(1,10):
        datePath = "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[4]/div["+str(i)+"]/div[1]/span"
        countPath = "/html/body/div[1]/div/div/div/div/div[2]/div/div/div[4]/div["+str(i)+"]/div[2]/span[1]"
        dateB = driver.find_element_by_xpath(datePath).text
        countB = driver.find_element_by_xpath(countPath).text
        print("Date:", dateB, "=>", countB)
        found = 1
except Exception as e:
    if found == 1:
        print()
    else:
        print("No slots available!!")

driver.quit()
