from crewai import Agent, Task, Crew
from jira_reader_tool import JiraReaderTool
from jira_creator_tool import JiraCreatorTool

jira_reader_tool = JiraReaderTool()
jira_creator_tool = JiraCreatorTool()
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
        - description (including acceptance criteria)
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
    goal="create Jira issues using tool",
    verbose=True,
    tools=[jira_creator_tool],
    backstory=("Able to connect to the right tool and create jira issue"),
)
