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

---

## ▶️ Run the App

```bash
streamlit run bank_statements_analyzer.py




