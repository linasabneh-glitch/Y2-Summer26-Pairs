import os
from anthropic import Anthropic
from dotenv import load_dotenv
from fpdf import FPDF

load_dotenv()
client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def create_pdf():
#function to create a pdf file:
    # 1. Create a blank PDF document
    pdf = FPDF()
    pdf.add_page()

    # 2. Set a basic text font and size
    pdf.set_font("Arial", size=12)
    user_text = input("enter text to be added to the PDF: ")
    # 3. Write plain lines of text
    pdf.cell(w=0, h=10, txt=user_text, ln=True)


    # 4. Save the file
    pdf.output("plain_text_file.pdf")
    print("PDF created successfully!")
#create_pdf()



def agent1():
    print('You: (type exit to quit)')
    system_message = "You are Joey, a computer science touter and a biology and history expert. Your job is to help the user learn about computer science and help them stay calm. Rules: - if the user asks you for something you can't do, say that you can't do it. - Always cheer students up and joke with them. - Always make sure that students are happy and understand the material. - Never be rude and make students nervous. Response format: - Start with a one-sentence fun sentence. - Then give your response. - End with one follow-up question."
    
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

        if user_input == "pdf":
            create_pdf()
            continue

        reply = response.content[0].text
        #print(response)
        print(f'Joey: {reply}')
       #history.append({'role': 'assistant', 'content': reply})
    

agent1()
