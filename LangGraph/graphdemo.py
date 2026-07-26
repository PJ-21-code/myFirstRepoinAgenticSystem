from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict
from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key= os.getenv("GROQ_API_KEY")
client= Groq(api_key=groq_api_key)

class State(TypedDict):
    product_name: str
    basic_description: str
    feature_benefits:str
    marketing_message: str
    final_description: str

def generate_basic_description(state):
    """Generate a basic description of the product"""

    response= client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role":"system","content": "You are a smart assistant that provides basic description of the product"},
            {"role": "user", "content": f"Write a brief description of a product named '{state['product_name']}'."}
        ]
    )

    basic_description= response.choices[0].message.content
    return {"basic_description": basic_description}  

def add_feature_benefits(state: State):
    """Add features and benefits to the product description"""
    response= client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": f"List key features and benefits of the product: {state['basic_description']}"}]
    )

    feature_benefits= response.choices[0].message.content
    return {"feature_benefits": feature_benefits}

def create_marketing_message(state: State):
    """Create a marketing message for the product."""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": f"Create a compelling marketing message for the product: {state['feature_benefits']}"}]
    )
    marketing_message = response.choices[0].message.content
    return {"marketing_message": marketing_message}

def final_polish_message(state: State):
    """Polish and finalize the product description."""
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": f"Polish and finalize the product description, incorporating the marketing message: {state['marketing_message']}"}]
    )
    final_description = response.choices[0].message.content
    return {"final_description": final_description}

def build_workflow():
    
    """Build and compile the workflow steps using LangGraph."""
    workflow= StateGraph(State)

    workflow.add_node("generate_basic_description", generate_basic_description)
    workflow.add_node("add_feature_benefits", add_feature_benefits)
    workflow.add_node("create_marketing_message", create_marketing_message)
    workflow.add_node("final_polish_message", final_polish_message)

    workflow.add_edge(START, "generate_basic_description")
    workflow.add_edge("generate_basic_description","add_feature_benefits")
    workflow.add_edge("add_feature_benefits","create_marketing_message")
    workflow.add_edge("create_marketing_message","final_polish_message")
    workflow.add_edge("final_polish_message", END)

    chain= workflow.compile()
    return chain

def main():

    product_name= input("Enter the name of the product: ")

    initial_state= {
        "product_name": product_name,
        "basic_description": "",
        "feature_benefits": "",
        "marketing_message": "",
        "final_description": ""
    }

    chain= build_workflow()

    result= chain.invoke(initial_state)

    print(result)

if __name__== "__main__":
    main()  