import sys
from selenium import webdriver
import os
contestnumber = sys.argv[1]
driver = webdriver.Firefox(executable_path=".\\geckodriver.exe")
driver.get(f"https://codeforces.com/contest/{contestnumber}")
pb_table = driver.find_elements_by_class_name("problems")
pburl_dic = {}
pb_a = pb_table[0].find_elements_by_tag_name("a")
for i in range(len(pb_a)) :
    pbcode = pb_a[i].text
    pburl = pb_a[i].get_attribute('href')
    if (f"https://codeforces.com/contest/{contestnumber}/problem/{pbcode}"==pburl) :
        pburl_dic[pbcode]=pburl    
for key in pburl_dic :
    driver.get(pburl_dic[key])
    try :
        os.makedirs(f".\\{contestnumber}\\{key}" , exist_ok=True)
    except OSError as error :
        pass
    element = driver.find_element_by_class_name("problem-statement")
    element.screenshot(f'.\\{contestnumber}\\{key}\\problem.png')
    inp = driver.find_elements_by_class_name("input")
    otp = driver.find_elements_by_class_name("output")
    for j in range(len(inp)) :
        inpt =  open(f".\\{contestnumber}\\{key}\\input{j+1}.txt" , 'w')
        inpt.write(inp[j].find_element_by_tag_name('pre').text)
        otpt = open(f".\\{contestnumber}\\{key}\\output{j+1}.txt" , 'w')
        otpt.write(otp[j].find_element_by_tag_name('pre').text)
        inpt.close()
        otpt.close() 
driver.close()     