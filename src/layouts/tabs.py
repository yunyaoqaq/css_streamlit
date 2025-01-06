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
st.header("Tabs")

st.write(
    dedent(
        """Tabs have multiple components, to style a specific tab group, wrap it in a container with a `key` value to generate a class. \n\n
**Stable selectors using data-baseweb property**\n\n
- `data-baseweb="tab-list"` : Main Tab Group
-  `button` : Each tab is a button 
-  `button[aria-selected="true"]` : Selects the current tab
- `data-baseweb="tab-border"` : Selects the ruler under the tabs
- `data-baseweb="tab-highlight"` : Selects the current tab ruler
- `data-baseweb="tab-panel"` : Selects the tab panel where content is rendered
"""
    )
)

st.subheader("Try it!")
code, preview = st.columns(2, border=True, vertical_alignment="top")


with code:
    dialog_css = dedent(
        """
/* This is the main container for tabs*/
.st-key-styled_tabs div[data-baseweb="tab-list"]{
    background:transparent;
}
/*Every tab is a button element*/
.st-key-styled_tabs button{
    width:33%;
    border-radius:10px;
}

/*Styles the selected tab*/
.st-key-styled_tabs button[aria-selected="true"]{
    background-color:#eaeaea;
}
.st-key-styled_tabs button[aria-selected="true"] p{
    color:blue;
    font-weight:bold;
}

/* This is the bottom ruler for tabs*/
.st-key-styled_tabs div[data-baseweb="tab-border"]{
    background-color:blue;
}

/* This highlights selected tab*/
.st-key-styled_tabs div[data-baseweb="tab-highlight"]{
    background-color:#5c5c5c;
    height:5px;
}

/* This is the bottom ruler for tabs*/
.st-key-styled_tabs div[data-baseweb="tab-border"]{
    background-color:blue;
}

/* This is the body of the tab content*/
.st-key-styled_tabs div[data-baseweb="tab-panel"]{
    background-color:#eaeaea;
}
           """
    )
    styles = st_monaco(
        value=dialog_css.strip(),
        height="400px",
        language="css",
        lineNumbers=True,
        minimap=False,
    )


with preview:
    if st.toggle("Preview Style Changes", value=True):
        st.html(base_style.substitute(css=styles))
    with st.echo("below"):
        with st.container(key="styled_tabs"):
            tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
            with tab1:
                st.write("This is tab 1")
            with tab2:
                st.write("This is tab 2")
            with tab3:
                st.write("This is tab 3")
