'''
This file will act as a temporary database, housing events, users, and comments for the time being

'''

users_db = {}
events_db = {}
comments_db = {}

user_id_counter = 0
event_id_counter = 0
comment_id_counter = 0

def get_next_user_id():
    global user_id_counter
    user_id_counter += 1
    return user_id_counter

def get_next_event_id():
    global event_id_counter
    event_id_counter += 1
    return event_id_counter

def get_next_comment_id():
    global comment_id_counter
    comment_id_counter += 1
    return comment_id_counter


