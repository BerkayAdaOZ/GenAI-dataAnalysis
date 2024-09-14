# Data Analysis with GenAI

This project provides a streamlined data analysis platform leveraging the power of Generative AI models such as OpenAI's GPT-4 and Anthropic's Claude. By integrating with Pandas, the platform offers robust data exploration, trend analysis, and intelligent querying functionalities for CSV datasets.

## Features
- **Data Upload**: Upload CSV files for data analysis.
- **Data Summary**: Automatically generates summaries of the dataset, including basic metrics, missing values, duplicate data, and a preview of the dataset.
- **Data Interaction**: Examine individual variables, visualize trends, and generate different types of charts (Histograms, Line Charts, Box Plots).
- **AI-Powered Analysis**: Use GPT-4 or Claude to generate insights and respond to natural language queries about the dataset.

  
## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.9+
- Virtual environment (optional but recommended)

### Installation

1. Clone the repository to your local machine.
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. Install the required dependencies.
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory and provide your API keys for OpenAI and Anthropic. 
    ```bash
    touch .env
    ```

    Add the following variables to the `.env` file:
    ```bash
    openaiApikey=your_openai_api_key
    anthropicApikey=your_anthropic_api_key
    ```

### Running the Application

1. Activate your virtual environment if you are using one:
    ```bash
    # On MacOS/Linux
    source venv/bin/activate

    # On Windows
    venv\Scripts\activate
    ```

2. Run the Streamlit app:
    ```bash
    streamlit run main.py
    ```

3. Open your browser and navigate to `http://localhost:8501/` to interact with the application.

### Usage

- **Upload a CSV file**: Go to the sidebar and upload a CSV file. The application will automatically analyze and summarize the data.
- **Examine a Variable**: Use the text input to specify which variable you want to visualize and choose the chart type (Histogram, Line Chart, or Box Plot).
- **Ask a Question**: Use natural language to ask specific questions about the dataset, and the AI will provide insights in response.

### Example

1. Upload your CSV file through the sidebar.
2. Check the generated summaries, such as missing values, duplicates, and basic metrics.
3. Select a variable to analyze and view its trends through charts.
4. Ask specific questions like: _"What are the key trends for the 'sales' variable?"_

## Technologies Used

- **Python**
- **Streamlit** for interactive data applications.
- **Pandas** for data manipulation.
- **Plotly** for interactive data visualizations.
- **LangChain** for integrating with language models.
- **OpenAI GPT-4** and **Anthropic Claude** for natural language processing.

