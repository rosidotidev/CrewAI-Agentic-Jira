from jira import JIRA
from crewai.tools import BaseTool
from dotenv import load_dotenv
import os


class JiraReaderTool(BaseTool):
    name: str = "JiraReaderTool"
    description: str = (
        "This tool can retrieve Jira issues using jql (JIRA QUERY LANGUAGE) language"
    )

    def _run(self, jql_query: str):
        load_dotenv()
        jira_url = os.environ["JIRA_URL"]
        username = os.environ["JIRA_USERNAME"]
        api_token = os.environ["JIRA_API_TOKEN"]
        jira_options = {"server": jira_url}

        try:
            # Login
            jira = JIRA(options=jira_options, basic_auth=(username, api_token))
            # Query
            results = jira.search_issues(jql_query)
            output = []
            for issue in results:
                output.append(
                    f"*{issue.key}*: {issue.fields.summary} \r\n *Status*:{issue.fields.status.name} \r\n *Description*: {issue.fields.description}"
                )

            return output
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    tool = JiraReaderTool()
    results = tool._run("PROJECT=COBA")
    for issue in results:
        print(issue)
