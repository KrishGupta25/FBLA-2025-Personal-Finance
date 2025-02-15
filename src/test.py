from google import genai

client = genai.Client(api_key= "AIzaSyDyG06T5SrsTAA0xwKn8VKwBu-ETJp00PU")
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="I am a happy person"
)
print(response.text)