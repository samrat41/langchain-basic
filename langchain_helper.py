from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

# Correct env var name

# Correct spelling of temperature
llm = OpenAI(temperature=0.7)


def generate_restaurant_name_and_items(cuisine):
    # Chain 1: Restaurant Name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this"
    )

    name_chain = prompt_template_name | llm | StrOutputParser()

    # Chain 2: Menu Items
    prompt_template_items = PromptTemplate(
        input_variables=["restaurant_name"],
        template="Suggest some menu items for {restaurant_name}. Return it as comma separated string"
    )

    food_items_chain = prompt_template_items | llm | StrOutputParser()

    # Run first chain to get restaurant name
    restaurant_name = name_chain.invoke({"cuisine": cuisine})

    # Run second chain using the restaurant name
    menu_items = food_items_chain.invoke({"restaurant_name": restaurant_name})

    return {
        "restaurant_name": restaurant_name,
        "menu_items": menu_items
    }


if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Italian"))
