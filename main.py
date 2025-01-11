from dotenv import load_dotenv
from crewai import Task, Crew
from jira_reader_tool import JiraReaderTool
from agents import jira_po_agent, jql_executor_agent, jql_agent, jira_creator_agent


def do_test_read(crew):
    inputs = {
        "ask": "all the issues assigned to 'rosi Doti' in status In Progress",
    }
    result = crew.kickoff(inputs=inputs)
    print(f"test_read----> \r\n{result}")


def do_test_act_po(crew):
    inputs = {
        "user_story": """
As user I need to a to-do app developed in Angular 19 and as backend REST services based on 
Spring Boot microservice.
Main features: 
- Angular UI for Login
- Angular UI for to-do list navigation
- Angular UI fro To-do item creation
- Backend implementation for required REST APIs
                """,
    }
    result = crew.kickoff(inputs=inputs)
    print(f"test_act_po----> \r\n {result}")


def do_test_act_cpo(crew):
    inputs = {
        "user_story": """
As Integration Architect I need to produce a new REST API for the entity 'slots', REST API have to respect level 2 maturity model 
- read API that can accept id or key
- update a slot
- delete a slot by id
- delete all slots
                """,
    }
    result = crew.kickoff(inputs=inputs)
    print(f"test_act_cpo----> \r\n{result}")


def main(action: str):
    print("Hello crewAI")
    jira_reader_tool = JiraReaderTool()
    # write all tasks, tools and crew here
    jql_task = Task(
        description="generate the JQL query" "required to solve this ask:{ask}",
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
        expected_output="produce a list of jira user story",
        agent=jira_po_agent,
    )

    jira_data_entry_task = Task(
        description="able to create jira user story or Epic defined by Jira PO Agent",
        expected_output="create a list of new jira user stories (or an Epic) on Jira",
        agent=jira_creator_agent,
    )

    crew = Crew(
        agents=[jql_agent, jql_executor_agent],
        tasks=[jql_task, jql_exe_task],
        verbose=True,
    )

    crew_jira_PO = Crew(agents=[jira_po_agent], tasks=[jira_backlog_task], verbose=True)
    crew_jira_PO_data_entry = Crew(
        agents=[jira_po_agent, jira_creator_agent],
        tasks=[jira_backlog_task, jira_data_entry_task],
        verbose=True,
    )
    match action:
        case "do_test_read":
            do_test_read(crew)
        case "do_test_act_po":
            do_test_act_po(crew_jira_PO)
        case "do_test_act_cpo":
            do_test_act_cpo(crew_jira_PO_data_entry)
        case _:
            print("no action")


if __name__ == "__main__":
    load_dotenv()
    main("do_test_act_po")
