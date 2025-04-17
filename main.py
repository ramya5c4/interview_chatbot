import streamlit as st
from data_stream import get_data_llm,get_validate_name,get_validate_contact_info

#Display welcome message
welcome_response='''<h3 style="padding:50px 0px 20px 50px;"> welcome to Talent scout.</h3>'''
st.write(welcome_response,unsafe_allow_html=True)

#initializing the sessions based on content
if "message" not in st.session_state:
    st.session_state.message= [{"role": "assistant", "response": "Kindly provide your full name"}]
if "prompt_index" not in st.session_state:
    st.session_state['prompt_index']=0
if "question" not in st.session_state:
    st.session_state["question"]=None
if "question_index" not in st.session_state:
    st.session_state["question_index"]=0
if "done" not in st.session_state:
    st.session_state.done = False

#Display chat content based on prompts
for message in st.session_state.message:
      st.chat_message(message["role"]).html(message["response"])


if not st.session_state.done:
#Get the user input
  if prompt:=st.chat_input("say something"):
#show the user input and added to the session
    with st.chat_message("user"):
        st.html(prompt)
        st.session_state.message.append({"role": "user", "response": prompt})

    question=""
    if st.session_state['prompt_index'] ==0:
           valid,msg=get_validate_name(prompt)

           if valid:
              question = f"Hello {prompt}.</br> Please provide the following information:</br>Email,Phone Number and Current Location(comma-separated):"
              st.session_state['prompt_index'] += 1
           else:
               question = msg

    elif st.session_state['prompt_index'] == 1:
        valid, msg = get_validate_contact_info(prompt)

        if valid:
            question = f"kindly provide your Tech Stack[streprogramming languages, frameworks, databases, and tools],Years Of Experience and Desired Position."
            st.session_state['prompt_index'] += 1
        else:
            question=msg

    elif st.session_state['prompt_index'] == 2:

          st.session_state["question"] = prompt
          question = f"Thank you for giving the details!Let's begin the interview(Type: Yes or No)."
          st.session_state['prompt_index'] += 1

    elif st.session_state['prompt_index']== 3:
        #get the interview questions help of the below function
       questions,len_questions = get_data_llm(st.session_state["question"])

       if st.session_state["question_index"] < len_questions:
         question=questions[st.session_state["question_index"]]
         st.session_state["question_index"] +=1

       else:
         question = "Thank you for the conversation! We'll get back to you shortly."
         st.session_state.done = True
#show the assistant message
    with st.chat_message("assistant"):
        st.html(question)
        st.session_state.message.append({"role": "assistant", "response": question})
else:
      st.info("The conversation is complete. You can refresh to start again.")









