from datetime import datetime, timedelta
from server.state import *
from server.constants import *
class Message:

    def __init__(self, text, channel, sender, time = None, is_standup = False):
        if MAX_MESSAGE_LEN < len(text):
            raise ValueError(f"Message '{text[:10]}...' with length {len(text)} exceeds maximum allowable length {MAX_MESSAGE_LEN}.") 
        
        send_immediate = (time == None) 
        
        if send_immediate:
            self._time_sent = datetime.now(TIMEZONE)
        else:
            self._time_sent = time
            if time < datetime.now(TIMEZONE) - timedelta(minutes = 1):
                raise ValueError(f"Time {time} is in the past.")


        self._channel_id = channel
        self._message = text
        self._u_id = sender
            
        self._is_sent = False # Set to true by channel
        self._is_standup = is_standup
        self._is_pinned = False
        self._reacts = {} # Dictionary of react id: react object.

        self._message_id = num_messages()

        set_message(self._message_id, self)
        inc_messages()

        # Automatically send or send later.
        if send_immediate:
            get_channel(channel).send_message(self._message_id)
        else:
            get_unsent().append(self)
        

    
    def get_time(self):
        return self._time_sent
    
    def get_id(self):
        return self._message_id

    def get_channel(self):
        return self._channel_id

    def get_user(self):
        return self._u_id

    def get_message(self):
        return self._message
    
    def is_sent(self):
        return self._is_sent

    def send(self):
        self._is_sent = True

    def is_pinned(self):
        return self._is_pinned

    def remove(self):
        get_channel(self._channel_id).delete_message(self._message_id)
        remove_message(self._message_id)

    def set_pin(self, pin):
        self._is_pinned = pin

    def add_react(self, user, react):
        if react not in self._reacts:
            self._reacts[react] = React(react, user)
        else:
            self._reacts.get(react)._u_ids.add(user)
    
    def set_message(self, text):
        if not self._is_standup and MAX_MESSAGE_LEN < len(text):
            raise ValueError(f"Message '{text[:10]}...' with length {len(text)} exceeds maximum allowable length {MAX_MESSAGE_LEN}.") 
        
        self._message = text

    def remove_react(self, user, react):
        self._reacts.get(react)._u_ids.remove(user)
        if not self._reacts.get(react).get_users():
            del self._reacts[react]

    # Returns the reacts list as in specification
    def get_reacts(self, user): 
        return [react.to_json(user) for react in self._reacts.values()]
    
    def get_react(self, react_id):
        return self._reacts[react_id]

    def has_react(self, react_id):
        return react_id in self._reacts
        
    def to_json(self, user):
        return dict(message_id = self._message_id,
                    u_id = self._u_id,
                    message = self._message,
                    time_created  = self._time_sent.timestamp(),
                    reacts = self.get_reacts(user),
                    is_pinned = self._is_pinned)
class React:
    def __init__(self, id, user):
        self._u_ids = set([user])
        self._react_id = id

    def to_json(self, user):
        return dict(u_ids = list(self._u_ids),
                    react_id = self._react_id,
                    is_this_user_reacted = (user in self._u_ids))
    def get_users(self):
        return self._u_ids
    
    def get_id(self):
        return self._react_id

if __name__ == "__main__":
    pass


