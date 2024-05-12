from twilio.rest import Client

account_sid = 'AC35fb884e3b9ed10c4d7f045e46bcadd1'
auth_token = '2707610a5137f1750e031bf62c523ccc'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+14144109592',
  body='yoooo',
  to='+660910375075'
)

print(message.sid)
