import requests
import urllib
from textblob.blob import TextBlob
from textblob.en.sentiments import NaiveBayesAnalyzer

ACCESS_TOKEN="7969366515.3d88568.6b680aad289742fd89b58b10f8e2dbaf"
BASE_URL="https://api.instagram.com/v1/"


def self_info():
    url= BASE_URL+"users/self/?access_token={}".format(ACCESS_TOKEN)
    print(url)
    

    user_info=requests.get(url).json()
    return type(user_info)
    
    
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
        
def download_image(item):
    #download the image for the given url
    urllib.request.urlretrieve(item['url',item['name']])
    
    return None
            
        
def get_own_posts():
    url1=BASE_URL+"users/self/media/recent/?access_token={}".format(ACCESS_TOKEN)  
    print(url1)
    r= requests.get(url1).json()
    print(r)
     
    if r['meta']['code']==200:
        if len(r['data']):
            image_name=r['data'][0]['id']+ ".jpeg"
            print(image_name)
            image_url=print(r['data'][0]["images"]['standard_resolution']['url'])
            
            urllib.request.urlretrieve(image_name,image_url)
            print('your image has been downloaded')
        else:
            print("post does not exist")
    else:
        print("status code other than 200 received")   


def get_post_id(insta_username):
    user_id=get_user_id(insta_username)
    if user_id==None:
        print("user does not exist")
        exit()
        
    url= BASE_URL+"users/{}/media/recent/?access_token={}".format(user_id,ACCESS_TOKEN)
    print(url)
    r= requests.get(url).json()       
    
    if r["meta"]["code"]==200:
        if len(r["data"]):
            return r["data"][0]['id']
        else:
            print("there is no recent post in this")
            exit()
            
    else:
        print("status code is other than 200")
        exit
        
        
def like_a_post(insta_username): 
    media_id= get_post_id(insta_username)
    url=BASE_URL+"media/%s/likes".format(media_id)
    print(url)
    payload={"access_token":ACCESS_TOKEN}
    r= requests.post(url,payload).json()
    if r['meta']["code"]==200:
        print('like is successfull')
    else:
        print("like was unsuccessfull try again")
        
        
        
def post_a_comment(insta_username):
    media_id=get_post_id(insta_username)
    url= BASE_URL+"'media/{}/comments".format(media_id)
    print(url)
    payload={"access_token":ACCESS_TOKEN,"text":"testing using instabot"}
    r= requests.post(url,payload).json()
    
    
    if r['meta']['code']==200:
        print("successfully added a new comment")
    else:
        print("unsuccessfull to added comment")
        
        
        
def del_a_comment(insta_username):
    media_id=get_post_id(insta_username)
    url=BASE_URL+"/media/media-id/comments?access_token={}".format(ACCESS_TOKEN)
    print(url)
    comment_info= requests.get(url).json()
    
    
    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            #Here's a naive implementation of how to delete the negative comments :
            for x in range(0,len(comment_info["data"])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                blob= TextBlob(comment_text,analyzer=NaiveBayesAnalyzer())
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    print ('Negative comment : {}') .format(comment_text)
                    
                    delete_url= BASE_URL+"/media/{}/comments/{}/?access_token={}".format(media_id,comment_id,ACCESS_TOKEN)
                    print ('DELETE request url : %s').format(delete_url)
                    delete_info = requests.delete(delete_url).json()

                    if delete_info['meta']['code'] == 200:
                        print ('Comment successfully deleted!\n')
                    else:
                        print ('Unable to delete comment!')
                else:
                    print ('Positive comment : %s\n') .format(comment_text)
        else:
            print ('There are no existing comments on the post!')
    else:
        print ('Status code other than 200 received!')
    
                 
def start_bot():
    while True:
        print("\n")
        print("hey welcome to instabot")
        print("here are your menu options")
        print("a. get your own details")
        print("b. get details of user by username")
        print("c. get your own post details")
        print ("f.Like the recent post of a user\n")
        print ("h.Make a comment on the recent post of a user\n")
        print('j. Exit')
            
            
        choice=input("enter your choice:")
        if choice=="a":
            self_info()
        elif choice=="b":
            insta_username= input('enter the username:')
            get_user_info(insta_username)
        elif choice =="c":
            get_own_posts()
        elif choice == "d":
            insta_username= input('enter the username:')
            get_user_id(insta_username)
        elif choice=="j":
            exit()    
        elif choice=="f":
            insta_username = input("Enter the username of the user: ")
            like_a_post(insta_username)
        elif choice=="h":
            insta_username = input("Enter the username of the user: ")
            post_a_comment(insta_username)
            
        elif choice=="m":
            insta_username = input("Enter the username of the user: ")
            del_a_comment(insta_username)
        elif choice=="l":
            insta_username = input("Enter the username of the user: ")
            get_user_id(insta_username)
        else:
            print('wrong choice')
            
start_bot()
