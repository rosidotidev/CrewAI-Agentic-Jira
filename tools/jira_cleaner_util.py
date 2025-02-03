from jira import JIRA
from dotenv import load_dotenv
import os


class JiraCleanerUtil:
    """
    JiraCleanerUtil
    This tool can delete jira issues using jql (JIRA QUERY LANGUAGE) language
    """

    def __init__(self):
        load_dotenv()
        self.jira_url = os.environ["JIRA_URL"]
        self.username = os.environ["JIRA_USERNAME"]
        self.api_token = os.environ["JIRA_API_TOKEN"]
        self.jira_options = {"server": self.jira_url}
        # login
        self.jira = jira = JIRA(
            options=self.jira_options, basic_auth=(self.username, self.api_token)
        )

    def removeAll(self, project: str) -> None:

        try:
            jql_query = f"project = {project}"
            issues = self.jira.search_issues(jql_query, maxResults=1000)
            for issue in issues:
                try:
                    issue.delete()
                    print(f"Issue {issue.key} removed ")
                except Exception as e:
                    print(f"Error on delete: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def removebyKey(self, key: str) -> None:

        try:
            jql_query = f"key = {key}"
            issues = self.jira.search_issues(jql_query, maxResults=1000)
            for issue in issues:
                try:
                    issue.delete()
                    print(f"Issue {issue.key} removed ")
                except Exception as e:
                    print(f"Error on delete: {e}")
        except Exception as e:
            print(f"Error: {e}")
    def removebyJQL(self, jql:str ) -> None:

        try:
            jql_query = f"{jql}"
            issues = self.jira.search_issues(jql_query, maxResults=1000)
            for issue in issues:
                try:
                    issue.delete()
                    print(f"Issue {issue.key} removed ")
                except Exception as e:
                    print(f"Error on delete: {e}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    jira_util = JiraCleanerUtil()
    #jira_util.removeAll("COBA")
    # jira_util.removebyKey("COBA-115")
    jira_util.removebyJQL("project = 'COBA' and key > 'COBA-400'")