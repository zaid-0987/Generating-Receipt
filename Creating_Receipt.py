from tkinter import *
from tkinter import messagebox
from fpdf import FPDF

class Creating_PaymentReceiptPDF(FPDF):
    def above(self):
        self.cell(0, 10, "Payment Receipt", 0, 1, "C")
        
    def down(self):
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

def creating_receipt():
    customer_name = customer_name_var.get()
    payment_date = payment_date_var.get()
    
    items = []
    total_amount = 0
    for i in range(len(item_names)):
        item_name = item_names[i].get()
        item_quantity = item_quantities[i].get()
        item_price = item_prices[i].get()
        item_amount = item_quantity * item_price
        items.append((item_name, item_quantity, item_price, item_amount))
        total_amount += item_amount
    
    receipt_pdf = Creating_PaymentReceiptPDF()
    receipt_pdf.add_page()
    
    receipt_pdf.set_font("Arial", size=12)
    receipt_pdf.cell(0, 10, f"Customer Name: {customer_name}", ln=True)
    receipt_pdf.cell(0, 10, f"Payment Date: {payment_date}", ln=True)
    
    col_width = [80, 30, 30, 30]
    receipt_pdf.set_font("Arial", "B", 12)
    receipt_pdf.cell(col_width[0], 10, "Item", border=1)
    receipt_pdf.cell(col_width[1], 10, "Qty", border=1)
    receipt_pdf.cell(col_width[2], 10, "Price", border=1)
    receipt_pdf.cell(col_width[3], 10, "Amount", border=1)
    receipt_pdf.ln()
    
    for item in items:
        for i in range(4):
            receipt_pdf.cell(col_width[i], 10, str(item[i]), border=1)
        receipt_pdf.ln()
    
    receipt_pdf.set_font("Arial", "B", 12)
    receipt_pdf.cell(col_width[0] + col_width[1] + col_width[2], 10, "Total Amount", border=1)
    receipt_pdf.cell(col_width[3], 10, str(total_amount), border=1)
    
    receipt_filename = "creating_payment_receipt.pdf"
    receipt_pdf.output(receipt_filename)

    messagebox.showinfo("Created Receipt", "Payment receipt and PDF have been generated.")

root = Tk()
root.title("Creating Payment Receipt")

CustomerName = Label(root, text="Customer Name:").grid(row=0, column=0, padx=10, pady=5)
PaymentDate = Label(root, text="Payment Date:").grid(row=1, column=0, padx=10, pady=5)

customer_name_var = StringVar()
payment_date_var = StringVar()

customer_name_entry = Entry(root, textvariable=customer_name_var)
payment_date_entry = Entry(root, textvariable=payment_date_var)

customer_name_entry.grid(row=0, column=1, padx=10, pady=5)
payment_date_entry.grid(row=1, column=1, padx=10, pady=5)

item_names = []
item_quantities = []
item_prices = []

for i in range(3):
    Quantity = Label(root, text=f"Quantity:").grid(row=2 + i, column=2, padx=10, pady=5)
    Name = Label(root, text=f"Name {i+1}:").grid(row=2 + i, column=0, padx=10, pady=5)
    Price = Label(root, text=f"Price {i+1}:").grid(row=2 + i, column=4, padx=10, pady=5)

    item_name_var = StringVar()
    item_quantity_var = IntVar()
    item_price_var = DoubleVar()

    item_name_entry = Entry(root, textvariable=item_name_var)
    item_quantity_entry = Entry(root, textvariable=item_quantity_var)
    item_price_entry = Entry(root, textvariable=item_price_var)

    item_name_entry.grid(row=2 + i, column=1, padx=10, pady=5)
    item_quantity_entry.grid(row=2 + i, column=3, padx=10, pady=5)
    item_price_entry.grid(row=2 + i, column=5, padx=10, pady=5)

    item_names.append(item_name_var)
    item_quantities.append(item_quantity_var)
    item_prices.append(item_price_var)

generate_button = Button(root, text="Creating Receipt", command=creating_receipt)
generate_button.grid(row=5, columnspan=6, padx=10, pady=10)

root.mainloop()
