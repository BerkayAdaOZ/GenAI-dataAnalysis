import streamlit as st
import data
import plotly.express as px
import pandas as pd

if "dataload" not in st.session_state:
    st.session_state.dataload = False

def activateDataload():
    st.session_state.dataload = True

st.set_page_config(page_title="Data Analysis with GenAI", layout="wide")
st.image(image="./img/genaıdataanalysıs.png", use_column_width=True)
st.title("Data Analysis with GenAI")
st.divider()

st.sidebar.subheader("Upload Your Data File")
st.sidebar.divider()

loadedFile = st.sidebar.file_uploader("Select Your CSV File", type="csv")
loadDatabtn = st.sidebar.button(label="Load", on_click=activateDataload, use_container_width=True)

colPrework, colDummy, colInteraction = st.columns([4, 1, 7])

if st.session_state.dataload:
    @st.cache_data
    def summarize():
        loadedFile.seek(0)
        dataSummary = data.summarizeData(dataFile=loadedFile)
        return dataSummary

    dataSummary = summarize()

    with colPrework:
        st.info("DATA SUMMARY")
        st.subheader("Sample Session From Your Data:")
        st.write(dataSummary["initialData"])
        st.divider()
        st.subheader("Variables of Dataset:")
        st.write(dataSummary["columnsInfo"])
        st.divider()
        st.subheader("Missing Value Status:")
        st.write(dataSummary["missingValues"])
        st.divider()
        st.subheader("Duplicate Data Status:")
        st.write(dataSummary["duplicateValues"])
        st.divider()
        st.subheader("Basic Metrics:")
        st.write(dataSummary["basicMetrics"])

    with colDummy:
        st.empty()

    with colInteraction:
        st.info("Interaction With Data")
        variable = st.text_input(label="Which variable do you want to examine?")
        chart_type = st.selectbox("Select Chart Type", ["Histogram", "Line Chart", "Box Plot"])
        examineBtn = st.button(label="Examine")
        st.divider()

        @st.cache_data
        def exploreVariable(dataFile, variable, chart_type):
            dataFile.seek(0)
            dataframe = data.getDataframe(dataFile=dataFile)
            if chart_type == "Histogram":
                fig = px.histogram(dataframe, x=variable, title=f"{variable} Distribution")
            elif chart_type == "Line Chart":
                fig = px.line(dataframe, y=variable, title=f"{variable} Trend Over Time")
            elif chart_type == "Box Plot":
                fig = px.box(dataframe, y=variable, title=f"{variable} Box Plot")
            st.plotly_chart(fig)
            st.divider()
            dataFile.seek(0)
            trendResponse = data.analysisTrend(dataFile=loadedFile, variable=variable)
            st.success(trendResponse)

        if variable and examineBtn:
            exploreVariable(dataFile=loadedFile, variable=variable, chart_type=chart_type)

        st.divider()
        freeQuestion = st.text_input(label="What do you want to ask about the dataset?")
        askBtn = st.button(label="Ask")

        @st.cache_data
        def answerQuestion(dataFile, question):
            dataFile.seek(0)
            AIResponse = data.askQuestion(dataFile=loadedFile, question=question)
            st.success(AIResponse)

        if freeQuestion and askBtn:
            answerQuestion(dataFile=loadedFile, question=freeQuestion)