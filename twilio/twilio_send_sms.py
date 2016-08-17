from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACd7c12c042e9f4a14cb7e3e9b7f746a76"
auth_token  = "38acff3deeaeaaf155d323e6894c1c41"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="This is a message from Twilio...How are you!",
    to="+14085940521",    # Replace with your phone number
    from_="+18312178048") # Replace with your Twilio number
print message.sid
