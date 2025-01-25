from crewai import Task
from agents.agile import (
    jira_po_agent,
    jql_executor_agent,
    jql_agent,
    jira_creator_agent,
    jira_updater_agent
)

jql_task = Task(
    description="generate the JQL query required to solve this ask:{ask}",
    expected_output="a string and only a string for JQL with no unuseful white space",
    agent=jql_agent,
)
jql_exe_task = Task(
    description="execute the query retrieved by the Jira JQL Expert",
    expected_output="a string and only with all the result of the query",
    agent=jql_executor_agent,
)

jira_backlog_task = Task(
    description="""Given this user story:
                --------------------    
                {user_story}
                --------------------
                produce a backlog""",
    expected_output="produce a list of jira user story starting with a blank line and using markdown language",
    agent=jira_po_agent,
)

jira_po_data_entry_task = Task(
    description="able to create jira user story or Epic defined by Jira PO Agent",
    expected_output="create a list of new jira user stories (or an Epic) on Jira",
    agent=jira_creator_agent,
)

jira_data_entry_task = Task(
    description="Given this backlog"
    "---------------"
    "{backlog}"
    "---------------"
    "is able to create jira user story or Epic",
    expected_output="create a list of new jira user stories (or an Epic) on Jira",
    agent=jira_creator_agent,
)

jira_updater_task = Task(
    description="Given a list of jira stories or epics and a update request"
                "------"
                " {list_of_stories_with_update_request}"
                "------"
                "is able to update the stories or epics looking to this request",
    expected_output="update a list of jira user stories (or epics) on Jira",
    agent=jira_updater_agent,
)
