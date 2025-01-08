import streamlit as st
from streamlit.components.v1 import html
from common import HTML_Template, MainCSS
from streamlit_monaco import st_monaco

st.header("Welcome!")
st.html(HTML_Template.base_style.substitute(css=MainCSS.initial_page_styles))


st.write(
    """This application will help you understand the basic structure of some of the most popular Streamlit widgets. 
    Each page contains an editor to allow you to test these CSS changes."""
)

st.subheader("Features")
st.markdown(
    """
:blue[$~~~~$:material/new_releases:] $~~$ CSS Selectors \n
:blue[$~~~~$:material/new_releases:] $~~$ Custom Tips and Tricks \n
:blue[$~~~~$:material/new_releases:] $~~$ Try your own styles \n
:blue[$~~~~$:material/new_releases:] $~~$ Copy to clipboard  \n
"""
)
st.info(
    ":streamlit: $~~$ This application CSS style requires **Streamlit 1.39** or greater."
)

st.subheader("Basic Structure")
st.html("src/static/main_structures.html")
st.subheader("Same style for multiple widgets")
st.write(
    "The `key` argument in Streamlit needs to be unique. In some cases, you want 1 or more widgets to share the same style. For this, the pseudo selector `:has()` needs be implemented."
)
st.write("**Example**")
example_columns = st.columns((1, 2))
example_columns[0].code(
    """
    st.button("Step 1", key="step_one")
    st.button("Step 2", key="step_two")
    st.button("Step 22", key="step_three")
    """
)
example_columns[1].code(
    """
    div:has(.st-key-step_one,.st-key-step_two, .st-key-step_three) button{
    /* button styles here */
    }
    /* OR */ 
    div[class*="st-key-step_"] button{
     /* button styles here */
    }
    """,
    language="css",
)


@st.dialog("About", width="large")
def about():
    with st.container(key="about_me_img"):
        about_me_columns = st.columns((1, 1.5))
        with about_me_columns[0]:
            st.image("src/static/me.jpg")
        with about_me_columns[1]:
            st.title("Carlos D. Serrano")
            st.divider()
            st.subheader(":snowflake: $~~$ Sr. Architect, Solutions Innovation")
            st.subheader(":streamlit: $~~$ Creators Group Member ")
            st.divider()
            link_columns = st.columns(2)
            link_columns[0].link_button(
                "LinkedIn",
                url="https://www.linkedin.com/in/carlosdserrano",
                icon=":material/link:",
                type="primary",
                use_container_width=True,
            )
            link_columns[1].link_button(
                "Medium",
                url="https://medium.com/@serranocarlosd",
                icon=":material/link:",
                type="primary",
                use_container_width=True,
            )


@st.dialog("Global Styles", width="large")
def css_show():
    st.code(MainCSS.initial_page_styles)


if st.button("", icon=":material/info:", type="primary", key="about_me"):
    about()

if st.button("", icon=":material/format_paint:", type="primary", key="css_main"):
    css_show()
