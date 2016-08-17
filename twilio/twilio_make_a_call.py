from twilio.rest import TwilioRestClient 
 
# put your own credentials here 

ACCOUNT_SID = "ACd7c12c042e9f4a14cb7e3e9b7f746a76"
AUTH_TOKEN  = "38acff3deeaeaaf155d323e6894c1c41"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
 
call = client.calls.create(url="http://demo.twilio.com/docs/voice.xml",
    to="+16505566704",
    from_="+18312178048") 
 
print call.sid
