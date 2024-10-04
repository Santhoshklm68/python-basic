# a=[1,2,3,4]
# x=a[1]
# print(type(a))
# print(a)

# # a=(1,2,3,5,4,4)
# # print(a)

# # a={"apple", "banana", "cherry"}
# # x=a[1]
# # print(a)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 2020
# }
# thisdict["year"]=2000#change item
# thisdict["speed"]="100kmph"

# print(thisdict["brand"])


# # x=thisdict["model"]
# thisdict.pop("year")
# print(thisdict)
# # print(x)


#--------------------------------------------------------------------------------#
# a="  Hi hello  "
# print(a)
# import csv
# with open('data.csv.csv', newline='') as csvfile:
#     writer = csv.reader(csvfile)
#     for a in writer:
#         print(a)

# import math

# ans=math.sqrt(55)
# print(ans)

# a=[1,2,3,4,5,6,4]
# b=a[1:4]
# print(b)

# from datetime import datetime
# a= datetime.now()
# print(a)

# a="  hello world  "
# print(a.strip())

# for i in range(0,10):
#     print(i)

# 





  
#   if i ==4:
#    continue
  # print(i)

# a=["a","b","c"]
# for i in a:
#     print(i)

# a=[1,2,4,5,7,8]


# for i in a:
#     if i % 2 !=0:
        
#      print(i)

#------------------GLOBAL SCOPE-----------------
# x = "awesome"

# def myfunc():
#   print("Python is " + x)

# myfunc()

# def myfunc():
#   global x #using global keyword
#   x = "fantastic"

# myfunc()

# print("Python is " + x)
# def fun():
#   return x
# print(x)
# fun()

#---------------------LAMBDA FUNCTION -----------------------------
# a= lambda x,y:x+y
# print(a(2,5))
# try:
#   a=5
#   b="h"
#   c=a+b
#   print(c)
# except Exception as e:
#   print("not mentioned",e)

# class Hi:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age

#     def display(self):
#         print(f"iam: {self.name}, my age: {self.age}")

# ans=Hi("santhosh", 26)
# ans.display()


#=--------------------WEB SCRAPING-------------------------############
# import requests
# from bs4 import BeautifulSoup

# # URL of the page you want to scrape
# url = "https://worldstories.org.uk/"

# # Send an HTTP request to the URL
# response = requests.get(url)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse the HTML content using BeautifulSoup
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     # Example: Find all <h1> tags (headers) and print them
#     # for header in soup.find_all('h1'):
#     #     print(header.text)
    
#     # # Example: Find all links on the page and print them
#     for link in soup.find_all('a'):
#         print(link.get('href'))
# else:
#     print("Failed to retrieve the page.")

#----------------------------CHATBOT-------------------------------############
import nltk
from nltk.chat.util import Chat, reflections

# Pairs of patterns and responses for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot!",]
    ],
    [
        r"how are you?",
        ["I'm doing great! How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "No problem.",]
    ],
    [
        r"I (.*) (good|well|okay|ok)",
        ["That's great to hear!",]
    ],
    [
        r"(hi|hello|hey)",
        ["Hello!", "Hi there!",]
    ],
    [
        r"quit",
        ["Goodbye! It was nice talking to you.",]
    ],
]

# Initialize the Chatbot
chatbot = Chat(pairs, reflections)

# Start conversation
print("Hi, I'm your chatbot! Type 'quit' to exit.")
chatbot.converse()

# import re


# # b=re.search(r"ye.*san", a)
# b= re.findall("a",a)

# print(b)


# from PyPDF2 import PdfReader

# # Open the PDF file
# with open('tesla.pdf', 'rb') as file:
#     reader = PdfReader(file)
    
#     # Loop through each page and extract text
#     for page_num in range(len(reader.pages)):
#         page = reader.pages[page_num]
#         text = page.extract_text()
#         print(f"--- Page {page_num + 1} ---")
#         print(text)
# a=8
# b=4
# print(a/b)
# i=0
# while(i%3 == 0):
#     i+=1
#     print(i)

# a={
#     "name":"bmw",
#     "model":"6series",
#     "year":2006
# }

# a["model"]=("5series")
# a["price"]=(100000)
# print(a)

# a=[1,2,3,4,5]
# for i in a:
#     if i ==3:
#         continue
#     print(i)

# else:
#     print("loop stopped")

# i=1
# while(i<6):
#     i+=1
#     if i==3:
#         continue
#     print(i)
# else:
#     print("loop stopped")

# i= 1
# while(i<10):
#     i+=1
#     if i==5:
#         continue
#     print(i)
    

# import csv

# with open('data.csv.csv', newline='') as csvfile:
#     read  = csv.reader(csvfile)
#     for i in read:
#         print(i)

# i=0
# while(i<10):
#     print(i)
    
#     i+=1

# else:
#     print("loop stopped")
# import os
# a = open("sample.txt","w")
# b = a.write("varun")
# print(b)


    