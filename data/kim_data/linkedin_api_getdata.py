from linkedin import linkedin # pip install python-linkedin

# Define CONSUMER_KEY, CONSUMER_SECRET,  
# USER_TOKEN, and USER_SECRET from the credentials 
# provided in your LinkedIn application

CONSUMER_KEY = '75wkfs612yxwdf'
CONSUMER_SECRET = 'MTRDIFOkjvJqSCxd'
USER_TOKEN = '8c423ccf-6d0d-4a92-8d2b-766edda3cfb9'
USER_SECRET = 'f0fc02b7-cba8-4b9d-ab6f-f5a0687c2817'

RETURN_URL = 'http://localhost:8000' # Not required for developer authentication

# Instantiate the developer authentication class

auth = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, 
                                USER_TOKEN, USER_SECRET, 
                                RETURN_URL, 
                                permissions=linkedin.PERMISSIONS.enums.values())

# Pass it in to the app...

app = linkedin.LinkedInApplication(auth)

import json

connections = app.get_connections()

connections_data = 'linkedin_connections.json'

f = open(connections_data, 'w')
f.write(json.dumps(connections, indent=1))
f.close()

DATA_FILENAME = 'position_info.json'

feeds = []
with open(DATA_FILENAME, mode='w') as feedsjson:
        for i in range(len(connections['values'])):
            if connections['values'][i]['id'] != 'private':
                connections['values'][i]['id']
                connection_positions = app.get_profile(member_id=connections['values'][i]['id'], 
                                       selectors=['positions','id'])
                feeds.append(connection_positions)
        json.dump(feeds, feedsjson)