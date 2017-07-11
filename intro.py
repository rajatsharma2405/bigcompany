import requests

APP_ACCESS_TOKEN = '1400615726.0c43bae.7ce2afc048f94fb4b9f0161accd45de0'
#access token for self info

BASE_URL = 'https://api.instagram.com/v1/'


def self_info():
  request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  user_info = requests.get(request_url).json()
  #convert json into py

  if user_info['meta']['code'] == 200:
    if len(user_info['data']):
      print 'Username: %s' % (user_info['data']['username'])
      print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
      print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
      print 'No. of posts: %s' % (user_info['data']['counts']['media'])
    else:
      print 'User does not exist!'
        #no user found
  else:
    print 'Status code other than 200 received!'

self_info()

def get_user_id(insta_username):
    requested_url = (BASE_URL +"users/search?q=%s&access_token=%s") %(insta_username, APP_ACCESS_TOKEN)
    print "Requested url is:%s" %(requested_url)
    user_info = requests.get(requested_url).json()
    print user_info

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print user_info['data'][0]['id']

        else:
            return None

    else:
        print "status code other than 200 received"
        exit()

insta_username = raw_input("enter the username of the user")
get_user_id(insta_username)


def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print "No user exists"
        exit()

    requested_url = (BASE_URL +"users/%s?q=%s") %(user_id,ACCESS_TOKEN)
    print "Requested url is:%s" %(requested_url)
    user_info = requests.get(requested_url)
    print user_info

get_user_info(insta_username)


