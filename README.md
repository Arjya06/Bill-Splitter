# 💸 Bill Splitter with UPI QR Code Generator

A Python-based web app to split a bill among friends and generate UPI QR codes for each person to pay their share instantly.

---

## 📌 Project Overview

This app helps users:

* Input a total bill amount
* Enter names and UPI IDs of group members
* Auto-calculate equal split
* Generate a UPI QR code for each person
* Share or display the QR for easy payment

---

## 🚀 Features

* [x] Input total bill and number of people
* [x] Enter names and UPI IDs
* [x] Equal amount calculation
* [x] UPI link generation
* [x] QR code creation and display
* [x] Save QR codes as images

---

## 🛠 Tech Stack

* **Language**: Python 3.8+
* **Frontend**: Streamlit (for UI)
* **QR Generation**: qrcode
* **Image Handling**: Pillow (PIL)
* **Editor**: Visual Studio Code

---

## 📁 Folder Structure

```
bill-splitter-upi/
├── main.py
├── qr_codes/              # Stores QR images
└── requirements.txt
```

---

## 📦 Setup Instructions (in VS Code)

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/bill-splitter-upi.git
cd bill-splitter-upi
```

### 2. Install Required Packages

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run main.py
```

---

## 💻 Main Python Code Explained

* Takes bill input and number of people
* Uses `session_state` to store form data
* Collects name and UPI for each person
* Creates a UPI deep link using:

  ```
  upi://pay?pa=<UPI_ID>&pn=<Name>&am=<Amount>&cu=INR
  ```
* Generates QR code with `qrcode` library
* Saves to `/qr_codes/`
* Displays each QR image in the web app

---

## ✅ Example Output

* Alice: ₹250 → \[UPI QR Code]
* Bob: ₹250 → \[UPI QR Code]

Each person can scan and pay instantly.

---

## 🔒 UPI Link Format

```
upi://pay?pa=example@upi&pn=Alice&am=250&cu=INR
```

---

## 🌐 Optional Add-ons

* [ ] Allow custom amounts per person
* [ ] Email QR code to each user
* [ ] Combine all QR codes into a single PDF
* [ ] Deploy to Streamlit Cloud for public access

---

## 📄 License

MIT License. Feel free to fork and use.

---

## 👨‍💻 Author

Made with ❤️ by \[Your Name]. Connect on [LinkedIn](https://linkedin.com/in/your-profile)

---

## 📬 Feedback

If you have suggestions or improvements, feel free to open an issue or PR!
