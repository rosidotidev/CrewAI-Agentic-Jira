# CrewAI-Agentic-Jira

## Introduction
**CrewAI-Agentic-Jira** is a project designed to **automate processes in Jira** using the **CrewAI framework** and Generative AI agents. It simplifies common Jira operations like creating, querying, and managing issues, while demonstrating the potential of AI-driven task automation.

This project also includes a **web interface** built with Streamlit, providing an intuitive way to interact with the system and showcasing the current capabilities of the automation framework.

---

## Features
- **Process Automation**:
  - Automates the creation of User Stories, Epics, and Tasks in Jira.
  - Allows natural language queries to retrieve and manage Jira issues.
  
- **Web Interface**:
  - A lightweight, user-friendly interface to demonstrate the automation features.
  - Includes dropdowns for selecting agents and multi-line inputs for complex queries.
  
- **Customizable AI Agents**:
  - Select from multiple AI-powered bots, each tailored for specific Jira operations.
  - Extendable backend for adding new bots and workflows.

- **Integration with Jira**:
  - Uses Jira's REST API to perform real-time operations.
  - Securely manages API tokens for authentication.

---

## Installation

### Prerequisites
- **Python** 3.8 or later
- **pip** package manager
- A valid **Jira API token**
- Internet connection to fetch dependencies and interact with Jira's API

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/rosidotidev/CrewAI-Agentic-Jira.git
   cd CrewAI-Agentic-Jira
 
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
    pip install -r requirements.txt

2. **Set Up Environment** 
  Variables Create a .env file in the project directory and add the following variables:

3. JIRA_URL=https://your-jira-domain.atlassian.net
JIRA_API_TOKEN=your-api-token
JIRA_EMAIL=your-email@example.com

4. **Run the Application**
   ```bash
   streamlit run app.py


