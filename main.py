from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkcalendar import *
from tkcalendar import DateEntry
from datetime import datetime
from Backend.function import insertProduct 

class stockTracking:
    def __init__(self, root):
        self.root = root
        titleSpace = " "
        self.root.title(80 * titleSpace + "STOCK TRACKING SYSTEM ORTA ANADOLU")
        self.root.geometry("1300x700+100+0")
        self.root.resizable(width=False, height=False)
        root.iconbitmap("orta.ico")

        #defining variables
        product_ID = StringVar()
        product_name = StringVar()
        product_amount = StringVar()
        product_category = StringVar()
        
        product_detail_ID = StringVar()
        product_detail_date = StringVar()
        product_detail_product_ID = StringVar()
        product_detail_invoice_ID = StringVar()

        invoice_ID = StringVar()
        invoice_customer_ID = StringVar()
        invoice_date = StringVar()

        customer_ID = StringVar()
        customer_name = StringVar()
        customer_tel = StringVar()
        customer_address_ID = StringVar()

        address_customer_ID = StringVar()
        address_city = StringVar()
        address_country = StringVar()
        addres_district = StringVar()
        address_open = StringVar()
        address_post_code = StringVar()

        #create a notebook 
        notebook = ttk.Notebook(root)
        notebook.pack(pady=0, expand=True)

        #menu
        my_menu = Menu(root)
        root.config(menu=my_menu)

        def our_command():
            pass

        file_menu = Menu(my_menu)
        my_menu.add_cascade(label ="File", menu=file_menu)
        file_menu.add_command(label ="New...", command=our_command)
        #############################

        #Frames
        #Home Page Frame
        MainFrame = Frame(notebook, bd=10, width=770, height=700, relief=RIDGE, bg='#40739f')
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=7, width=770, height=100, relief=RIDGE)
        TitleFrame.grid(row=0, column=0)
        
        TopFrame = Frame(MainFrame, bd=5, width=770, height=500, relief=RIDGE)
        TopFrame.grid(row=1, column=0)

        #Title Frame Title
        self.lbltitle = Label(TitleFrame, font=('VERDANA', 26, 'bold'), text="STOCK TRACKING SYSTEM", bd=7)
        self.lbltitle.grid(row=0, column=0, padx=132)

        #self.btnInsert=Button(MainFrame,font=('verdana',16,'bold'),text="Insert",bd=4,pady=1,padx=20,width=5,height=2, command=insertProduct(1,"name",1,"name")).grid(row=0,column=0,padx=1)


        
        #All Information
        scroll_y = Scrollbar(TopFrame, orient=VERTICAL)
        scroll_x = Scrollbar(TopFrame, orient=HORIZONTAL)

        self.all_records = ttk.Treeview(TopFrame,height=6,
                    columns=("product_name","product_amount","product_category","product_detail_date","customer_name","customer_tel","invoice_date","address_country","address_city","address_district","address_open","address_post_code"),yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
                    
        
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.pack(side=BOTTOM, fill=X)

        self.all_records.heading("product_name", text="Product Name")
        self.all_records.heading("product_amount", text="Amount")
        self.all_records.heading("product_category", text="Category")
        self.all_records.heading("product_detail_date", text="Product Date")
        self.all_records.heading("customer_name", text="Customer Name")
        self.all_records.heading("customer_tel", text="Customer Tel")
        self.all_records.heading("invoice_date", text="Invoice Date")
        self.all_records.heading("address_country", text="Country")
        self.all_records.heading("address_city", text="City")
        self.all_records.heading("address_district", text="District")
        self.all_records.heading("address_open", text="Open Address")
        self.all_records.heading("address_post_code", text="Post Code")

        self.all_records['show'] = 'headings'

        self.all_records.column("product_name", width=100)
        self.all_records.column("product_amount", width=100)
        self.all_records.column("product_category", width=100)
        self.all_records.column("product_detail_date", width=100)
        self.all_records.column("customer_name", width=100)
        self.all_records.column("customer_tel", width=100)
        self.all_records.column("invoice_date", width=100)
        self.all_records.column("address_country", width=100)
        self.all_records.column("address_city", width=100)
        self.all_records.column("address_district", width=100)
        self.all_records.column("address_open", width=100)
        self.all_records.column("address_post_code", width=100)

        self.all_records.pack(fill=BOTH, expand=1)
        
        #Frames2
        #Products
        MainFrame2 = Frame(notebook, bd=10, width=770, height=700, relief=RIDGE, bg='#40739f')
        MainFrame2.grid()
        
        TopFrame2 = Frame(MainFrame2, bd=5, width=770, height=500, relief=RIDGE)
        TopFrame2.grid(row=1, column=0)

        RightFrame12 = Frame(TopFrame2, bd=5, width=100, height=400, bg='#40739f', relief=RIDGE)
        RightFrame12.pack(side=RIGHT)
        RightFrame12a = Frame(RightFrame12, bd=5, width=90, height=300, padx=2, pady=2, relief=RIDGE)
        RightFrame12a.pack(side=TOP)

        self.btnInsert=Button(RightFrame12a,font=('verdana',16,'bold'),text="Insert",bd=4,pady=1,padx=20,width=5,height=2).grid(row=0,column=0,padx=1)
        self.btnUpdate=Button(RightFrame12a,font=('verdana',16,'bold'),text="Update",bd=4,pady=1,padx=20,width=5,height=2).grid(row=1,column=0,padx=1)
        self.btnDelete=Button(RightFrame12a,font=('verdana',16,'bold'),text="Display",bd=4,pady=1,padx=20,width=5,height=2).grid(row=2,column=0,padx=1)
        self.btnSearch=Button(RightFrame12a,font=('verdana',16,'bold'),text="Search",bd=4,pady=1,padx=20,width=5,height=2).grid(row=3,column=0,padx=1)
        self.btnReset=Button(RightFrame12a,font=('verdana',16,'bold'),text="Reset",bd=4,pady=1,padx=20,width=5,height=2).grid(row=4,column=0,padx=1)
        self.btnExit=Button(RightFrame12a,font=('verdana',16,'bold'),text="Exit",bd=4,pady=1,padx=20,width=5,height=2).grid(row=5,column=0,padx=1)

        #Product Table
        scroll_y_product = Scrollbar(TopFrame2, orient=VERTICAL)
        scroll_x_product = Scrollbar(TopFrame2, orient=HORIZONTAL)

        self.product_records = ttk.Treeview(TopFrame2,height=6,
                    columns=("product_ID","product_name","product_amount","product_category"),yscrollcommand=scroll_y_product.set, xscrollcommand=scroll_x_product.set)
                    
        
        scroll_y_product.pack(side=RIGHT, fill=Y)
        scroll_x_product.pack(side=BOTTOM, fill=X)

        self.product_records.heading("product_ID", text="Product ID")
        self.product_records.heading("product_name", text="Name")
        self.product_records.heading("product_amount", text="Amount")
        self.product_records.heading("product_category", text="Category")


        self.product_records['show'] = 'headings'

        self.product_records.column("product_ID", width=100)
        self.product_records.column("product_name", width=100)
        self.product_records.column("product_amount", width=100)
        self.product_records.column("product_category", width=100)

        self.product_records.pack(fill=BOTH, expand=1)


        #Frames3
        #Product Details
        MainFrame3 = Frame(notebook, bd=10, width=770, height=700, relief=RIDGE, bg='#40739f')
        MainFrame3.grid()
        
        TopFrame3 = Frame(MainFrame3, bd=5, width=770, height=500, relief=RIDGE)
        TopFrame3.grid(row=1, column=0)

        RightFrame13 = Frame(TopFrame3, bd=5, width=100, height=400, bg='#40739f', relief=RIDGE)
        RightFrame13.pack(side=RIGHT)
        RightFrame13a = Frame(RightFrame13, bd=5, width=90, height=300, padx=2, pady=2, relief=RIDGE)
        RightFrame13a.pack(side=TOP)

        self.btnInsert=Button(RightFrame13a,font=('verdana',16,'bold'),text="Insert",bd=4,pady=1,padx=20,width=5,height=2).grid(row=0,column=0,padx=1)
        self.btnUpdate=Button(RightFrame13a,font=('verdana',16,'bold'),text="Update",bd=4,pady=1,padx=20,width=5,height=2).grid(row=1,column=0,padx=1)
        self.btnDelete=Button(RightFrame13a,font=('verdana',16,'bold'),text="Display",bd=4,pady=1,padx=20,width=5,height=2).grid(row=2,column=0,padx=1)
        self.btnSearch=Button(RightFrame13a,font=('verdana',16,'bold'),text="Search",bd=4,pady=1,padx=20,width=5,height=2).grid(row=3,column=0,padx=1)
        self.btnReset=Button(RightFrame13a,font=('verdana',16,'bold'),text="Reset",bd=4,pady=1,padx=20,width=5,height=2).grid(row=4,column=0,padx=1)
        self.btnExit=Button(RightFrame13a,font=('verdana',16,'bold'),text="Exit",bd=4,pady=1,padx=20,width=5,height=2).grid(row=5,column=0,padx=1)

        #Product Details Table
        scroll_y_product_details = Scrollbar(TopFrame3, orient=VERTICAL)
        scroll_x_product_details = Scrollbar(TopFrame3, orient=HORIZONTAL)

        self.product_details_records = ttk.Treeview(TopFrame3,height=6,
                    columns=("product_detail_ID","product_detail_date","product_detail_product_ID","product_detail_invoice_ID"),yscrollcommand=scroll_y_product_details.set, xscrollcommand=scroll_x_product_details.set)
                    
        
        scroll_y_product_details.pack(side=RIGHT, fill=Y)
        scroll_x_product_details.pack(side=BOTTOM, fill=X)

        self.product_details_records.heading("product_detail_ID", text="Product Detail ID")
        self.product_details_records.heading("product_detail_date", text="Product Date")
        self.product_details_records.heading("product_detail_product_ID", text="Product ID")
        self.product_details_records.heading("product_detail_invoice_ID", text="Invioce ID")


        self.product_details_records['show'] = 'headings'

        self.product_details_records.column("product_detail_ID", width=100)
        self.product_details_records.column("product_detail_date", width=100)
        self.product_details_records.column("product_detail_product_ID", width=100)
        self.product_details_records.column("product_detail_invoice_ID", width=100)

        self.product_details_records.pack(fill=BOTH, expand=1)

        #Frames4
        #Customers
        MainFrame4 = Frame(notebook, bd=10, width=770, height=700, relief=RIDGE, bg='#40739f')
        MainFrame4.grid()
        
        TopFrame4 = Frame(MainFrame4, bd=5, width=770, height=500, relief=RIDGE)
        TopFrame4.grid(row=1, column=0)

        RightFrame14 = Frame(TopFrame4, bd=5, width=100, height=400, bg='#40739f', relief=RIDGE)
        RightFrame14.pack(side=RIGHT)
        RightFrame14a = Frame(RightFrame14, bd=5, width=90, height=300, padx=2, pady=2, relief=RIDGE)
        RightFrame14a.pack(side=TOP)

        self.btnInsert=Button(RightFrame14a,font=('verdana',16,'bold'),text="Insert",bd=4,pady=1,padx=20,width=5,height=2).grid(row=0,column=0,padx=1)
        self.btnUpdate=Button(RightFrame14a,font=('verdana',16,'bold'),text="Update",bd=4,pady=1,padx=20,width=5,height=2).grid(row=1,column=0,padx=1)
        self.btnDelete=Button(RightFrame14a,font=('verdana',16,'bold'),text="Display",bd=4,pady=1,padx=20,width=5,height=2).grid(row=2,column=0,padx=1)
        self.btnSearch=Button(RightFrame14a,font=('verdana',16,'bold'),text="Search",bd=4,pady=1,padx=20,width=5,height=2).grid(row=3,column=0,padx=1)
        self.btnReset=Button(RightFrame14a,font=('verdana',16,'bold'),text="Reset",bd=4,pady=1,padx=20,width=5,height=2).grid(row=4,column=0,padx=1)
        self.btnExit=Button(RightFrame14a,font=('verdana',16,'bold'),text="Exit",bd=4,pady=1,padx=20,width=5,height=2).grid(row=5,column=0,padx=1)

        #Customers Table
        scroll_y_customer = Scrollbar(TopFrame4, orient=VERTICAL)
        scroll_x_customer = Scrollbar(TopFrame4, orient=HORIZONTAL)

        self.customer_records = ttk.Treeview(TopFrame4,height=6,
                    columns=("customer_ID","customer_name","customer_tel","customer_address_ID"),yscrollcommand=scroll_y_customer.set, xscrollcommand=scroll_x_customer.set)
                    
        
        scroll_y_customer.pack(side=RIGHT, fill=Y)
        scroll_x_customer.pack(side=BOTTOM, fill=X)

        self.customer_records.heading("customer_ID", text="Customer ID")
        self.customer_records.heading("customer_name", text="Customer Name")
        self.customer_records.heading("customer_tel", text="Customer Tel")
        self.customer_records.heading("customer_address_ID", text="Address ID")


        self.customer_records['show'] = 'headings'

        self.customer_records.column("customer_ID", width=100)
        self.customer_records.column("customer_name", width=100)
        self.customer_records.column("customer_tel", width=100)
        self.customer_records.column("customer_address_ID", width=100)

        self.customer_records.pack(fill=BOTH, expand=1)


        #Frames5
        #Invoice
        MainFrame5 = Frame(notebook, bd=10, width=770, height=700, relief=RIDGE, bg='#40739f')
        MainFrame5.grid()
        
        TopFrame5 = Frame(MainFrame5, bd=5, width=770, height=500, relief=RIDGE)
        TopFrame5.grid(row=1, column=0)

        RightFrame15 = Frame(TopFrame5, bd=5, width=100, height=400, bg='#40739f', relief=RIDGE)
        RightFrame15.pack(side=RIGHT)
        RightFrame15a = Frame(RightFrame15, bd=5, width=90, height=300, padx=2, pady=2, relief=RIDGE)
        RightFrame15a.pack(side=TOP)

        self.btnInsert=Button(RightFrame15a,font=('verdana',16,'bold'),text="Insert",bd=4,pady=1,padx=20,width=5,height=2).grid(row=0,column=0,padx=1)
        self.btnUpdate=Button(RightFrame15a,font=('verdana',16,'bold'),text="Update",bd=4,pady=1,padx=20,width=5,height=2).grid(row=1,column=0,padx=1)
        self.btnDelete=Button(RightFrame15a,font=('verdana',16,'bold'),text="Display",bd=4,pady=1,padx=20,width=5,height=2).grid(row=2,column=0,padx=1)
        self.btnSearch=Button(RightFrame15a,font=('verdana',16,'bold'),text="Search",bd=4,pady=1,padx=20,width=5,height=2).grid(row=3,column=0,padx=1)
        self.btnReset=Button(RightFrame15a,font=('verdana',16,'bold'),text="Reset",bd=4,pady=1,padx=20,width=5,height=2).grid(row=4,column=0,padx=1)
        self.btnExit=Button(RightFrame15a,font=('verdana',16,'bold'),text="Exit",bd=4,pady=1,padx=20,width=5,height=2).grid(row=5,column=0,padx=1)

        #Invoice Table
        scroll_y_invoice = Scrollbar(TopFrame5, orient=VERTICAL)
        scroll_x_invoice = Scrollbar(TopFrame5, orient=HORIZONTAL)

        self.invoice_records = ttk.Treeview(TopFrame5,height=6,
                    columns=("invoice_ID","invoice_customer_ID","invoice_date"),yscrollcommand=scroll_y_invoice.set, xscrollcommand=scroll_x_invoice.set)
                    
        
        scroll_y_product.pack(side=RIGHT, fill=Y)
        scroll_x_product.pack(side=BOTTOM, fill=X)

        self.invoice_records.heading("invoice_ID", text="Invoice ID")
        self.invoice_records.heading("invoice_customer_ID", text="Customer ID")
        self.invoice_records.heading("invoice_date", text="Date")

        self.invoice_records['show'] = 'headings'

        self.invoice_records.column("invoice_ID", width=100)
        self.invoice_records.column("invoice_customer_ID", width=100)
        self.invoice_records.column("invoice_date", width=100)

        self.invoice_records.pack(fill=BOTH, expand=1)

        #Frames6
        #Address
        MainFrame6 = Frame(notebook, bd=10, width=770, height=700, relief=RIDGE, bg='#40739f')
        MainFrame6.grid()
        
        TopFrame6 = Frame(MainFrame6, bd=5, width=770, height=500, relief=RIDGE)
        TopFrame6.grid(row=1, column=0)

        RightFrame16 = Frame(TopFrame6, bd=5, width=100, height=400, bg='#40739f', relief=RIDGE)
        RightFrame16.pack(side=RIGHT)
        RightFrame16a = Frame(RightFrame16, bd=5, width=90, height=300, padx=2, pady=2, relief=RIDGE)
        RightFrame16a.pack(side=TOP)

        self.btnInsert=Button(RightFrame16a,font=('verdana',16,'bold'),text="Insert",bd=4,pady=1,padx=20,width=5,height=2).grid(row=0,column=0,padx=1)
        self.btnUpdate=Button(RightFrame16a,font=('verdana',16,'bold'),text="Update",bd=4,pady=1,padx=20,width=5,height=2).grid(row=1,column=0,padx=1)
        self.btnDelete=Button(RightFrame16a,font=('verdana',16,'bold'),text="Display",bd=4,pady=1,padx=20,width=5,height=2).grid(row=2,column=0,padx=1)
        self.btnSearch=Button(RightFrame16a,font=('verdana',16,'bold'),text="Search",bd=4,pady=1,padx=20,width=5,height=2).grid(row=3,column=0,padx=1)
        self.btnReset=Button(RightFrame16a,font=('verdana',16,'bold'),text="Reset",bd=4,pady=1,padx=20,width=5,height=2).grid(row=4,column=0,padx=1)
        self.btnExit=Button(RightFrame16a,font=('verdana',16,'bold'),text="Exit",bd=4,pady=1,padx=20,width=5,height=2).grid(row=5,column=0,padx=1)

        #Address Table
        scroll_y_address = Scrollbar(TopFrame6, orient=VERTICAL)
        scroll_x_address = Scrollbar(TopFrame6, orient=HORIZONTAL)

        self.address_records = ttk.Treeview(TopFrame6,height=6,
                    columns=("address_ID","address_country","address_city","address_district", "address_open", "address_post_code"),yscrollcommand=scroll_y_address.set, xscrollcommand=scroll_x_address.set)
                    
        
        scroll_y_address.pack(side=RIGHT, fill=Y)
        scroll_x_address.pack(side=BOTTOM, fill=X)

        self.address_records.heading("address_ID", text="Address ID")
        self.address_records.heading("address_country", text="Country")
        self.address_records.heading("address_city", text="City")
        self.address_records.heading("address_district", text="District")
        self.address_records.heading("address_open", text="Open Address")
        self.address_records.heading("address_post_code", text="Post Code")


        self.address_records['show'] = 'headings'

        self.address_records.column("address_ID", width=100)
        self.address_records.column("address_country", width=100)
        self.address_records.column("address_city", width=100)
        self.address_records.column("address_district", width=100)
        self.address_records.column("address_open", width=100)
        self.address_records.column("address_post_code", width=100)

        self.address_records.pack(fill=BOTH, expand=1)

     
        notebook.add(MainFrame, text='Home Page',)
        notebook.add(MainFrame2, text='Products')
        notebook.add(MainFrame3, text='Product Details')
        notebook.add(MainFrame4, text='Customers')
        notebook.add(MainFrame5, text='Invoices')
        notebook.add(MainFrame6, text='Address')


if __name__ == '__main__':
    root = Tk()
    application = stockTracking(root)
    root.mainloop()
