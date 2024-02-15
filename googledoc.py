import json
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/documents.readonly"]

# The ID of a sample document.
DOCUMENT_ID = "11c7NkQaj9izwzT1u_rcRZOQ-CMYq01P42LOkX7UEEoA"

paths_not_to_clean = []

def get_paths_from_doc():
  """Shows basic usage of the Docs API.
  Prints the title of a sample document.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials2.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("docs", "v1", credentials=creds)

    # Retrieve the documents contents from the Docs service.
    document = service.documents().get(documentId=DOCUMENT_ID).execute()

    # print(f"{document.get('body')}")
    jsonData = json.dumps(document)
    dictData = json.loads(jsonData)
    i = 1;
    while i < len(dictData['body']['content']) - 1:
      print(dictData['body']['content'][i]['paragraph']['elements'])
      x1 = json.dumps(dictData['body']['content'][i]['paragraph']['elements'])
      x2 = json.loads(x1)
      y1 = json.dumps(x2[0]['textRun'])
      y2 = json.loads(y1)
      str = y2['content'].replace('\n', '')
      paths_not_to_clean.append(str)
      i += 1
    return paths_not_to_clean
  except HttpError as err:
    print(err)