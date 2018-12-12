import argparse
import json
import requests
import datetime

from oauth2client.service_account import ServiceAccountCredentials

PROJECT_ID = 'distributedsystemsjp'
BASE_URL = 'https://fcm.googleapis.com'
FCM_ENDPOINT = 'v1/projects/' + PROJECT_ID + '/messages:send'
FCM_URL = BASE_URL + '/' + FCM_ENDPOINT
SCOPES = ['https://www.googleapis.com/auth/firebase.messaging']


def _get_access_token():
  credentials = ServiceAccountCredentials.from_json_keyfile_name(
      'service-account.json', SCOPES)
  access_token_info = credentials.get_access_token()
  return access_token_info.access_token

def _send_fcm_message(fcm_message):
  headers = {
    'Authorization': 'Bearer ' + _get_access_token(),
    'Content-Type': 'application/json; UTF-8',
  }
  resp = requests.post(FCM_URL, data=json.dumps(fcm_message), headers=headers)
  if resp.status_code == 200:
    print('Message sent to Firebase for delivery, response:')
    print(resp.text)
  else:
    print('Unable to send message to Firebase')
    print(resp.text)

def _build_common_message(message):
  return {
    'message': {
      'token': 'AAAAT7gFYkg:APA91bGxC007WUhxs5kBPctj5EhAYjOPfXKg1SOKem_5NV-nCSmDbgaq-doZJIUiM-sObtt2mw2Y14saEnEigmFwwkX7BvzYghopRHsynSfly4qjAJsdXz2Xalj4DxgxxVGUX6FvtmN_',
      'notification': {
        'title': 'FCM Notification using Push',
        'body': message
      }
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
