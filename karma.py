'''Compares Karma received between 2 users' most recent posts'''

from reddit_user import reddituser
import sys

def main():
    main.user1 = "amaklp"
    main.user2 = "andygmb"
    main.submission = "comment"

    user1data = jdata(main.user1)
    user2data = jdata(main.user2)

    main.user1_karma = reddituser.karma(user1data, main.submission)
    main.user2_karma = reddituser.karma(user2data, main.submission)

    highest_link_karma(main.user1, main.user2)


def jdata(username):
    '''returns .json file for indicated username'''
    
    while True:
        
        user = reddituser(username)
        profdata = user.importer()
        
        # Prompts user to re-enter a user if specified username was not found.
        if profdata == 404:
            print("{} doesn't seem to exist.".format(username))
            sys.exit()
        elif profdata == 429:
            print("Too many requests. Please wait before trying again.")
            sys.exit()
        elif profdata == None:
            print("Something went wrong importing userdata. Please check the log file")
            sys.exit()
        else:
            return profdata

def highest_link_karma(first_user, second_user):
    '''compares karma from users 1 and 2's most recent link and evaluates which one 
       is higher.
    '''

    if main.user1_karma > main.user2_karma:
        print("{}'s most recent {} has the highest Karma, with {} points.".format(
            main.user2, main.submission, main.user1_karma))
    elif main.user2_karma > main.user1_karma:
        print("{}'s most recent {} has the highest Karma, with {} points.".format(
            main.user2, main.submission, main.user2_karma))
    elif main.user2_karma == main.user1_karma:
        print("{} and {}'s most recent {} have the same karma, with {} points.".format(
            main.user1, main.user2, main.submission, main.user2_karma))


if __name__ == '__main__':
    main()
