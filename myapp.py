import json
import datetime

data = {'email': 'test@test.com','username':'test','password':'12345778','password2':'12345778','first_name':'foo','last_name':'test'}
print(json.dumps(data))

print(type(datetime.timedelta(days=10)))