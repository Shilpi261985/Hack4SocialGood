from openai import OpenAI
client = OpenAI()

# Open the file in read mode ('r')
with open('anonyme_daten.txt', 'r') as file:
    # Read the entire contents of the file
    contents = file.read()
    # Do something with the contents, such as printing them
    # print(contents)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  temperature=0,
  messages=[
  {"role": "system",
    "content": "You are helpful assistant helping a social worker trying to make sense of journal entries. Be brief and to the point"},
  {"role": "user", "content": "What are the names of the people mentioned in the journal entries? just give me all their names"
                              f"journal entries (enclosed in ```): ```{contents}```"
                              
                              },
  {"role": "user", "content": "Please give me all the names of the people mentioned in the journal entries."}]
)

print(completion.choices[0].message)

# Output:
# ChatCompletionMessage(content='- Felix\n- Sandra\n- Klaus\n- Carmen\n- Helen\n- Theodor', role='assistant', function_call=None, tool_calls=None)