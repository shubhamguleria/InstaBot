import requests
from random import choice


ACCESS_TOKEN="7969366515.3d88568.6b680aad289742fd89b58b10f8e2dbaf"
BASE_URL="https://api.instagram.com/v1/"


def self_info():
    url= BASE_URL+"users/self/?access_token={}".format(ACCESS_TOKEN)
    print(url)
    user_info=requests.get(url).json()
    print()
    
    if user_info['meta']['code']==200:
        if len(user_info['data']):
            print("username:{}".format(user_info['data']['username']))
            print("id:{}".format(user_info['data']['id']))
            print("profile picture:{}".format(user_info['data']['profile_picture']))
            print("full name:{}".format(user_info['data']['full_name']))
            print("following: {}".format(user_info['data']['counts']['follows']))
            print("followed by: {}".format(user_info['data']['counts']['followed_by']))
        else:
            print("user does not exist")
    else:
        print('status code other than 200 received')
    
    #Function declaration to get the ID of a user by username
    
def get_user_id(insta_username):
    url=BASE_URL+'users/search?q={}&access_token={}'.format(insta_username,ACCESS_TOKEN)
    print(url)
    user_info =requests.get(url).json()  
    
    
    if user_info['meta']['code']==200:
        if len(user_info['data']):
            return user_info['data']['id']
        else:
            return None
    else:
        print("status code other than 200")
        exit()
        
    #function declaration to get the info of a user by username
    
def get_user_info(insta_username):
    user_id=get_user_id(insta_username)
    if user_id==None:
        print('user does not exist')
        exit()
    url=BASE_URL+'users/{}?access_token={}'.format(user_id,ACCESS_TOKEN)
    print(url)
    user_info=requests.get(url).json()
        
    if user_info['meta']['code']==200:
        if len(user_info['data']):
            print("username:{}".format(user_info['data']['username']))
            print("id:{}".format(user_info['data']['id']))
            print("profile picture:{}".format(user_info['data']['profile_picture']))
            print("full name:{}".format(user_info['data']['full_name']))
            print("following: {}".format(user_info['data']['counts']['follows']))
            print("followed by: {}".format(user_info['data']['counts']['followed_by']))
        else:
            print("there is no data for user") 
    else:
        print("code is other than 200")
        exit()           
                
def start_bot():
    while True:
        print("\n")
        print("hey welcome to instabot")
        print("here are your menu options")
        print("a. get your own details")
        print("b. get details of user by username")
        print('j. Exit')
            
            
        choice=input("enter your choice:")
        if choice=="a":
            self_info()
        elif choice=="b":
            insta_username= input('enter the username:')
            get_user_info(insta_username)
        elif choice=="c":
            exit()    
        else:
            print('wrong choice')
                       
start_bot()                          
    
    






        
