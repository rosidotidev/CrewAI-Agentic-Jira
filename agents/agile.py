from crewai import Agent
from tools.jira_reader_tool import JiraReaderTool
from tools.jira_story_creator_tool import JiraStoryCreatorTool
from tools.jira_epic_creator_tool import JiraEpicCreatorTool
from tools.jira_story_updater_tool import JiraStoryUpdaterTool

jira_story_updater_tool=JiraStoryUpdaterTool()
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
        Has experience neither as Product Owner of agile teams neither as Solution Architect and Developer Frontend and Backend
        knows best practices on creating user story: accordingly with INVEST principle, define Acceptance criteria.
        Has experience to split stories in to independent stories having their INVEST value.
        defining for each activity:
        - type (can be Story or Epic)
        - summary
        - description (split in two parts: Details and Acceptance Criteria)
        """
    ),
)

jql_executor_agent = Agent(
    role="Jira JQL Executor",
    goal="receive instructions, transform them in JQL (Jira  Query Language) execute the query JQL query, max 3 attempts."
         "returns the JQL query and the result",
    verbose=True,
    max_execution_time=3,
    tools=[jira_reader_tool],
    backstory=("Knows Jira, knows Jira most important fields ,"
               "knows that if it has to search an issue under an Epic then it has to use 'parent' field of the issue:"
               "in the query substitute 'epiclink' with 'parent'"
               "and is able to connect to the right tool and execute the query returning the query and the result"),
)

jira_creator_agent = Agent(
    role="Jira Creator Agent",
    goal="create Jira issues using the right tool, if the issue is an Epic return the Epic key."
    "If the description contains the acceptance criteria, format them im markdown, if they are already "
         "in markdown leave current format",
    verbose=True,
    tools=[jira_creator_tool_for_story, jira_creator_tool_for_epic],
    backstory=(
        "Able to connect to the right tool and create jira issue, understand if it is a Story or an Epic"
    ),
)

jira_updater_agent = Agent(
    role="Jira Updater Agent",
    goal="update Jira issues using the right tool and mapping the right fields to be updated.",
    verbose=True,
    tools=[jira_story_updater_tool],
    backstory=("Able to connect to the right tool and update jira issue, "
               "Receives single jira story "
               "or epic or a list of them, retrieves the keys and invokes the tools in order to update."
               "it behaves in those steps:"
               "1) extract list of user stories/epic keys"
               "2) extract fields to be updated"
               "3) update each jira story updating right fields"

    ),
)
