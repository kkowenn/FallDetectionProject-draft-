from twilio.rest import Client

account_sid = 'AC35fb884e3b9ed10c4d7f045e46bcadd1'
auth_token = '2707610a5137f1750e031bf62c523ccc'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='!!!!!!! Your user has failed !!!!!!!!!!',
  to='whatsapp:+66910375075'
)

print(message.sid)

'''
noted !
The number of WhatsApp messages you can send with Twilio isn't directly limited by Twilio, but rather by WhatsApp itself with limitations that ease as you establish yourself as a trusted sender. Here's a breakdown:

* **Initial Limits:**  New WhatsApp-enabled Twilio numbers start on Tier 1, allowing you to send to a maximum of 1,000 unique recipients within a 24-hour window.

* **Ramp Up and Higher Tiers:** WhatsApp monitors the volume and quality of your messages. If you maintain a good "quality rating" and stay below your daily limits, you can be automatically upgraded to higher tiers within a week. Higher tiers come with increased message limits.

* **Quality Rating:** WhatsApp considers factors like opt-in rates, complaint rates, and message content when determining your quality rating. Sending spammy messages or having high complaint rates can hinder your ability to reach higher tiers.

**Here are some resources from Twilio's documentation that you might find helpful:**

* **Rules and Best Practices for WhatsApp Messaging on Twilio:** [https://www.twilio.com/docs/whatsapp](https://www.twilio.com/docs/whatsapp)

'''
