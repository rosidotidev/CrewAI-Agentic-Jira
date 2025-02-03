from jira import JIRA
from crewai.tools import BaseTool
import os
from dotenv import load_dotenv

class JiraStoryUpdaterTool(BaseTool):
    name: str = "Jira Update Tool"
    description: str = (
        "This tool allows the user to update a Jira story by providing the story ID and new fields to update."
        "To update the epic link or to assign a epic to a story uses parent:{'key':epic-key},"
        "To assign the epic or the the story to an assignee uses {'assignee':assignee-name}"
    )

    def _run(self, story_id: str, fields: dict) -> str:
        """
        Updates a Jira story with the given fields.

        Args:
            story_id (str): The ID of the Jira story to update.
            fields (dict): A dictionary containing the fields to update.

        Returns:
            str: Success message or error information.
        """
        load_dotenv()
        jira_url = os.environ["JIRA_URL"]
        username = os.environ["JIRA_USERNAME"]
        api_token = os.environ["JIRA_API_TOKEN"]
        jira_options = {"server": jira_url}
        try:
            print(f"JiraStoryUpdaterTool {fields}")
            # Login
            jira = JIRA(options=jira_options, basic_auth=(username, api_token))
            # Update the story
            if "assignee" in fields.keys():
                jira.assign_issue(story_id,fields["assignee"])
                fields.pop("assignee")
            if "comment" in fields.keys():
                jira.add_comment(story_id,fields["comment"])
                fields.pop("comment")
            jira.issue(story_id).update(fields=fields)

            return f"Story {story_id} has been successfully updated."
        except Exception as e:
            return f"Failed to update story {story_id}: {str(e)}"
if __name__ == "__main__":
    # Initialize tool
    tool = JiraStoryUpdaterTool()

    # Example invocation via ToolAgent
    story_id = "COBA-338"  # Replace with the actual story ID
    fields = {"labels": ["careca_proposed"],"assignee":"roberto73"}  # Adding a label

    result = tool._run(story_id, fields)

    print(result)