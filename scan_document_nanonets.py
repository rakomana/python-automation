import json
import requests

file_url = r'C:\Users\PrinceR\Downloads\api_test_3.pdf'
url = 'https://app.nanonets.com/api/v2/OCR/Model/ebb724da-508e-4091-b498-1e5c5702b5e7/LabelFile/?async=false'

data = {'file': open(file_url, 'rb')}

response = requests.post(url, auth=requests.auth.HTTPBasicAuth('3R9nRHs_i8cb2nwJZ8vUWijp9CFXZPmS', ''), files=data)

prediction = json.loads(response.text)['result'][0]["prediction"]

new_prediction = {}

count = 0

for key in prediction:
    if prediction[count]["label"] == 'bank_account':
        new_prediction["bank_account"] = prediction[count]["ocr_text"]
    elif prediction[count]["label"] == 'vat':
        new_prediction["excl_vat"] = prediction[count]["ocr_text"]
    elif prediction[count]["label"] == 'vat':
        new_prediction["incl_vat"] = prediction[count]["ocr_text"]
    elif prediction[count]["label"] == 'total_tax':
        new_prediction["vat"] = prediction[count]["ocr_text"]
    elif prediction[count]["label"] == 'buyer_vat_number':
        new_prediction["sp_vat_number"] = prediction[count]["ocr_text"]
    elif prediction[count]["label"] == 'po_number':
        new_prediction["clc_vat_number"] = prediction[count]["ocr_text"]
    elif prediction[count]["label"] == 'buyer_name':
        new_prediction["invoice_to"] = prediction[count]["ocr_text"]
    elif prediction[count]["label"] == 'invoice_date':
        new_prediction["invoice_date"] = prediction[count]["ocr_text"]
    elif prediction[count]["label"] == 'invoice_date':
        new_prediction["invoice_date"] = prediction[count]["ocr_text"]
    elif prediction[count]["label"] == 'invoice_number':
        new_prediction["invoice_number"] = prediction[count]["ocr_text"]
    elif prediction[count]["label"] == 'clc_reference_number':
        new_prediction["clc_reference_number"] = prediction[count]["ocr_text"]
    count = count + 1

print(new_prediction)