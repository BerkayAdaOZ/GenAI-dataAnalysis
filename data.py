import pandas as pd
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.agents.agent_types import AgentType
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os

# Ortam değişkenlerini yükleyin
load_dotenv()

# API anahtarlarını alın
openaiApi = os.getenv("openaiApikey")
anthropicApi = os.getenv("anthropicApikey")

# Dil modellerini başlatın
llmGpt = ChatOpenAI(openai_api_key=openaiApi, model="gpt-4", temperature=0)
llmClaudeHaiku = ChatAnthropic(anthropic_api_key=anthropicApi, model_name="claude-3-haiku-20240307", temperature=0)

# Kullanılacak dil modelini seçin
selectedLlm = llmGpt

# Veri özetleme fonksiyonu
def summarizeData(dataFile):
    dataFile.seek(0)
    df = pd.read_csv(dataFile, low_memory=False)

    pdAgent = create_pandas_dataframe_agent(
        selectedLlm,
        df,
        verbose=True,
        agent_executor_kwargs={"handleParsingErrors": "True"},
        allow_dangerous_code=True,
    )

    dataSummary = {}

    dataSummary["initialData"] = df.head()

    dataSummary["columnsInfo"] = pdAgent.run(
        "Verideki sütunları içeren bir tablo yap. Tabloda sütunların adları ve yanlarına özet bir şekilde içerdikleri bilgi yer alsın. Bunu bir tablo olarak vereceksin ve her şey kesinlikle Türkçe olacak."
    )

    dataSummary["missingValues"] = pdAgent.run(
        "Bu veri kümesinde eksik veri var mı? Eksik veri varsa kaç adet var? Bu sorulara Türkçe olacak şekilde cevap ver."
    )

    dataSummary["duplicateValues"] = pdAgent.run(
        "Bu veri kümesinde tekrar eden veri var mı? Tekrar eden veri varsa kaç adet var? Bu sorulara Türkçe olacak şekilde cevap ver."
    )

    dataSummary["basicMetrics"] = df.describe()

    return dataSummary

# DataFrame'i elde etme fonksiyonu
def getDataframe(dataFile):
    dataFile.seek(0)
    df = pd.read_csv(dataFile, low_memory=False)
    return df

# Değişken trend analizi fonksiyonu
def analysisTrend(dataFile, variable):
    dataFile.seek(0)
    df = pd.read_csv(dataFile, low_memory=False)

    pdAgent = create_pandas_dataframe_agent(
        selectedLlm,
        df,
        verbose=True,
        agent_executor_kwargs={"handleParsingErrors": "True"},
        allow_dangerous_code=True,
    )

    analyzeResponse = pdAgent.run(
        f"Veri kümesi içindeki şu değişkenin değişim trendini yorumla: {variable} Kesinlikle yorumlayacaksın ve yanıtın Türkçe olacak. Verideki satırlar geçmişten günümüze tarih bazlı olduğu için, verideki satırlara bakarak yorumlayabilirsin."
    )

    return analyzeResponse

# Veri hakkında soru sorma fonksiyonu
def askQuestion(dataFile, question):
    dataFile.seek(0)
    df = pd.read_csv(dataFile, low_memory=False)

    pdAgent = create_pandas_dataframe_agent(
        selectedLlm,
        df,
        verbose=True,
        agent_executor_kwargs={"handleParsingErrors": "True"},
        allow_dangerous_code=True,
    )

    AIResponse = pdAgent.run(f"{question} Bu soruya Türkçe cevap vereceksin.")

    return AIResponse