import requests
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv
import os


class EasyJiraWrapper:
    def __init__(self, jira_url):
        """
        Initializes the instance with the Jira URL.
        """
        self.jira_url = jira_url.rstrip("/")  # Removes any trailing slashes
        self.session = requests.Session()  # Use a session to maintain the connection
        self.auth = None  # Will be set during login

    def login(self, username, api_token):
        """
        Logs in using username and password.
        """
        # URL for authentication
        # login_url = f"{self.jira_url}/rest/auth/1/session"
        login_url = f"{self.jira_url}/rest/api/2/myself"
        self.session = requests.Session()
        self.session.auth = HTTPBasicAuth(username, api_token)
        self.auth = self.session.auth

        url = f"{self.jira_url}/rest/api/2/myself"
        response = self.session.get(url)

        if response.status_code == 200:
            print(
                f"Login effettuato con successo come: {response.json().get('displayName')}"
            )
        else:
            raise Exception(
                f"Errore durante il login: {response.status_code} - {response.text}"
            )

    def query(self, jql):
        """
        Executes a JQL query and returns the results.
        """
        if self.auth is None:
            raise Exception("Please log in first using the 'login' method.")

        # URL for JQL search
        search_url = f"{self.jira_url}/rest/api/2/search"
        params = {
            "jql": jql,
            "fields": ["summary", "status", "key", "description"],  # Fields to return
            "maxResults": 50,  # Maximum number of results
        }

        # Perform the request
        response = self.session.get(search_url, auth=self.auth, params=params)

        if response.status_code == 200:
            issues = response.json().get("issues", [])

            results = []
            for issue in issues:
                print(f">>>>>> RESULTS {issue}")
                results.append(
                    {
                        "key": issue["key"],
                        "summary": issue["fields"].get("summary", ""),
                        "status": issue["fields"]["status"]["name"],
                        "description": issue["fields"].get("description", ""),
                    }
                )
            print(results)
            return results
        else:
            raise Exception(
                f"JQL query error: {response.status_code} - {response.text}"
            )

    def create_coba_issue(self, summary, description):
        """
        Creates a new issue in the COBA project.
        """
        if self.auth is None:
            raise Exception("Please log in first using the 'login' method.")

        # URL for creating an issue
        create_issue_url = f"{self.jira_url}/rest/api/2/issue"

        # Payload to create the issue
        payload = {
            "fields": {
                "project": {"key": "COBA"},  # Project key for COBA
                "summary": summary,
                "description": description,
                "issuetype": {
                    "name": "Task"  # Issue type, you can modify it as needed
                },
            }
        }

        # Send the POST request to create the issue
        response = self.session.post(create_issue_url, json=payload, auth=self.auth)

        if response.status_code == 201:
            issue_data = response.json()
            issue_key = issue_data.get("key")
            print(f"Issue created successfully! Key: {issue_key}")
            return issue_key
        else:
            raise Exception(
                f"Issue creation error: {response.status_code} - {response.text}"
            )


# Example usage
if __name__ == "__main__":
    load_dotenv()
    jira_url = os.environ["JIRA_URL"]
    username = os.environ["JIRA_USERNAME"]
    api_token = os.environ["JIRA_API_TOKEN"]
    jql_query = "project = COBA AND status = 'In Progress'"

    jira = EasyJiraWrapper(jira_url)

    try:
        # Login
        jira.login(username, api_token)

        # Query
        results = jira.query(jql_query)
        print(f">>>>>> RESULTS {results}")
        for issue in results:
            print(
                f"Key: {issue['key']}, Summary: {issue['summary']}, Status: {issue['status']}, Description: {issue['description']}"
            )

        # Create a new issue in the COBA project
        issue_key = jira.create_coba_issue("performance review", "performance review")
        print(f"Created issue key: {issue_key}")

    except Exception as e:
        print(f"Error: {e}")
