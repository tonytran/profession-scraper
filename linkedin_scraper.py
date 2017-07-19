from requests_oauthlib import OAuth2Session
import webbrowser
def get_linkedin_credentials_from_file(linkedin_credentials_filename):
    credentials_file_handler = open(linkedin_credentials_filename)
    clientid_line = credentials_file_handler.readline()
    clientsecret_line = credentials_file_handler.readline()
    client_id = clientid_line.split()[1]
    client_secret = clientsecret_line.split()[1]
    return (client_id, client_secret)

def get_linked_history(linkedin_session):
    pass

def create_linkedin_work_history_json(linkedin_history):
    pass

def create_linkedin_oauth_session(authorization_base_url, token_url, client_id, redirect_uri, client_secret):


    linkedin = OAuth2Session(client_id, redirect_uri = redirect_uri)
    #linkedin = linkedin_compliance_fix(linkedin)

    authorization_url, state = linkedin.authorization_url(authorization_base_url)
    print("Please go here and authorize", authorization_url)
    webbrowser.open(authorization_url)
    redirect_response = str(input("Enter the full redirect url here "))

    linkedin.fetch_token(token_url, client_secret=client_secret, authorization_response=redirect_response)
    return linkedin

def main():
    linkedin_credentials_filename = "linkedin_credentials.txt"
    linkedin_credentials = get_linkedin_credentials_from_file(linkedin_credentials_filename)


    client_id = linkedin_credentials[0]
    client_secret = linkedin_credentials[1]
    redirect_uri = "https://127.0.0.1"


    authorization_base_url = "https://www.linkedin.com/uas/oauth2/authorization"
    token_url = 'https://www.linkedin.com/uas/oauth2/accessToken'

    linkedin = create_linkedin_oauth_session(authorization_base_url, token_url, client_id, redirect_uri, client_secret)


    r = linkedin.get("https://api.linkedin.com/v1/people/~?format=json")
    print(r.content)


main()
