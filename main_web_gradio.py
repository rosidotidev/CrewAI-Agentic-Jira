import gradio as gr
from dotenv import load_dotenv
from crews import crew, crew_jira_PO, crew_jira_PO_data_entry, crew_jira_data_entry, crew_jira_updater

def ask(prompt):
    inputs = {
        "user_story": prompt,
    }
    output = crew_jira_PO_data_entry.kickoff(inputs=inputs)
    result = {"output": output.raw}

    return result


def start_web_app_blue():
    print("Building web app")
    from web_app_gradio import create_webapp

    models = {}
    models["crew_jira_PO_data_entry"] = {
        "crew": crew_jira_PO_data_entry,
        "description": "Create a backlog and Jira User Stories on Jira",
        "input_field": "user_story",
    }
    models["crew_jira_PO"] = {
        "crew": crew_jira_PO,
        "description": "Create a backlog",
        "input_field": "user_story",
    }
    models["crew_jira_data_entry"] = {
        "crew": crew_jira_data_entry,
        "description": "Create Jira User Stories on Jira",
        "input_field": "backlog",
    }
    models["crew_jira_updater"] = {
        "crew": crew_jira_updater,
        "description": "Bulk update Jira stories",
        "input_field": "list_of_stories_with_update_request",
    }
    models["crew"] = {
        "crew": crew,
        "description": "Retrieves jira issues",
        "input_field": "ask",
    }
    create_webapp(models)


if __name__ == "__main__":
    load_dotenv()
    start_web_app_blue()
