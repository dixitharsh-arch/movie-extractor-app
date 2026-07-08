import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from typing import List, Optional


class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str


model = init_chat_model(
    "llama-3.3-70b-versatile",
    model_provider="groq",
    temperature=0.8
)

parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert movie information extractor.

Extract the movie information from the given paragraph.

Instructions:
1. Return the output ONLY in the format specified below.
2. Fill every field whenever possible.
3. If the paragraph does not explicitly mention the director, cast, release year, rating, or genre but they are widely known, use your general knowledge to fill them.
4. Never return null for 'genre' or 'cast'. If unknown, return an empty list [].
5. Never leave the summary empty. Generate a concise 2-3 sentence summary based on the paragraph.
6. Do not include any explanation, markdown, or extra text.
7. Follow the format instructions exactly.

{format_instructions}
"""
        ),
        ("human", "{paragraph}")
    ]
)

st.set_page_config(page_title="Movie Information Extractor", page_icon="🎬", layout="centered")

st.title("🎬 Movie Information Extractor")

para = st.text_area("Give your paragraph:", height=200)

if st.button("Extract"):
    if para.strip():
        with st.spinner("Extracting movie information..."):
            final_prompt = prompt.invoke(
                {
                    "paragraph": para,
                    "format_instructions": parser.get_format_instructions()
                }
            )

            response = model.invoke(final_prompt)

            movie_data = parser.parse(response.content)

        st.json(movie_data.model_dump_json(indent=4))
    else:
        st.warning("Please enter a paragraph.")
