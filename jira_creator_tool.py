from jira import JIRA
from crewai.tools import BaseTool
from dotenv import load_dotenv
import os


class JiraCreatorTool(BaseTool):
    name: str = "JiraCreatorTool"
    description: str = (
        "This tool is able to create a Jira issue using summary, description and type"
    )

    def _run(self, summary: str, description: str, type: str):
        load_dotenv()
        jira_url = os.environ["JIRA_URL"]
        username = os.environ["JIRA_USERNAME"]
        api_token = os.environ["JIRA_API_TOKEN"]
        jira_options = {"server": jira_url}

        try:
            # Login
            jira = JIRA(options=jira_options, basic_auth=(username, api_token))
            # permissions = jira.my_permissions()
            meta = jira.createmeta(projectKeys="COBA")
            print(meta)
            epic_issue = jira.create_issue(
                fields={
                    "project": {"key": "COBA"},
                    "summary": summary,
                    "description": description,
                    "issuetype": {"name": type},
                }
            )
            print(epic_issue)
            return epic_issue.key
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    tool = JiraCreatorTool()
    key = tool._run(
        "create a button unit test", "create a material button unit test", "Epic"
    )
    print(f"Key: {key}")
