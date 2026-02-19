import requests

# Your deployed endpoint
url = "https://ocr-compare-five.vercel.app/compare"

# Direct download link for the Google Drive file
drive_url = "https://drive.google.com/uc?export=download&id=1lU_gjstAFpmXQuCI5efKYP02cgpurbR_"

# Example OCR text (replace with actual OCR output)
ocr_text = """NITROGEN 12%
INGREDIENTS: UREA, CMC
STORAGE: Keep in a cool dry place"""

# Send POST request with form data
data = {
    "csv_url": drive_url,
    "ocr_text": ocr_text
}

response = requests.post(url, data=data)

print("Status:", response.status_code)

# If the API returns a DOCX file, save it locally
if response.status_code == 200 and "application/vnd.openxmlformats-officedocument.wordprocessingml.document" in response.headers.get("Content-Type", ""):
    with open("test_report.docx", "wb") as f:
        f.write(response.content)
    print("Report saved as test_report.docx")
else:
    # Otherwise, print JSON error/info
    try:
        print("Response:", response.json())
    except Exception:
        print("Raw response:", response.text)
