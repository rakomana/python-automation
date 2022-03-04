# from multiprocessing import connection
# import secrets
# import smtplib
# import secret_manager

# connection = smtplib.SMTP('smtp.gmail.com')

# connection.starttls()
# connection.login(user= secret_manager.email_address, password= secret_manager.password)
# connection.sendmail(
#     from_addr= secret_manager.from_email,
#     to_addrs= secret_manager.to_email, 
#     msg= 'Subject:Hello\n\nThis is the actual message'
#     )
# connection.close()

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.weekday()
print(f'{now}')