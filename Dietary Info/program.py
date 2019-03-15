from flask import Flask
from flask import request
import sys

import os
from google.oauth2 import service_account
import googleapiclient.discovery

#export GOOGLE_APPLICATION_CREDENTIALS="./service-key.json"


worked = False;
# Get credentials
credentials = service_account.Credentials.from_service_account_file(
	filename=os.environ['GOOGLE_APPLICATION_CREDENTIALS'],
	scopes=['https://www.googleapis.com/auth/cloud-platform'])

# Createthe Cloud IAM service object
service = googleapiclient.discovery.build(
	'iam', 'v1', credentials=credentials)

# Call the Cloud IAM ROles API
# If using pulint: disable=no=member
response = service.roles().list().execute()
roles = response['roles']

'''
# Process the response
for role in roles:
	print('Title: ' + role['title'])
	print('Name: ' + role['name'])
	print('Description: ' + role['description'])
	print('')
'''

def create_service_account(project_id, name, display_name):
	#Creates a service account

	# pylint: disable=no-member
	service_account = service.projects().serviceAccounts().create(
		name = 'projects/' + project_id,
		body ={
			'accountId': name,
			'serviceAccount': {
				'displayName': display_name
			}
		}).execute()

	print('Created service account: ' + service_account['email'])
	return service_account


app = Flask(__name__)

@app.route('/')
def hello_world():
    print("Hello console!")
    return 'Hello, World!'