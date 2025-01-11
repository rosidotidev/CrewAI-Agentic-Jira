from jira import JIRA
from crewai.tools import BaseTool
from dotenv import load_dotenv
import os


class JiraStoryCreatorTool(BaseTool):
    name: str = "JiraStoryCreatorTool"
    description: str = (
        """
        This tool is able to create a Jira Story using summary, description, type, epic_key.
        """
    )

    def _run(self, summary: str, description: str, type: str, parent_key:str=None):
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
            issue_fields={
                    "project": {"key": "COBA"},
                    "summary": summary,
                    "description": description,
                    "issuetype": {"name": type},
                }
            if(parent_key):
                issue_fields["parent"]={"key":parent_key}
            epic_issue = jira.create_issue(
                fields=issue_fields
            )
            print(epic_issue)
            return epic_issue.key
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    tool = JiraStoryCreatorTool()
    key = tool._run(
        "create a button unit test", "create a material button unit test story", "Story"
    )
    print(f"Key: {key}")