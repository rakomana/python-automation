import json
import time
import requests

base_url = 'https://elis.rossum.ai/api/v1/'

#login
login_url = base_url + 'auth/login'
login_data_obj = {'username': 'bradh@clc.co.za','password': 'Bradley123!'}

login = requests.post(login_url, data=login_data_obj)

api_key = json.loads(login.text)["key"]

# print(api_key)

# upload a file
upload_doc_url = base_url + 'queues/113942/upload'
# file_url = r'C:\Users\PrinceR\Downloads\invoice.pdf'
file_url = r'C:\Users\PrinceR\Downloads\api_test_3.pdf'
upload_data_obj = {"content": open(file_url, 'rb')}

upload = requests.post(upload_doc_url, files=upload_data_obj, headers={
    "Authorization": "token " + api_key,
});

annotation_id = (json.loads(upload.text)["annotation"]).rsplit('/', 1)[-1]

# print(annotation_id)

#extract result
#loop until the document is automated
is_automated = True
extracted_data = ''

while is_automated:
    extract_result_url = base_url + 'queues/113942/export?format=json&columns=meta_file_name,document_id,date_issue,sender_name,amount_total&id=' + annotation_id

    extract = requests.post(extract_result_url, headers={
        "Authorization": "token " + api_key,
    });

    extracted_data = extract.text

    is_automated = not json.loads(extract.text)["results"][0]["automated"]
    time.sleep(15)

prediction = json.loads(extracted_data)["results"][0]["content"]

new_prediction = {}

count = 0

# print(prediction)

for key in prediction:
    #invoice_details_section
    if prediction[count].get("schema_id") == 'invoice_details_section':
        children = prediction[count]["children"]
        i = 0
        for child in children:
            if children[i].get("schema_id") == 'document_id':
                new_prediction["invoice_number"] = children[i].get("value")
            elif children[i].get("schema_id") == 'order_id':
                new_prediction["clc_reference_number"] = children[i].get("value")
            elif children[i].get("schema_id") == 'date_issue':
                new_prediction["invoice_date"] = children[i].get("value")
            i = i + 1

    #payment_info_section
    if prediction[count].get("schema_id") == 'payment_info_section':
        p_children = prediction[count]["children"]
        p = 0
        for p_child in p_children:
            if p_children[p].get("schema_id") == 'account_num':
                new_prediction["bank_account"] = p_children[p].get("value")
            p = p + 1

    #totals_section
    if prediction[count].get("schema_id") == 'totals_section':
        t_children = prediction[count]["children"]
        t = 0
        for t_child in t_children:
            if t_children[t].get("schema_id") == 'amount_total_base':
                new_prediction["excl_vat"] = t_children[t].get("value")
            elif t_children[t].get("schema_id") == 'amount_total_tax':
                new_prediction["vat"] = t_children[t].get("value")
            elif t_children[t].get("schema_id") == 'amount_due':
                new_prediction["incl_vat"] = t_children[t].get("value")
            t = t + 1

    #vendor_section
    if prediction[count].get("schema_id") == 'vendor_section':
        v_children = prediction[count]["children"]
        v = 0
        for v_child in v_children:
            if v_children[v].get("schema_id") == 'sender_name':
                new_prediction["invoice_to"] = v_children[v].get("value")
            elif v_children[v].get("schema_id") == 'sender_vat_id':
                new_prediction["sp_vat_number"] = v_children[v].get("value")
            v = v + 1

    count = count + 1



print(new_prediction)
