from agents import jira_po_agent, jql_executor_agent, jql_agent, jira_creator_agent
from tasks import jql_task, jira_backlog_task, jql_exe_task, jira_data_entry_task
from crewai import Crew
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