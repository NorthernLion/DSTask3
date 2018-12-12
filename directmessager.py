import argparse
import json
import requests
from datetime import datetime
import time

from oauth2client.service_account import ServiceAccountCredentials

PROJECT_ID = 'distributedsystemsjp'
BASE_URL = 'https://fcm.googleapis.com'
FCM_ENDPOINT = 'fcm/send'
FCM_URL = BASE_URL + '/' + FCM_ENDPOINT
SCOPES = ['https://www.googleapis.com/auth/firebase.messaging']


def _get_access_token():
  credentials = ServiceAccountCredentials.from_json_keyfile_name(
      'service-account.json', SCOPES)
  access_token_info = credentials.get_access_token()
  return access_token_info.access_token

def _send_fcm_message(fcm_message):
  headers = {
    'Authorization': 'key=' + 'AIzaSyDsfya2CusyM0hcRi_PmAeW9TGsNGUCFzg',
    'Content-Type': 'application/json; UTF-8',
  }
  print(int(time.time() * 1000))
  requests.post(FCM_URL, data=json.dumps(fcm_message), headers=headers)

def _build_common_message(message):
  return {
      'to': 'e_fidSeWNNE:APA91bGfPJXf-INQPszUFMA-u_x-ze1AeJDnCD7U0gL8jEPCV0MUWgeFSV3YOAhBGNFOFSteGlp58CItyiMa0u4Po6g-D7fBL33AcyJXpLW_mriKBE4mHNJ9uMSTECg_YTN3VBg84f72',
      'notification': {
        'title': 'FCM Notification using Push',
        'body': message
      }
  }
  


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--message')
  args = parser.parse_args()
  common_message = _build_common_message(args.message)
  print('FCM request body for message using common notification object:')
  print(json.dumps(common_message, indent=2))
  _send_fcm_message(common_message)

if __name__ == '__main__':
  main()
