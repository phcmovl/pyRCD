from pyRCD.conf import logger

class User(object):
    """
    This is the base class for all users

    Arguments coming soon.
    """
    @logger.log_and_call('creating new user')
    def __init__(self):
        #internal
        self._id                    = ''
        self._access_levels         = set()

        #basics
        self.user_nickname          = ''
        self.user_realname          = ''
        self.user_host              = ''
        self.user_indent            = ''
        self.user_email             = ''
        
        #extra
        self.using_ssl              = False
        self.connect_date           = ''
        self.last_command           = ''
        self.last_command_timestamp = ''
    
