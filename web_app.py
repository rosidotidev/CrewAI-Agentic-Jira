import streamlit as st

# set layout wide
st.set_page_config(layout="wide")

def get_key_by_value(dictionary, target_value):
    for key, value in dictionary.items():
        if value == target_value:
            return key
    return None

def create_webapp(models):
    """
    Create a chatbot web application interface with a Material-like theme,
    where the bot selection dropdown and input field are aligned on the same line.
    The output is styled with dark blue text on a light blue background.
    """
    # Add a compact top bar using Streamlit layout
    st.markdown(
        """
        <div style="background-color:#1976D2; padding:5px; border-radius:5px;">
            <h3 style="color:white; text-align:center; margin:0; font-size:24px;">Smart Jira Assistant</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Apply CSS to align input at the top and style output
    st.markdown(
        """
        <style>
        .main {
            padding-top: 0px !important; /* Remove extra padding from the main content */
        }
        .output-box {
            background-color: #E3F2FD; /* Light blue background */
            color: #0D47A1; /* Dark blue text */
            padding: 15px;
            border-radius: 5px;
            font-size: 16px;
            border: 1px solid #0D47A1;
            margin-top: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([3, 1])  # Define column ratios
    descriptions_dict = {key: value["description"] for key, value in models.items()}
    crew_dict = {key: value["crew"] for key, value in models.items()}
    input_dict={key: value["input_field"] for key, value in models.items()}
    print(crew_dict)
    with col2:
        bot_type = st.selectbox("Choose Assistant:", descriptions_dict.values())

    # Multiline input in the second column
    with col1:
        user_input = st.text_area("Ask your question:", key="user_input", height=150)

    # Submit button aligned below both components
    if st.button("Submit"):
        if not user_input.strip():
            st.warning("Please enter a question!")
        else:

            crew_key = get_key_by_value(descriptions_dict, bot_type)
            crew=crew_dict[crew_key]
            input_field=input_dict[crew_key]
            inputs = {input_field: user_input}
            crew_response=crew.kickoff(inputs=inputs)
            response=crew_response.raw
            st.markdown(f'{response}', unsafe_allow_html=True)


