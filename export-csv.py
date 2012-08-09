from rauth.service import OAuth2Service
import requests
import simplejson

# Get a real consumer key & secret from:
redu = OAuth2Service(
        name='redu',
        authorize_url='http://redu.com.br/oauth/authorize',
        access_token_url='http://redu.com.br/oauth/token',
        consumer_key='',
        consumer_secret='')

# GET urls
# see dev api documentation for more information
me_get_url = "http://www.redu.com.br/api/me.json"
enrollment_get_url = "http://www.redu.com.br/api/courses/{0}/spaces.json"
statuses_get_url = "http://www.redu.com.br/api/spaces/{0}/statuses/timeline.json"

def get_access_token():
	print 'Visit this URL in your browser: ' +  redu.get_authorize_url()
	# This is a bit cumbersome, but you need to copy the code=something (just the
	# `something` part) out of the URL that's redirected to AFTER you login and
	# authorize the demo applicatio
	code = raw_input('Enter the PIN: ')
	# create a dictionary for the data we'll post on the get_access_token request
	data = dict(code=code,
            grant_type='authorization_code',
            redirect_uri='')
	# retrieve the access token
	access_token = \
        redu.get_access_token('POST', data=data).content['access_token']

	print 'The access token is: ' + access_token
	return access_token

def get_login(client):
	r=client.get(me_get_url).content
	return simplejson.loads(r)['login']
def get_enrollments(client):
	r=client.get(me_get_url).content
	data = simplejson.loads(r)
	ref = ""
	for element in data["links"] :
		if(element["rel"] == "enrollments"):
			ref = element["href"]
	r = client.get(ref+".json").content
	return simplejson.loads(r)

def get_enrollment(client, id):
	#print (spaces_get_url.format(id))
	url=spaces_get_url.format(str(id))
	r=client.get(url).content
	return r
def get_spaces(client, id):
	r=client.get(id+"/spaces.json").content
	return simplejson.loads(r)
def get_statuses(client, id):
	r=client.get(statuses_get_url.format(id)).content
	return simplejson.loads(r)



token=get_access_token()
client=requests.session(params={"oauth_token":token}, headers={"content-type":"application/json"})


#after we manage to get our acess_token is just a matter of making the right requests, refer to the redu dev api for more
#information
print ("you own these spaces: ")
names = []
ids = []
count = 0
for element in get_enrollments(client): # iterate through each enrollment
	for link in element["links"]:
		if(link["rel"] == "course"): #if we find a course
			for space in get_spaces(client, link["href"]): # iterate through each space
				ids.append((space["id"]))
				decodedString = space["name"].encode('utf-8', 'ignore')
				names.append(decodedString)
				print (str(count)+") "+decodedString)
				count = count+1
num = raw_input("Please, choose the space you'd like export to CSV:")
choice_id = ids[int (num)]

f = open(names [int (num)]+'.csv', 'w') # create the .csv file
for element in get_statuses(client, choice_id): # iterate through each statuses
	user = element['user']
	user_name = user['first_name']
	user_name = user_name + ' '+ user['last_name']
	user_name = user_name.encode('utf-8')
	f.write(user_name+', ')
	text_encoded = element['text'].encode('utf-8')
	f.write(text_encoded+'\n\n')
f.close()
print ('yay we fineshed exporting your file!')
