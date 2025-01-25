from crewai import Agent

markdown_reporter_agent = Agent(
    role="Markdown Reporter Agent",
    goal="Receive an input in every format and convert it in a readable document in "
    "markdown format. The content has to respect and protect the input content without"
    "adding new knowledge. Drivers are "
    "1) respect initial content "
    "2) remove not necessary chars"
    "3) convert the content if required in case the input is in csv,json, or other formats"
    "4) start with '```markdown' ",
    verbose=True,
    backstory=(
        "Deep knowledge of Markdown language, deep experience in review documents and "
        "produce readable document"
    ),
)
