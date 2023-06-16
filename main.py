import openai

openai.api_base = "http://localhost:4891/v1"
# openai.api_base = "https://api.openai.com/v1"

openai.api_key = "not needed for a local LLM"

# Set up the prompt and other parameters for the API request
prompt = "Write me a text prompt for a text-to-image of a girl with a school uniform which would be perfect for 16:9 using Stable-diffusion prompt formula"

# model = "gpt-3.5-turbo"
# model = "mpt-7b-chat"
model = "ggml-gpt4all-j-v1.3-groovy.bin"

messages=[
        {"role": "system", "content": "act as prompt generator ,i will give you text and you describe an image that match that text in details, answer with one response only"},
        {"role": "user", "content": prompt}]

# Make the API request
response = openai.Completion.create(
    model=model,
    messages=messages,
    prompt=prompt,
    max_tokens=200,
    temperature=0.25,
    top_p=0.95,
    n=1,
    echo=False,
    stream=False
)

# Print the generated completion
print(response['choices'][0]['text'])
