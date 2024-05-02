import time
from datetime import datetime
from threading import Thread
def sms(mobile):
    time.sleep(15)
    print(f"sent sms to {mobile}")
def send_email(email):
    time.sleep(10)
    print(f"send and email to {email}")

def send_app(gcm_id, user):
    time.sleep(5)
    print(f"send an app notification to user: {user}, GCM_ID: {gcm_id}")
def transaction():
    print("Transaction Success")
    print(datetime.now())
    sms("1234567890")
    send_email("venkat@gmail.com")
    send_app("qwertyuiop", "venkat")
    print(datetime.now())
    print("Completed the functionality")
transaction()
