from dotenv import load_dotenv
from crews import crew, crew_jira_PO, crew_jira_PO_data_entry


def ask(prompt):
    inputs = {
        "user_story": prompt,
    }
    output = crew_jira_PO_data_entry.kickoff(inputs=inputs)
    result = {"output": output.raw}

    return result


def start_web_app_blue():
    print("Building web app")
    from web_app import create_webapp
    models={}
    models["crew_jira_PO_data_entry"]={"crew":crew_jira_PO_data_entry,
                                       "description":"Create a backlog and jira User Stories on Jira",
                                       "input_field":"user_story"}
    models["crew_jira_PO"] = {"crew": crew_jira_PO,
                              "description": "Create a backlog",
                              "input_field":"user_story"}
    models["crew"] = {"crew": crew,
                      "description": "retrieves jira issues",
                      "input_field":"ask"}
    create_webapp(models)

if __name__ == "__main__":
    load_dotenv()
    start_web_app_blue()
