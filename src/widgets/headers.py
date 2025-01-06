import streamlit as st
from textwrap import dedent
from streamlit_monaco import st_monaco
from string import Template

st.header("Headers", anchor=False, divider=True)

st.write(
    dedent(
        """Headers do not have a `key` argument on the widget definition. 
    To style a specific widget, wrapping it in a `st.container` will allow you to isolate the specific widget.\n\n
- `st.title` -> `H1`
- `st.header` -> `H2`
- `st.subheader` -> `H3`
    """
    )
)

st.subheader("Try it!")
code, preview = st.columns(2, border=True, vertical_alignment="top")


base_style = Template(
    dedent(
        """
        <style>
            $css
        </style>"""
    )
)
with code:
    headers_css = dedent(
        """

.st-key-header_style_one h1{
        color:red;
        font-weight:bold;
        }
.st-key-header_style_one h2{
        background-color:grey;
        color:black;
        padding-left:10px;
        border-radius:25px;
    }
.st-key-header_style_one h3{
        background-color:black;
        color:white;
        padding-left:10px;
        margin:10px;
    }

           """
    )
    styles = st_monaco(
        value=headers_css,
        height="400px",
        language="css",
        lineNumbers=True,
        minimap=False,
    )


with preview:
    if st.toggle("Preview Style Changes", value=True):
        st.html(base_style.substitute(css=styles))
    with st.echo("below"):

        with st.container(key="header_style_one"):
            st.title("Streamlit", anchor=False)
            st.header("Styles", anchor=False)
            st.subheader("Sample", anchor=False)
