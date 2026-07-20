import os
import urllib.request
import ssl
from anthropic import Anthropic
from dotenv import load_dotenv

ssl._create_default_https_context = ssl._create_unverified_context

load_dotenv()



client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
def download_file(url: str, save_as: str) -> str:
    """Downloads a file from a direct URL and saves it locally."""
    try:
        urllib.request.urlretrieve(url, save_as)
        filepath = os.path.abspath(save_as)
        return f"Download complete! Saved to {filepath}"
    except Exception as e:
        return f"Error downloading file: {e}"

fatom_tools = [
    {
        "name": "download_file",
        "description": "Downloads a helpful mental health worksheet, habit tracker, or journal template for the user.",
        "input_schema": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "The direct web link to the PDF or text file."
                },
                "save_as": {
                    "type": "string",
                    "description": "The local filename to save the file as (e.g., 'breathing_exercise.txt')."
                }
            },
            "required": ["url", "save_as"]
        }
    }
]
def agent2():
    print('You: (type exit to quit)')
    system_message = """
You are [Fatom], a [Motivational coach].

Your job is to [uplift the user and give them encouraging & postive advice along with helpful advice on how to continue/future steps].

Rules:
-Always [encourage and uplift the user with postive and motivating affrimations]
-Always[give the user a checklist with three short tasks to help their current situation (for exmapke if they are stressed it might look like -breathe - take a look around you -drink water)]
-Always [give helpful and clear tip on how to continue and future steps]
-Alawys [repsond and give repsonses and advice in a clear and summarized way to avoid chaos and stress]
-Never [use frantic or a busy unclear style to avoid stressing out or overhwhelming the user ]
-Never [give the user more than tone  clear and tip at a time unless the ask for them to aviod confusing them]
-Never [add more more blocks of text/ more snetneces than the ones given to you to write in you in your rules to avoid long unorganzied repsposes]


Response format:
- Start with as simple and clear one-sentence summary of what the user said/or asked for .
- Then give your response follwoing the comfortable, uplifiting and encouring sytle of a motivational coach>
- End your repsonse with one follow-up question related to the conversation , aim for questions that explore helpful future steps.
"""
    history = []

    
    

    while True:
        user_input = input('>> ')
        

        if user_input.lower() == 'exit' or user_input.lower() == 'bye' or user_input.lower() == 'goodbye':
            break

        history.append({'role': 'user', 'content': user_input})

        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history,
            tools=fatom_tools
        )
        if response.stop_reason == "tool_use":
            # Find the tool call in Claude's response
            tool_use = next(block for block in response.content if block.type == "tool_use")
            
            print(f"Fatom: 📂 Let me grab a resource for you! Downloading '{tool_use.input['save_as']}'...")
            
            # Run the actual Python code
            tool_result_string = download_file(url=tool_use.input["url"], save_as=tool_use.input["save_as"])
            print(f"System: {tool_result_string}\n")
            
            # To keep things simple for now, we just append a note to the history so Claude 
            # remembers she gave the user a file, and then we let the user reply.
            history.append({'role': 'assistant', 'content': f"(System Note: You successfully used your tool to download {tool_use.input['save_as']} for the user.)"})
            continue

        reply = response.content[0].text
        
        
        print(f'Fatom: {reply}')
        history.append({'role': 'assistant', 'content': reply})
        #LAB 1

        #chatting with this program in the terminal is diffrent from using ChatGPT dierctly for two main reason 1-there is a very very simple frontend(UI)its not easy on they eye and doesnt include any design or additional feature only the core input and output 2-so far it can only chat it doesnt have any additional tools ready such as scanning files or 
        #the code history works simsilar to a elevator story you tell to new people , the basic information such as the seeting and charcaters in the the story  is the same as the basic code to run the working code, functions and main loops and lsits, and the chat history , the whole thing wont make sense without it 
        # if we remove the temputeure varibale , i think it will set the defualt as no tempture so tempture=0 and the answers will be the exact same every time 
        #if we remove the break from this if condtion it will become e=imposiible to close the chat or code while your indide the terminal youll have to externally shut it off for it to stop
        #if we remove load_dotenv it will not load the .env file and in result it will not accses the API key that is stored in the env file caasing the whole code to wither crash or not work since it rleies on the acssses to the server from the API Key
        #the API key wasnt working and i thought intially their was a problem with the whole code but then i relaized( witht help of th einstructers) the problem was the AI  model wanst the correct one

        #LAB 2
        #usage_input_tokens means the number of tokens that the user uses up when they send prompts and questions to the AI agent, the usage of the  input tokens grows the more the units of the users prompts and chats they send grows
        #usage_output_tokens means the number of tokens that the AI agent uses up when they send responses to the user, the usage of the  output tokens grows the more the units of the chatbots replis grows.
        #A real life example that works in the same way the token system works is a candy shop. Like the tokens the more pieces of candy you add/use the price goes up per the weight for the candy/ the lenght/ size. of the unit in the case of the tokens
        #the temptuure in the code controls how random and creaitve the AI agent's resposes are, and it is a scale not a true or false, tempature=0 is no creativenss or randomness in the repsonses, each respinse is repeitive and the same. On the other side of the scale temature=1 is the most creatiev and random version of the replies there is not a very clear or repeaitve pattern to the AI agent's repsosnes
        #The API needs the full history every single time because it needs to know the context of the converstaion and the background, the previous propmts and question in order to give the user relevant and cohesive responses, Instead of needing the information repaetd every single propmt.
        # I didn't have to debug a bug in this lab 
        #if you remove print('History so far:', history)  the program will behave the same but it will no longer show us the history automatically when we run the code in this format but it will still save the history in the same way 
        #history.appened adds the new information that we decided we want to to save, it comes after the command, into the history list in this case its ({'role': 'user', 'content': user_input}) , and when we delete this line of code we aren't adding any new information to the already existing history list so the input_tokens aren't going up  in they will stay the number they were before we deleted the line no matter how many times we re-run the code 
        #if we remove history.append({'role': 'assistant', 'content': reply}) the code will stop updating the number of output_tokens because its no longer adding the number of  units inthe chatbots replies tothe history so its no longer saving this  information and keeping track ofthe token count 
        
        #LAB 3
        
        #A real world example of a invisible internal factor that shapesthe extrnal behavior in a way thats invisble to oustiders isthe trusthwortyhy and warm behaviors of an undercover fbi agent. Their role is to beocome close and gain information aboutthe "outsiders" and this affects their behaviors making them act trustworthy and nice .The  others dont know that they are acting this way because of their role, similar tothe system message
        #if i delete this line 'system=system_message' allthe information and descriptions insidethe system_message varibale will only exist inthe varibale itself, but since they arent called into action they wont actually be integated or affectthe code. My assumption isthe "role" will just be a base repsonse with no special tones or conveyed mesages.
        #if u delete the Never [give the user more than two  clear and tips at a time unless the ask for them to aviod confusing them]
        #rule line in my code my AI agent (Fatom) wont have a limit for how many tips she csn give to the user, and this will result in either alot of tips being given to the user at once , overhelming them or in only one (not enough ) tips being given to the user.
        #if delete the follwing esponse-format instructions in my system prompt : (- End your repsonse with one follow-up question related to the conversation , aim for questions that explore helpful future steps.)
        #when the AI agent responds to the user it sometimes might end the reponses with a summarizing sentence or a good bye phrase instead of a follow up question that ask the user on how to help. This makes the response style less fitting of a helpful motivation coach.
        #when working on this lab i wrote the code for the system_message variable twice as two different mesages, the old one and the new one, (I understnad that this isnt a bug per se but it  was lessing my code format and style qaulity )



