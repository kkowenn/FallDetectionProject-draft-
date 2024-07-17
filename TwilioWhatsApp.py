from twilio.rest import Client

# Twilio credentials (assuming these are correct and have permissions for WhatsApp messaging)
account_sid = 
auth_token = 
client = Client(account_sid, auth_token)

def send_whatsapp_message(message_body):
    message = client.messages.create(
      from_='whatsapp:+14155238886',
      body=message_body,
      to='whatsapp:+66910375075'
    )
    print(f"WhatsApp message sent: {message.sid}")

'''
test it
if __name__ == '__main__':
    send_whatsapp_message("!!!!!!!! Your user has failed !!!!!!!!!! help now call : 1234567890")
'''

'''
if running not work use anaconda
/opt/anaconda3/bin/pip install twilio
/opt/anaconda3/bin/python3 TwilioWhatsApp.py
'''

'''
note!

The number of WhatsApp messages you can send with Twilio isn't directly limited by Twilio,

- Initial Limits:  New WhatsApp-enabled Twilio numbers start on Tier 1,
allowing you to send to a maximum of 1,000 unique recipients within a 24-hour window.

- Ramp Up and Higher Tiers: WhatsApp monitors the volume and quality of your messages.
If you maintain a good "quality rating" and stay below your daily limits,
you can be automatically upgraded to higher tiers within a week.
Higher tiers come with increased message limits.

- Quality Rating:** WhatsApp considers factors like opt-in rates, complaint rates,
and message content when determining your quality rating.
Sending spammy messages or having high complaint rates can hinder your ability to reach higher tiers.

- Here are some resources from Twilio's documentation that you might find helpful:
- Rules and Best Practices for WhatsApp Messaging on Twilio:** [https://www.twilio.com/docs/whatsapp](https://www.twilio.com/docs/whatsapp)

'''
