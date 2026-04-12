# import streamlit as st
# from langchain.chains import SequentialChain # type: ignore
# from langchain import PromptTemplate
# from langchain.chains import LLMChain # type: ignore

# st.title('Langchain Project')
# import os  # noqa: E402
# from langchain.llms import OpenAI # type: ignore  # noqa: E402
# os.environ['OPENAI_API_KEY'] = 'sk-'
# llm = OpenAI(temperature = 0.6)

# promptt = PromptTemplate(
#     input_variables =['country'],
#     template = "whats the capital of {country}"
# )
# chain1 = LLMChain(llm=llm, prompt=promptt, output_key="capital")

# prompt_food = PromptTemplate(
#     input_variables = ['capital'],
#     template="""suggest some most famous food items of {capital}"""
# )
# chain2 = LLMChain(llm=llm, prompt=prompt_food, output_key="food")

# final_chain = SequentialChain(
#     chains = [chain1, chain2],
#     input_variables = ['country'],
#     output_variables = ['capital', 'food']
# )
# user_input = st.text_input("Enter Country")

# if(st.button('Get Food')):
#     response = final_chain.invoke({"country": user_input })
#     st.success(response['country'])
#     st.success(response['capital'])
#     st.success(response['food'])

#     # streamlit run langchain.py (terminal command)


# import streamlit as st
# import os

# # Correct imports (latest LangChain)
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain, SequentialChain
# from langchain_openai import OpenAI

# # Set API Key (⚠️ put your real key here)
# os.environ["OPENAI_API_KEY"] = "your_api_key_here"

# # Create LLM
# llm = OpenAI(temperature=0.6)

# st.title("LangChain Project")

# # Prompt 1 → Get capital
# promptt = PromptTemplate(
#     input_variables=["country"], template="What is the capital of {country}?"
# )

# chain1 = LLMChain(llm=llm, prompt=promptt, output_key="capital")

# # Prompt 2 → Get famous food
# prompt_food = PromptTemplate(
#     input_variables=["capital"], template="Suggest some famous food items of {capital}"
# )

# chain2 = LLMChain(llm=llm, prompt=prompt_food, output_key="food")

# # Sequential Chain
# final_chain = SequentialChain(
#     chains=[chain1, chain2],
#     input_variables=["country"],
#     output_variables=["capital", "food"],
# )

# # User Input
# user_input = st.text_input("Enter Country")

# # Button Action
# if st.button("Get Food"):
#     if user_input:
#         response = final_chain.invoke({"country": user_input})

#         st.success(f"Country: {user_input}")  # FIXED
#         st.success(f"Capital: {response['capital']}")  # Correct
#         st.success(f"Food: {response['food']}")  # Correct
#     else:
#         st.warning("Please enter a country")

# # Run command:
# # streamlit run app.py


import streamlit as st
import os

# ✅ Correct imports (latest)
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain_openai import ChatOpenAI

# ✅ Set your real API key here
os.environ["OPENAI_API_KEY"] = "sk-xxxxxxxxxxxxxxxx"

# ✅ Create LLM (Chat model)
llm = ChatOpenAI(temperature=0.6)

st.title("LangChain Project 🚀")

# ✅ Prompt 1 → Get capital
promptt = PromptTemplate(
    input_variables=["country"], template="What is the capital of {country}?"
)

chain1 = LLMChain(llm=llm, prompt=promptt, output_key="capital")

# ✅ Prompt 2 → Get food
prompt_food = PromptTemplate(
    input_variables=["capital"], template="Suggest some famous food items of {capital}"
)

chain2 = LLMChain(llm=llm, prompt=prompt_food, output_key="food")

# ✅ Sequential Chain
final_chain = SequentialChain(
    chains=[chain1, chain2],
    input_variables=["country"],
    output_variables=["capital", "food"],
)

# ✅ User Input
user_input = st.text_input("Enter Country")

# ✅ Button
if st.button("Get Food"):
    if user_input:
        response = final_chain({"country": user_input})  # simpler than invoke

        st.success(f"Country: {user_input}")
        st.success(f"Capital: {response['capital']}")
        st.success(f"Food: {response['food']}")
    else:
        st.warning("Please enter a country")

# ✅ Run command:
# streamlit run app.py
