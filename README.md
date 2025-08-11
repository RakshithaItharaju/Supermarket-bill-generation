# Supermarket Bill Generation System (Python)

## 📌 Introduction
Supermarket Bill Generation System is a Python-based application that automates billing for supermarket transactions.
It reads product data, accepts customer purchases, calculates totals, applies taxes/discounts, and generates a printable receipt.

**Developed by:** Itharaju Rakshitha
**College:** Sreenidhi Institute of Science and Technology

---

## 🎯 Features
- Load products and prices from `data/products.csv`
- Add multiple items with quantities
- Automatically calculate subtotal, tax, discounts, and final total
- Generate a receipt saved as a text file in `receipts/`
- Simple CLI interface (no web server required)

---

## 🛠 Technologies & Files
- **Language:** Python 3.8+
- `supermarket_bill.py` - Main application script
- `data/products.csv` - Sample product catalog
- `receipts/` - Folder where receipts are saved (created at runtime)
- `requirements.txt` - (empty, no external packages required)

---

## 📂 How to Run (Local)
1. Ensure Python 3.8+ is installed.
2. Unzip the project folder.
3. From project root, run:
   ```bash
   python supermarket_bill.py
   ```
4. Follow on-screen prompts to add items. A receipt text file will be saved in `receipts/`.

---

## 📊 Billing Logic
- Subtotal = sum(price * qty for all items)
- Tax = 5% of subtotal
- Discount = 2% of subtotal if subtotal > 2000 (configurable in script)
- Total = subtotal + tax - discount

---

## 🚀 Future Enhancements
- Add CSV import/export of transactions
- Add a GUI using Tkinter or a web interface with Flask
- Integrate barcode scanner support
- Add user authentication and multi-store support

---

## 👩‍💻 Author
**Itharaju Rakshitha**  
B.Tech Computer Science and Engineering  
Sreenidhi Institute of Science and Technology
