from dotenv import load_dotenv
from crews import crew, crew_jira_PO, crew_jira_PO_data_entry, crew_jira_data_entry, crew_jira_updater
from statememnts_repo import devops_backlog_us


def do_test_read(crew):
    inputs = {
        "ask": "all issues under Epic COBA-343 assigned to 'rosi Doti'"
               "",
    }
    result = crew.kickoff(inputs=inputs)
    print(f"test_read----> \r\n{result}")
    return result


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
    return result


def do_test_act_cpo_1(crew):
    inputs = {
        "user_story": """
As product owner I want to add a new functionality to ecommerce: evaluate shopping.
This functionality has this features:
- A new Angular UI called Evaluate Shopping where it is possible to search an ordered products
- Capability to give a vote to the the ordered products
- A new backend service to associate a vote to the ordered product
                """,
    }
    result = crew.kickoff(inputs=inputs)
    print(f"test_act_cpo----> \r\n{result}")
    return result

def do_test_populate_jira_from_backlog(crew):
    inputs = {"backlog": devops_backlog_us}
    result = crew.kickoff(inputs=inputs)
    print(f"do_test_populate_jira_from_backlog----> \r\n{result}")
    return result
def do_test_jira_updater(crew):
    inputs = {"list_of_stories_with_update_request": "set labels to 'pippo_committed' and 'DevOps' "
                                                     "and assign to 'roberto sidoti' from COBA-353 to COBA-356"}
    result = crew.kickoff(inputs=inputs)
    print(f"do_test_populate_jira_from_backlog----> \r\n{result}")
    return result

def main(action: str):
    print("Hello crewAI")

    match action:
        case "do_test_read":
            do_test_read(crew)
        case "do_test_act_po":
            do_test_act_po(crew_jira_PO)
        case "do_test_act_cpo":
            do_test_act_cpo(crew_jira_PO_data_entry)
        case "do_test_act_cpo_1":
            do_test_act_cpo_1(crew_jira_PO_data_entry)
        case "do_test_populate_jira_from_backlog":
            do_test_populate_jira_from_backlog(crew_jira_data_entry)
        case "do_test_jira_updater":do_test_jira_updater(crew_jira_updater)
        case _:
            print("no action")


if __name__ == "__main__":
    load_dotenv()
    main("do_test_jira_updater")
