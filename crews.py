from agents.agile import (
    jira_po_agent,
    jql_executor_agent,
    jql_agent,
    jira_creator_agent,
    jira_updater_agent
)
from agents.reporter import markdown_reporter_agent
from tasks.agile import (
    jql_task,
    jira_backlog_task,
    jql_exe_task,
    jira_po_data_entry_task,
    jira_data_entry_task,
    jira_updater_task,
)
from tasks.reporter import (
    markdown_pode_backlog_jira_reporter_task,
    markdown_backlog_jira_reporter_task,
    markdown_backlog_reporter_task,
    markdown_jira_reporter_task,
    markdown_jira_updater_reporter_task
)
from crewai import Crew

crew = Crew(
    agents=[jql_agent, jql_executor_agent,markdown_reporter_agent],
    tasks=[jql_task, jql_exe_task,markdown_jira_reporter_task],
    verbose=True,
)

crew_jira_PO = Crew(
    agents=[jira_po_agent, markdown_reporter_agent],
    tasks=[jira_backlog_task, markdown_backlog_reporter_task],
    verbose=True,
)
crew_jira_PO_data_entry = Crew(
    agents=[jira_po_agent, jira_creator_agent, markdown_reporter_agent],
    tasks=[
        jira_backlog_task,
        jira_po_data_entry_task,
        markdown_pode_backlog_jira_reporter_task,
    ],
    verbose=True,
)

crew_jira_data_entry = Crew(
    agents=[jira_creator_agent, markdown_reporter_agent],
    tasks=[jira_data_entry_task, markdown_backlog_jira_reporter_task],
    verbose=True,
)

crew_jira_updater = Crew(
    agents=[jira_updater_agent,markdown_reporter_agent],
    tasks=[jira_updater_task,markdown_jira_updater_reporter_task],
    verbose=True,
)
