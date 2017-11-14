from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACcd5e29e9de9910421dd3dec145d4840b"
# You're Auth Token from twilio.com/console
auth_token  = "87345eaa6b50eba7cd47fede96bd27cb"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+201124582520", 
    from_="+1 510-662-0376 ",
    body="Hello from Python! My Names Ramy :")

print(message.sid)
