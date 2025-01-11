from jira import JIRA
from crewai.tools import BaseTool
from dotenv import load_dotenv
import os


class JiraEpicCreatorTool(BaseTool):
    name: str = "JiraEpicCreatorTool"
    description: str = (
        """
        This tool is able to create a Jira Epic using summary, description, type.
        """
    )

    def _run(self, summary: str, description: str, type: str):
        load_dotenv()
        jira_url = os.environ["JIRA_URL"]
        username = os.environ["JIRA_USERNAME"]
        api_token = os.environ["JIRA_API_TOKEN"]
        jira_options = {"server": jira_url}
        jira_project = os.environ["JIRA_PROJECT"]

        try:
            # Login
            jira = JIRA(options=jira_options, basic_auth=(username, api_token))
            # permissions = jira.my_permissions()
            meta = jira.createmeta(projectKeys=jira_project)
            print(meta)
            issue_fields = {
                "project": {"key": jira_project},
                "summary": summary,
                "description": description,
                "issuetype": {"name": type},
            }
            epic_issue = jira.create_issue(fields=issue_fields)
            print(epic_issue)
            return epic_issue.key
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    tool = JiraEpicCreatorTool()
    key = tool._run(
        "create a button unit test", "create a material button unit test story", "Story"
    )
    print(f"Key: {key}")
