
import streamlit as st
import ollama
import os
import pandas as pd
import json
import tempfile

# ---------------------------
# Config
# ---------------------------
st.set_page_config(page_title="GlobalCorp & Ollin Group Bank Statement Analyzer", page_icon="🏦", layout="centered")

st.title("🏦GlobalCorp & Ollin Group Bank Statement Analyzer")

# ---------------------------
# JSON extraction instruction
# ---------------------------
JSON_INSTRUCTION = """
Extract all data from this bank statement image and return ONLY valid JSON with the following structure:

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

⚠️ Important:
- Return ONLY the JSON object (no explanations, no comments, no markdown).
- Dates must be in ISO format (YYYY-MM-DD).
- If a field is missing, set it to null.
- Ensure the JSON is syntactically valid.
"""
# ---------------------------
# Upload 
# ---------------------------
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
        tmp_file.write(uploaded_file.getbuffer())
        temp_path = tmp_file.name

    st.image(temp_path, caption="Uploaded Image", width="stretch")

    if st.button("Extract Table"):
        with st.spinner("Extracting data from uploaded image..."):
            try:
                response = ollama.chat(
                    model="llama3.2-vision",
                    messages=[{
                        "role": "user",
                        "content": JSON_INSTRUCTION,
                        "images": [temp_path]
                    }],
                )

                raw_output = response["message"]["content"].strip()

                try:
                    data = json.loads(raw_output)
                    if "Transactions" in data and isinstance(data["Transactions"], list):
                        df = pd.DataFrame(data["Transactions"])
                        st.subheader("📊 Extracted Transactions")
                        st.dataframe(df, width="stretch")
                    st.subheader("📝 Extracted JSON")
                    st.json(data)
                except json.JSONDecodeError:
                    st.error("⚠️ The model did not return valid JSON. Showing raw output instead:")
                    st.text_area("Raw Output", raw_output, height=300)

            except Exception as e:
                st.error(f"⚠️ Error: {e}")
            finally:
                if os.path.exists(temp_path):
                    os.remove(temp_path)
