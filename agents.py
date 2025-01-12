from crewai import Agent
from jira_reader_tool import JiraReaderTool
from jira_story_creator_tool import JiraStoryCreatorTool
from jira_epic_creator_tool import JiraEpicCreatorTool

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
    goal="execute the query JQL query",
    verbose=True,
    tools=[jira_reader_tool],
    backstory=("Able to connect to the right tool and execute the query"),
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

markdown_reporter_agent = Agent(
    role="Markdown Reporter Agent",
    goal="Receive an input in every format and convert it in a readable document in "
         "markdown format. The content has to respect and protect the input content without"
         "adding new knowledge. Drivers are "
         "1) respect initial content "
         "2) remove not necessary chars"
         "3) convert the content if required in case the input is in csv,json, or other formats"
         "4) start with '```markdown' ",

    verbose=True,
    backstory=(
        "Deep learning of Markdown language, deep experience in review documents and "
        "produce readable document"
    ),
)
