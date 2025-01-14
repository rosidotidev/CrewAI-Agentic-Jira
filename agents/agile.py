from crewai import Agent
from tools.jira_reader_tool import JiraReaderTool
from tools.jira_story_creator_tool import JiraStoryCreatorTool
from tools.jira_epic_creator_tool import JiraEpicCreatorTool

jira_reader_tool = JiraReaderTool()
jira_creator_tool_for_story = JiraStoryCreatorTool()
jira_creator_tool_for_epic = JiraEpicCreatorTool()
jql_agent = Agent(
    role="Jira JQL Expert",
    goal="produce only JQL (Jira Query Language) queries accordingly with task to execute",
    verbose=True,
    backstory=(
        "With great knowledge of JIRA JQL Language"
        "understand the request"
        "and able to produce optimized JQL Query"
    ),
)

jira_po_agent = Agent(
    role="Jira PO Expert",
    goal="produce a backlog of jira issues",
    verbose=True,
    backstory=(
        """
        with deep knowledge of the business is able to define a backlog of activities. 
        knows best practices on creating user story: accordingly with INVEST principle, define Acceptance criteria.
        defining for each activity:
        - type (can be Story or Epic)
        - summary
        - description (split in two parts: Details and Acceptance Criteria)
        """
    ),
)

jql_executor_agent = Agent(
    role="Jira JQL Executor",
    goal="receive instructions, transform them in JQL (Jira  Query Language) execute the query JQL query, max 3 attempts",
    verbose=True,
    max_execution_time=3,
    tools=[jira_reader_tool],
    backstory=("Knows Jira, knows Jira main fields ,"
               "knows that if it has to search an issue under an Epic then it has to use 'parent' field of the issue:"
               "in the query substitute 'epiclink' with 'parent'"
               
               "and is able to connect to the right tool and execute the query"),
)

jira_creator_agent = Agent(
    role="Jira Creator Agent",
    goal="create Jira issues using the right tool, if the issue is an Epic return the Epic key."
    "If the description contains the acceptance criteria, format them im markup",
    verbose=True,
    tools=[jira_creator_tool_for_story, jira_creator_tool_for_epic],
    backstory=(
        "Able to connect to the right tool and create jira issue, understand if it is a Story or an Epic"
    ),
)
