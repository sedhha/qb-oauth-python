import requests

class AuthClientError(Exception):
    """AuthClient Error object in case API response status != 200
    """

    def __init__(self, response):
        """Constructor for AuthClientError
        
        :param response: API response
        :type response: `requests` object
        """

        self.response = response
        self.status_code = response.status_code
        self.content = response.content 
        self.headers = response.headers
        self.intuit_tid = response.headers.get('intuit_tid', None) 
        self.timestamp = response.headers.get('Date', None) 

        Exception.__init__(self, 'HTTP status {0}, error message: {1}, intuit_tid {2} at time {3}'.format(self.status_code, self.content, self.intuit_tid, self.timestamp)) 
