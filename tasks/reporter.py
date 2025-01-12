from crewai import Task
from agents.reporter import markdown_reporter_agent
from tasks.agile import jira_backlog_task, jira_po_data_entry_task, jira_data_entry_task

markdown_backlog_reporter_task = Task(
    description="Given a set of input produced by other Agents is able to process their output",
    expected_output="create a markdown document",
    context=[jira_backlog_task],
    agent=markdown_reporter_agent,
)

markdown_pode_backlog_jira_reporter_task = Task(
    description="Given a set of input produced by other Agents is able to process their output",
    expected_output="create a markdown document",
    context=[jira_po_data_entry_task],
    agent=markdown_reporter_agent,
)

markdown_backlog_jira_reporter_task = Task(
    description="Given a set of input produced by other Agents is able to process their output",
    expected_output="create a markdown document",
    context=[jira_data_entry_task],
    agent=markdown_reporter_agent,
)
