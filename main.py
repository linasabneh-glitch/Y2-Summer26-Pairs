import os
import urllib.request
import ssl
from fpdf import FPDF
from anthropic import Anthropic
from dotenv import load_dotenv



load_dotenv()


client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
while True:

    user_option=input("Choose a chatbot to chat with: #1# Joey(a computer science, biology and history tutor) or  #2# Fatom( your motivation bestie))")
    if user_option == "1":
        print("Joey(your helpful tutor): ")
        from app1 import agent1
        agent1()
        break

    elif user_option == "2":
        print("Fatom(your motivational bestie): ")
        from app2 import agent2
        agent2()
        break

    else:
        print("Invalid input. Please choose a chatbot")
        user_option=input("Choose a chatbot to chat with: #1# Joey(a computer science, biology and history tutor) or  #2# Fatom( your motivation bestie))")

    