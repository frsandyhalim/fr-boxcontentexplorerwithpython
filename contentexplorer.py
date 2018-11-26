from boxsdk import Client
from boxsdk import JWTAuth
from flask import Flask, render_template
import config

# Configure JWT auth and fetch access token
auth = JWTAuth(
  client_id=config.client_id,
  client_secret=config.client_secret,
  enterprise_id=config.enterprise_id,
  jwt_key_id=config.jwt_key_id,
  rsa_private_key_file_sys_path=config.private_key_path,
  rsa_private_key_passphrase=config.private_key_passphrase
)

# Obtain client auth
access_token = auth.authenticate_instance()
client = Client(auth)

# Render HTML using Flask
app = Flask(__name__)
@app.route('/')
def hello():
  html = render_template('template.html',
    fid=config.fid,
    at=access_token
  )
  return html

if __name__ == '__main__':
  app.run()