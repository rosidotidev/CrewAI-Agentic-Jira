import gradio as gr

def get_key_by_value(dictionary, target_value):
    for key, value in dictionary.items():
        if value == target_value:
            return key
    return None

def create_webapp(models):
    descriptions_dict = {key: value["description"] for key, value in models.items()}
    crew_dict = {key: value["crew"] for key, value in models.items()}
    input_dict = {key: value["input_field"] for key, value in models.items()}

    def handle_input(user_input, bot_type):
        if not user_input.strip():
            return "Please enter a question!"
        crew_key = get_key_by_value(descriptions_dict, bot_type)
        crew = crew_dict[crew_key]
        input_field = input_dict[crew_key]
        inputs = {input_field: user_input}
        crew_response = crew.kickoff(inputs=inputs)
        return crew_response.raw

    dropdown_options = [value for value in descriptions_dict.values()]

    with gr.Blocks() as demo:
        gr.Markdown(
            """
            <div style="background-color:#1976D2; padding:5px; border-radius:5px; text-align:center;">
                <h3 style="color:white; margin:0; font-size:24px;">Smart Jira Assistant</h3>
            </div>
            """,
        )

        with gr.Row():
            with gr.Column(scale=3):
                user_input = gr.TextArea(
                    label="Ask your question:",
                    placeholder="Enter your question here...",
                    elem_id="user_input",
                )
            with gr.Column(scale=1):
                dropdown = gr.Dropdown(
                    choices=dropdown_options,
                    value=dropdown_options[0],
                    label="Choose Assistant:",
                )
                submit_button = gr.Button("Submit")

        # Prepopulate the output with a default message
        output = gr.Markdown(
            "Output will be displayed here.<br><br><br><br>",
            elem_id="output",
        )

        submit_button.click(
            handle_input,
            inputs=[user_input, dropdown],
            outputs=output,
        )

    demo.launch(share=True)
