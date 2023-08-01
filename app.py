import streamlit as st
import plotly.figure_factory as ff
import plotly.express as px
import requests
import pandas as pd
import numpy as np
import io
from snowflake.snowpark.session import Session
from snowflake.snowpark.types import Variant
from snowflake.snowpark.functions import udf,sum,col,array_construct,month,year,call_udf,lit
from snowflake.snowpark.version import VERSION
from snowflake.ml.modeling.compose import ColumnTransformer
from snowflake.ml.modeling.pipeline import Pipeline
from snowflake.ml.modeling.preprocessing import PolynomialFeatures, StandardScaler
from snowflake.ml.modeling.linear_model import LinearRegression
from snowflake.ml.modeling.model_selection import GridSearchCV
import json
import logging 
logger = logging.getLogger("snowflake.snowpark.session")
logger.setLevel(logging.ERROR)

## Connection
connection_parameters = json.load(open('connection.json'))
session = Session.builder.configs(connection_parameters).create()
session.sql_simplifier_enabled = True
snowflake_environment = session.sql('select current_user(), current_version()').collect()
snowpark_version = VERSION
st.title("Digital Twinning Australia")

## Tabular data
df= session.table('fishing')
df = df.to_pandas() 
st.dataframe(df[:5], use_container_width=True)

## APIs
#api_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/birdwood%2C%20south%20australia?unitGroup=metric&include=days&key=CBWQ6NTRW2GUF443E4WZ7XLGM&contentType=csv"
#response = requests.get(api_url)
#csv_data = response.content
#df = pd.read_csv(io.BytesIO(csv_data))
#st.dataframe(df, use_container_width=True)

## Display
fig = px.box(df, x='DEPTH', y='CATCH', title='Box Plot of "CATCH" vs. "DEPTH"')
st.plotly_chart(fig)
