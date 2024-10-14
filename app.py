import requests

def User():
    username = input("Enter your GitHub username: ")

    if not username:
        print("Enter a Valid Github Username!")
    else:
        url = "https://api.github.com/users/{}/events"

    
        # Making connection to the API
        requset = requests.get(url.format(username)).json()
        numCommit = 0
        numIssuess = 0
        nameIssuses = []

        # Getting the necessary Github Endpoints

        for req in requset:
            if req['type'] == "PushEvent":
                numCommit += len(req['payload']['commits'])
            elif req['type'] == 'IssuesEvent' and req['payload']['action'] in ['opened', 'edited']:
                numIssuess += len(req['payload']['issue'])
                nameIssuses.append(req['payload']['issue'])


        for issues in nameIssuses:
            issues['title']
            issues['html_url']
            print(f"Your most recent Issuse is {issues['title']} and the URL is {issues['html_url']}")

        print(f"User: {username}")
        print(f"The Number of Commits made by {username} is {numCommit}")
        print(f"The Number of Issues made by {username} is {numIssuess}")
User()