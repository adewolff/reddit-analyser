'''imports a reddit user's .json file and can parse for post/comment info.'''

import requests, json, logging

logging.basicConfig(filename='error-log.txt', level=logging.DEBUG, 
format='%(asctime)s - %(levelname)s - %(message)s')

class reddituser(object):

    def __init__(self, username):
        self.username = username
        self.data = self.importer()

    def importer(self):
        '''imports the profile .json data from the Reddit username input.
           accounts for HTTP errors 404 and 429. Any other HTTP error is saved to log.txt.
        '''
        try:
            with requests.get("http://reddit.com/user/{}.json".format(self.username),
                             headers={"user-agent": "karmacompbot"}) as r:
                r.raise_for_status()
                return(json.loads(r.text))
            # json_data = json.loads(f.read().decode())
            # return json_data

        except requests.exceptions.HTTPError as e:
            if "404" in str(e):
                return 404
            elif "429" in str(e):
                return 429
            else:
                return None
                logging.debug('importer HTTP Error: {}'.format(e))

        ## For using a local .json file:
        # with open('{}.json'.format(self.username)) as json_data:
        #     d = json.load(json_data)
        #     return(d)
        
    def karma(self, submission_type):
        '''returns the karma for the most recent link posted'''
        if submission_type.lower() in {"comment", "comments"}:
            vector = "t1"
        elif submission_type.lower() in {"link","links"}:
            vector = "t3"
        i = 0
        type = self['data']['children'][i]['kind']
        while type != vector:
            type = self['data']['children'][i]['kind']
            i += 1
            if i >= 25:
                return None
                logging.debug('Parsing error: No {} found in recent profile history.'.format(submission_type))
            continue
        return self['data']['children'][i]['data']['score']



        

