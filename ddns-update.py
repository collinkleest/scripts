# external packages
from dotenv import load_dotenv
import requests as req
import os

# load environment variables
load_dotenv()

#
# @author ckleest 
# This script is to dynamically update dns records with google domains 
# This script should be run as a chron job every 10 minutes or so
#


GOOGLE_HOSTNAME = os.getenv('GOOGLE_HOSTNAME')
DDNS_USERNAME = os.getenv('DDNS_USERNAME')
DDNS_PASSWORD = os.getenv('DDNS_PASSWORD')
PERSONAL_HOSTNAME = os.getenv('PERSONAL_HOSTNAME')

ENDPOINT_URL = f'https://{GOOGLE_HOSTNAME}/nic/update?hostname={PERSONAL_HOSTNAME}'

googleRequest = req.post(ENDPOINT_URL, auth=(DDNS_USERNAME, DDNS_PASSWORD))


print()

