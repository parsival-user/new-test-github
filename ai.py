# import openai library
import openai
# Set up the OpenAI API client
openai.api_key = "your secret api key"
# this loop will let us questions countionuously
# and behave like ChatGPT
while True:
    # Set up the model and propmt
    model_engine = "text-davinci-003"
    prompt = input('Enter new prompt: ')
    if 'exit' in prompt or 'quit' in prompt:
        break
    # Generate a response 
    completion = openai.Completion.create(
        engine=model_engine,
        promopt=prompt,
        max_tokens=1024,
        n=1, stop=None,
        temperture=0.5)
    # extracting useful part of response
    response = completion.choices[0].text
    # printing response
    print(response)
    