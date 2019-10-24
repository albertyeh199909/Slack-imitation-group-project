import sys
from flask_cors import CORS
from json import dumps
from flask import Flask, request
from objects import *
import jwt
from AccessError import AccessError

users = {} # u_id: user obj
channels = {} # chann
messages = {} # message_id: message obj

private_key = "secure password"

def authcheck(u_id, user = None, channel = None, chowner = False, admin = False):
    
    if user != None and user != u_id:
        raise AccessError(f"auth: User {u_id} is not {user}.")
    if channel != None and not users[u_id].is_admin:
        if channel not in users[user].get_channels():+
            raise AccessError(f"auth: User {u_id} is not in channel {channel}")
        if chowner and user not in channels[channel].get_owners():
            raise AccessError(f"auth: User {u_id} is in channel {channel} but is not an owner.")  
    if admin and not users[u_id].is_admin():
        raise AccessError(f"auth: User {u_id} is not admin")

def tokcheck(token):
    payload = jwt.decode(token, private_key)
    return payload["u_id"]



TEST_OWNER_EMAIL = "TODO"
TEST_OWNER_PASSWORD = "TODO"
TEST_CHANNEL_EMAIL = "TODO"
TEST_CHANNEL_PASSWORD = "TODO"
TEST_EMAIL = "TODO"
TEST_PASSWORD = "TODO"
TEST_CHANNEL_OWNER_UID = "TODO"
TEST_NORMAL_UID = "TODO"
TEST_INVALID_UID = "TODO"
TEST_INVALID_PASSWORD = TEST_PASSWORD + " "
TEST_INVALID_EMAIL = "TODO"
TEST_INVALID_MESSAGE = "0"*1001
TEST_VALID_MESSAGE = "0"*1000
TEST_VALID_CHANNEL_ID = "TODO"  
TEST_INVALID_CHANNEL_ID = "TODO"
TEST_VALID_CHANNEL_OWNER = "TODO"

TEST_VALID_REACT = 0


def auth_login(email, password):
    return {}
def auth_logout(token):
    return {}
def auth_register(email, password, name_first, name_last):
    return {}
def auth_passwordreset_request(email):
    return {}
def auth_passwordreset_reset(reset_code, new_password):
    return {}
def channel_invite(token, channel_id, u_id):
    return {}
def channel_details(token, channel_id):
    return {}
def channel_messages(token, channel_id, start):
    return {}
def channel_leave(token, channel_id):
    return {}
def channel_join(token, channel_id):
    return {}
def channel_addowner(token, channel_id, u_id):
    return {}
def channel_removeowner(token, channel_id, u_id):
    return {}
def channels_list(token):
    u_id = tok(token)
    authcheck(u_id, channel = channel_id)
    
    return {}
def channels_listall(token):
    u_id = tok(token)
    authcheck(u_id, channel = channel_id)
    
    return {}
def channels_create(token, name, is_public):u_id = tok(token)
    authcheck(u_id, channel = channel_id)
    
    return {}
def channels_delete(token, channel_id):u_id = tok(token)
    authcheck(u_id, channel = channel_id)
    
    return {}
def message_sendlater(token, channel_id, message, time_sent):
    
    return {}

def message_send(token, channel_id, message):
    u_id = tok(token)
    authcheck(u_id, channel = channel_id)
    channels[channel].send_message(u_id, message)
    return {}


def message_remove(token, message_id):
    u_id = tok(token)
    authcheck(u_id, channel = channel_id)

    return {}
def message_edit(token, message_id, message):
    return {}
def message_react(token, message_id, react_id): 
    
    if react in self._reacts and user in self._reacts.get(react)._u_ids:
            raise ValueError(f"message_react: User {user} already has react_id {react} on message {self._message_id}: '{self._message[:10]}...'")
     
    return {}
def message_unreact(token, message_id, react_id):



    if react not in self._reacts or user not in self._reacts.get(react)._u_ids:
            raise ValueError(f"message_unreact: User {user} already has react_id {react} on message {self._message_id}: '{self._message[:10]}...'")
        
    return {}
def message_pin(token, message_id):        
    
    
    if self._is_pinned:
        raise ValueError(f"message.pin: Message {self._message_id} '{self._message[:10]}...' is already pinned.")
    else:
    return {}
def message_unpin(token, message_id):
    if self._is_pinned:
        raise ValueError(f"message.unpin: Message {self._message_id} '{self._message[:10]}...' is not pinned.")
    else:
    
    return {}
def user_profile(token, u_id):
    

    return {}
def user_profile_setname(token, name_first, name_last):
    return {}
def user_profile_setemail(token, email):
    return {}
def user_profile_sethandle(token, handle_str):
    return {}
def user_profiles_uploadphoto(token, img_url, x_start, y_start, x_end, y_end):
    return {}
def standup_start(token, channel_id):
    return {}
def standup_send(token, channel_id, message):
    return {}
def search(token, query_str):
    return {}
def admin_userpermission_change(token, u_id, permission_id):
    return {}