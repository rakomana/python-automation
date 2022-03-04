import schedule
import time

def job(t):
    print (f"I'm working...")
    return

schedule.every().day.at("01:00").do(job,'It is 01:00')

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute