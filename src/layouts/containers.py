import streamlit as st
from string import Template
from textwrap import dedent
from streamlit.components.v1 import html
from streamlit_monaco import st_monaco

base_style = Template(
    dedent(
        """
        <style>
            $css
        </style>"""
    )
)
st.header("Containers")

st.write(
    "To style a specific container, assign a value to the `key` argument to create a CSS class.  "
)

st.subheader("Try it!")
code, preview = st.columns(2, border=True, vertical_alignment="top")


with code:
    button_css = dedent(
        """
.st-key-styled_container{
    background-color:grey;
    border-radius:1rem;
    padding:1rem;
    min-height:100px;
    box-shadow: 3px 5px 15px 0px rgba(128, 128, 128, 0.245);
    }

 .st-key-styled_container div[data-testid="stText"] div{
    color:white;
    
}
           """
    )
    styles = st_monaco(
        value=button_css.strip(),
        height="400px",
        language="css",
        lineNumbers=True,
        minimap=False,
    )

st.html(base_style.substitute(css=styles))
with preview:
    with st.echo("below"):
        with st.container(key="styled_container"):
            st.text("This is a styled container")

        with st.container():
            st.text("This is an unstyled container")
