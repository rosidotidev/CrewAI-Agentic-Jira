from dotenv import load_dotenv
from crews import crew, crew_jira_PO, crew_jira_PO_data_entry

def ask(prompt):
    inputs = {
        "user_story": prompt,
    }
    output=crew_jira_PO_data_entry.kickoff(inputs=inputs)
    result = {"output":output.raw}

    return result


def start_web_app():
    print("Building web app")
    from web_app import build_web_app
    build_web_app(ask=ask)



if __name__ == "__main__":
    load_dotenv()
    start_web_app()
