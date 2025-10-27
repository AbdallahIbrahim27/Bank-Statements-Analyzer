# 🏦 Bank Statements Analyzer

A Streamlit-based web app that uses **LLama 3.2 Vision** to extract structured financial data from bank statement images and return it in **valid JSON** — including customer info and transaction tables.

---

## 🚀 Features

- Upload a bank statement image (`.jpg`, `.jpeg`, `.png`)
- Uses **LLama Vision** via `ollama.chat` to extract data
- Returns **strictly valid JSON** in a predefined schema
- Parses transactions into a **pandas DataFrame**
- Displays extracted JSON and table in UI

---

## 📦 Installation

```bash
git clone <repo-url>
cd bank-statements-analyzer
pip install -r requirements.txt
```

## ▶️ Run the App

```bash
streamlit run bank_statements_analyzer.py
```
## 📤 Expected JSON Schema
The model is instructed to return only:
```json
{
  "Name": "string",
  "Account Number/Customer Number": "string",
  "Account IBAN": "string",
  "Currency": "string",
  "Branch":"string or null",
  "Start Date": "YYYY-MM-DD",
  "End Date": "YYYY-MM-DD",
  "Transactions": [
    {
      "Date": "YYYY-MM-DD",
      "Transaction Details": "string",
      "Ref. No.":"string",
      "Deposit/Debit": "number or null",
      "Withdrawal/Credit": "number or null",
      "Balance": "number",
      "Value/Notes": "string or null"
    }
  ]
}
```
## 🛠 Tech Stack

Python

Streamlit

Ollama + Llama Vision

Pandas

## 📌 Notes

If extraction returns malformed JSON, the app shows raw model output.

Statements with low scan quality may reduce accuracy.



