from langchain_groq import ChatGroq
import streamlit as st
import re

def get_data_llm(prompt):


        response_llm =f"give the three interview questions based on tech stak,experience,desired position{prompt}"
        llm = ChatGroq(
          model="llama3-70b-8192",
          api_key="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",
          temperature=0.7,
         )
        response=llm.invoke(response_llm)
        questionn=response.content

        cleaned_text = re.sub(r'Here are three interview questions based on tech stack */*/ Question \d+:.*?\n+', '', questionn)

        question_pattern = r"(?s)([A-Za-z0-9\s,.;!?()\-#@$%^&+=|\\'\":,<>/\[\]{}~_]+(?:\s+[A-Za-z0-9\s,.;!?()\-#@$%^&+=|\\'\":,<>/\[\]{}~_]*\?)\s*)"
        question = re.findall(question_pattern, cleaned_text)

        questions = [q.replace("\n", " ").strip() for q in question if q.strip()]

        return questions,len(questions)

def get_validate_name(prompt):
    if not re.match(r"^[A-Za-z\s]{2,50}$", prompt):
        return False,"❌ invalid Name,name should be 2 to 50 characters"
    else:
        return True,""

def get_validate_contact_info(prompt):

    contact_info=[x.strip() for x in prompt.split(",")]

    if len(contact_info) == 3:
       email, phone, location = contact_info
       if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email):
          return False, "❌ Invalid email format."
       if not re.match(r"^[6-9]\d{9}$", phone):
          return False, "❌ Phone number must be 10 digits starting with 6–9."
       if len(location) < 2:
          return False, "❌ Location must be at least 2 characters long."
       return True,""
    else:
        return False, "❌ Please enter Email, Phone Number, and Location (comma-separated)."




