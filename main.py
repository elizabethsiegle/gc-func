from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

url = "https://us-central1-sms-cloud-func.cloudfunctions.net/reply"

def lol():
    res = requests.post(url=url, params=None)
    resp = MessagingResponse()
    resp.message('hi')
    return str(resp)
