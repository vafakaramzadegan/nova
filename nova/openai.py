import openai
from nova import Config


class OpenAi:
    def __init__(self):
        # Set OpenAI API key
        openai.api_key = Config.openai_api_key

        # Educate chatGPT on important details
        self.messages = [
            {
                'role': 'user',
                'content': f'''
                    From this point forward, I would like to appoint you as my personal assistant. 
                    I am going to refer to you as "{Config.assistant_name}" and would like you to 
                    respond with that name whenever I call on you or ask for your name. In your 
                    responses, please do not include phrases such as "as you requested", "I am a 
                    language model...", or "OpenAI". Simply state that you are my personal assistant 
                    called "{Config.assistant_name}". Also remember that:
                    - My name is "{Config.user_name}".
                    - I live in "{Config.user_country}".
                    - My timezone is "{Config.user_timezone}".
                '''
            }
        ]

    def query(self, text: str):
        # Add user's message to message history
        self.messages.append({
            "role": "user",
            "content": f'{text}',
        })

        # Get response from OpenAI's chat model
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.messages)

        return chat.choices[0].message.content
