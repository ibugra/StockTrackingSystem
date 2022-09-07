from cgitb import text
import locale
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from turtle import back, color, width
import pymysql 
from tkcalendar import *
from tkcalendar import DateEntry
from datetime import datetime


#PRODUCT FUNCTIONS
def insertProduct(ID, name, amount, category):


    #connected to the db
    sqlCon = pymysql.connect(host="localhost", user="root",password="3859",database="dbstock")
    cur = sqlCon.cursor()
    
    cur.execute("INSERT INTO products values(?,?,?,?)"(ID,name,amount,category))
    sqlCon.commit()
    sqlCon.close()


    pass

def updateProduct():
    pass
def deleteProduct():
    pass

def selectProduct():
    pass


#PRODUCT DETAIL FUNCTIONS
def insertProductDetail():
    pass
def updateProductDetail():
    pass
def deleteProductDetail():
    pass

def selectProductDetail():
    pass

#INVOICE FUNCTIONS
def insertInvoice():
    pass
def updateInvoice():
    pass
def deleteInvoice():
    pass

def selectInvoice():
    pass


#CUSTOMER FUNCTIONS

def insertCustomer():
    pass
def updateCustomer():
    pass
def deleteCustomer():
    pass

def selectCustomer():
    pass
#ADDRESS FUNCTIONS
def insertAddress():
    pass
def updateAddress():
    pass
def deleteAddress():
    pass

def selectAddress():
    pass