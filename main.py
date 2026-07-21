import os
import urllib.request
import ssl
from fpdf import FPDF
from anthropic import Anthropic
from dotenv import load_dotenv



load_dotenv()

#class Agent:
    #def __init__(self,chosen_name):
        #self.name=chosen_name
        #self.messages_received=[]
    #def listen(self, incoming_message):
        #self.messages_received.append(incoming_message)
#agent_joey=Agent("Joey")
#agent_fatom=Agent("Fatom")

shared_history = []
client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
while True:

    user_option=input("Choose a chatbot to chat with: #1# Joey(a computer science, biology and history tutor) or  #2# Fatom( your motivation bestie))")
    if user_option == "1":
        print("Joey(your helpful tutor): ")
        from app1 import agent1
        agent1(shared_history)
        

    elif user_option == "2":
        print("Fatom(your motivational bestie): ")
        from app2 import agent2
        agent2(shared_history)
        
    elif user_option == "exit":
        print("goodbye!")
        break
    
    else:
        print("Invalid input. Please choose a chatbot")
        user_option=input("Choose a chatbot to chat with: #1# Joey(a computer science, biology and history tutor) or  #2# Fatom( your motivation bestie))")

    