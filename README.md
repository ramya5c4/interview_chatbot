<html>
  <h2 align=center>AI Interview chatbot</h2>
  <div>
    <h3>Overview &nbsp:</h3> <p>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspThis project is the Interview chatbot by using Large Language Model.It is mainly for interview scenarios to help the users prepare for job interviews.This chatbot asks the questions based on the given skill set and experience.</p>
    <h3>Technical Details:</h3>
    <span><b>Language Model : </b>LLaMA 3(Here I am using <b>ChatGroq</b> for fast response)</span></br>
    <span><b>Programing Language : </b>Python</span></br>
    <span><b>Frontend : </b>Streamlit</span></br>  
  </div>
  <div>
    <h3>Installation Instructions:</h3>
    <ul>
    <li><b>clone repo:(Github repository)</b></li>
       git clone https://github.com/ramya5c4/interview_chatbot.git</br>
             cd interview_chatbot
    <li><b>Install dependencies:</b></li>
        pip install streamlit</br>
        pip install langchain_groq
    </ul>  
  </div>
  <div>
    <h3>Prompt Design:</h3>
         <p> &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspThe chatbot uses dynamic prompt engineering to simulate tailored interview experiences. It begins by collecting essential candidate details, then generates interview questions based on their tech background and experience level</p>
    <ul>
   <li>The chatbot gathers user information and creates targeted interview questions tailored to the provided tech stack and experience level.</li>
    <li>The user provides a response to the given prompt.</li>
                 
  </div>
  <div>
      if prompt:=st.chat_input("say something"):

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
       
       questions,len_questions = get_data_llm(st.session_state["question"])

       if st.session_state["question_index"] < len_questions:
         question=questions[st.session_state["question_index"]]
         st.session_state["question_index"] +=1

       else:
         question = "Thank you for the conversation! We'll get back to you shortly."
         st.session_state.done = True

    with st.chat_message("assistant"):
        st.html(question)
        st.session_state.message.append({"role": "assistant", "response": question})
  </div>
</html>
