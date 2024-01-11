```python
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/presentations']

def create_slide(title, content):
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('slides', 'v1', credentials=creds)

    # Call the Slides API
    presentation = service.presentations().create().execute()
    print('Created presentation with ID: {0}'.format(presentation.get('presentationId')))

    # Create a new slide with the title and content.
    requests = [
        {
            'createSlide': {
                'objectId': 'slide1',
                'insertionIndex': '1',
                'slideLayoutReference': {
                    'predefinedLayout': 'TITLE_AND_TWO_COLUMNS'
                },
            }
        },
        {
            'insertText': {
                'objectId': 'title1',
                'insertionIndex': 0,
                'text': title
            }
        },
        {
            'insertText': {
                'objectId': 'content1',
                'insertionIndex': 0,
                'text': content
            }
        }
    ]

    # Execute the requests.
    body = {
        'requests': requests
    }
    response = service.presentations().batchUpdate(
        presentationId=presentation.get('presentationId'),
        body=body).execute()

    print('Created slide with ID: {0}'.format(response.get('replies')[0].get('createSlide').get('objectId')))

    return presentation.get('presentationId')
```