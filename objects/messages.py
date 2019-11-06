from datetime import datetime, timedelta
from server.server import get_num_messages, inc_messages, get_users, get_channels, get_messages, get_messages_to_send, MAX_MESSAGE_LEN

class Message:

    def __init__(self, text, channel, sender, time = datetime.now()):
        if MAX_MESSAGE_LEN < len(text):
            raise ValueError(f"message.__init__: '{text[:10]}...' exceeds maximum allowable length.") 
        
        send_immediate = (time == None) 
        
        if send_immediate:
            self._channel_id = channel
            self._time_sent = datetime.now()
        else:
            if time < datetime.now() - timedelta(minutes = 1):
                raise ValueError(f"Message: Time {time} is in the past.")

        self._message = text
        self._u_id = sender
            
        self._is_sent = False # Set to true by channel
        self._is_pinned = False
        self._reacts = {} # Dictionary of react id: react object.

        self._message_id = get_num_messages()

        get_messages()[self._message_id] = self 
        inc_messages()

        # Automatically send or send later.
        if send_immediate:
            get_channels()[channel].send_message(self._message_id)
        else:
            get_messages_to_send().append(self)
        

    
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
        get_channels()[self._channel_id].delete_message(self._message_id)
        del get_messages()[self._message_id]

    def set_pin(self, pin):
        self._is_pinned = pin

    def add_react(self, user, react):
        if react not in self._reacts:
            self._reacts[react] = React(react, user)
        else:
            self._reacts.get(react)._u_ids.add(user)
    
    def set_message(self, message):
        if MAX_MESSAGE_LEN < len(message):
            raise ValueError(f"message.__init__: '{message[:10]}...' exceeds maximum allowable length.") 
        
        self._message = message

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
                    time_created  = (self._time_sent - datetime(1970,1,1)).total_seconds(),
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


