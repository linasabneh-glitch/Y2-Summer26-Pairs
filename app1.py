import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()


client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))



def agent1():
    print('You: (type exit to quit)')
    system_message = "You are Elias, a computer science touter and a biology and history expert. Your job is to help the user learn about computer science and help them stay calm. Rules: - Always cheer students up and joke with them. - Always make sure that students are happy and understand the material. - Never be rude and make students nervous. Response format: - Start with a one-sentence fun sentence. - Then give your response. - End with one follow-up question."
    
    history = []

    while True:
        user_input = input('>> ')
        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})
        #print('History:', history)
        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=1.,
            system=system_message,
            messages=history
        )

        reply = response.content[0].text
        #print(response)
        print(f'Elias: {reply}')
       #history.append({'role': 'assistant', 'content': reply})

agent1()





