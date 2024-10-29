
import streamlit as st
import urllib.request
import json
from urllib.error import HTTPError
import time
import random
import string
from pathlib import Path

from prompts import prompts

__author__ = "lcalmbach@gmail.com"
__version__ = "0.0.3"

nomi_dict = {
    'patrick': {'key': st.secrets['bot1_key'], 'name': 'Patrick', 'icon': '👨‍🏭'},
    'michael': {'key': st.secrets['bot2_key'], 'name': 'Michael', 'icon': '🧑‍🦱'},
    'evelyn': {'key': st.secrets['bot3_key'], 'name': 'Evelyn', 'icon': '👩‍🦱'},
}

MAX_NO = 100
nomi_name_dict = {k: v['name'] for k, v in nomi_dict.items()}
authorisation_key = st.secrets['auth_key'] 

st.set_page_config(
    page_title="nomi-chat",
    page_icon="🤖",
    layout="wide"  # This sets the mode to wide
)

def get_response(nomi: dict, prompt: str):
    error_response = "Sorry, I am not sure I can follow you here."
    if prompt is not None:
        req = urllib.request.Request(
            url=f"https://api.nomi.ai/v1/nomis/{nomi['key']}/chat",
            method="POST",
            data=json.dumps({"messageText": prompt}).encode("utf-8"),
            headers={
                "Authorization": authorisation_key,
                "Content-Type": "application/json",
            },
        )
        try:
            with urllib.request.urlopen(req) as response:
                response_data = json.loads(response.read().decode())
                if 'error' in response_data:
                    print(len(prompt), response_data['error'])
                    return error_response
                else:
                    return response_data['replyMessage']['text']
        except HTTPError as e:
            return error_response
        except Exception as e:
            print(f"Error: {e}")
            return error_response
    else:
        return error_response

def create_file():
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    file = Path(f"chats/{random_string}.txt")
    title_line = 'nomi;text\n'
    with open(file, 'a') as f:
        f.write(title_line)
    return file

def append_to_file(file, nomi: str, text:str):
    line = f'{nomi};{text}'
    with open(file, 'a') as file:
        file.write(line + '\n')

def read_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read()
    return data

def main():
    if 'state' not in st.session_state:
        st.session_state['state'] = 'init'
    cols = st.columns([1,3])
    with cols[0]:
        st.title("Nomi-Chatbot")
        st.write("This is a simple chatbot that can be used to interact with the Nomi API.")
    with cols[1]:
        st.image("./assets/robo_chat.webp", width=800)
    st.markdown('---')
    if 'topic' not in st.session_state:
        st.session_state['topic'] = random.choice(prompts['topics'])
        st.session_state['nomi1_key'] = 'patrick'
        st.session_state['nomi2_key'] = 'michael'

    topic = st.text_area(
        "****Enter the context of the discussion here:****", 
        value=st.session_state['topic']['topic']
    )
    num_exchanges = st.number_input(
        "Enter the number of exchanges you want to have:", 
        min_value=1, 
        max_value=MAX_NO, 
        value=10, 
        help="the more exchanges, the slower the answer will be"
    )

    cols = st.columns(2)
    nomi1 = nomi_dict[st.session_state['nomi1_key']]
    nomi2 = nomi_dict[st.session_state['nomi2_key']]
    with cols[0]:
        nomi1_key = st.selectbox(
            f"**Select the first Bot {nomi1['icon']}:**", 
            options=list(nomi_name_dict.keys()),
            format_func=lambda x: nomi_name_dict[x],
        )
        nomi1_backstory = st.text_area(
            f"**Enter the backstory for {nomi_name_dict[nomi1_key]} here:**", 
            value = st.session_state['topic']['nomi1_backstory']
        )
    
    with cols[1]:
        nomi2_name_dict = {k: v for k, v in nomi_name_dict.items() if k != nomi1_key}
        nomi2_key = st.selectbox(
            f"**Select the second Bot {nomi2['icon']}:**", 
            options=list(nomi2_name_dict.keys()),
            format_func=lambda x: nomi_name_dict[x]
        )
        nomi2_backstory = st.text_area(
            f"**Enter the backstory for {nomi_name_dict[nomi2_key]} here:**", 
            value=st.session_state['topic']['nomi2_backstory']
        )
    
    nomi1 = nomi_dict[nomi1_key]
    nomi2 = nomi_dict[nomi2_key]
    
    if st.button("🚀 Start Chat"):
        cols = st.columns([1,11])
        file = create_file()
        st.session_state['file'] = file
        st.session_state['state'] = 'running'
        
        with st.spinner("Starting Chat..."):
            # make introduction, this is not shown to the user
            nomi1_response = prompts['intro'].format(name=nomi1['name'], partner=nomi2['name'], topic=topic, backstory=nomi1_backstory)
            # nomi1 responds to my introduction
            st.markdown(f'{nomi1['icon']} {nomi1['name']}: {get_response(nomi1, nomi1_response)}')
            # nomi2 responds to my introduction, this starts the conversation
            response = prompts['intro'].format(name=nomi2['name'], partner=nomi1['name'], topic=topic, backstory=nomi2_backstory)
            # now it is up to Nomi 1 to respond and the conversation starts
            request_nomi = nomi1
            for i in range (num_exchanges):
                # make sure that during the last exchange the conversation is ended with a goodbye
                if i < (num_exchanges -1):
                    response_nomi = nomi1 if request_nomi == nomi2 else nomi2 
                    request_nomi = nomi1 if response_nomi == nomi2 else nomi2
                    # request_nomi to reponse_nomi
                    response = get_response(response_nomi, response)
                    st.markdown(f'{response_nomi['icon']} {response_nomi['name']}: {response}')
                    append_to_file(file, response_nomi['name'], response)
                    # response_nomie to request_nomi
                    response = get_response(request_nomi, response)
                    st.markdown(f'{request_nomi['icon']} {request_nomi['name']}: {response}')
                    append_to_file(file, request_nomi['name'], response)
                    # slow down the conversation for many exchanges, 1 sec per 10 exchanges
                    time.sleep(num_exchanges // 10)
                else:
                    prompt = f"Thank {response_nomi['name']} for the conversation and say goodbye. (End of RP)"
                    response = get_response(response_nomi, prompt)
                    st.markdown(f'{response_nomi['icon']} {response_nomi['name']}: {response}')
                    response = get_response(request_nomi, response)
                    st.markdown(f'{request_nomi['icon']} {request_nomi['name']}: {response}')
                    append_to_file(file, request_nomi['name'], response)

            st.session_state['state'] = 'done'
    
    if st.session_state['state'] == 'done':
        text = read_file(st.session_state['file'])
        st.download_button(
            label="Download the text file",
            data=text,
            file_name=str(st.session_state['file']),
            mime="text/plain"
        )
    st.expander(f"ℹ️ About v{__version__}", expanded=False).markdown(prompts['info'])

if __name__ == "__main__":
    main()


