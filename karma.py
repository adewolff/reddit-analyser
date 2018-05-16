'''Compares Karma received between 2 users' most recent posts'''

from reddit_user import reddituser
import sys

def main():
    # Define users and submission type
    main.user1 = input("First user: ")
    main.user2 = input("Second user: ")
    main.submission = input("Submission type (comment or link): ")
    while main.submission not in {"comment", "comments", "link", "links"}:
        main.submission = input("Please enter either 'comment', or 'link': ")

    # Obtain json data for users 1 and 2.
    user1data = jdata(main.user1)
    user2data = jdata(main.user2)

    # Extra karma for most recent post/comment
    main.user1_karma = reddituser.karma(user1data, main.submission)
    main.user2_karma = reddituser.karma(user2data, main.submission)

    # Determine which user's most recent post/comment has the highest karma.
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
