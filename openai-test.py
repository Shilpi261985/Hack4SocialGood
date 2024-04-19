from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system",
     "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming in german."},
    {"role": "assistant", "content": "In der Welt der Codes und Zahlen funkeln,Liegt ein Konzept, das uns fesselt und soll uns tränken. Rekursion genannt, in der Tiefe versteckt, Wie ein Geheimnis, das uns nach Wissen streckt.  Ein Ausdruck, der sich selbst ruft im Bann, Tief eingeschrieben im Programmcodeplan. Wie ein Spiegel, der sich selbst reflektiert, Im unendlichen Abgrund verirrt.  Schicht um Schicht, steigt die Funktion empor, Bis die Basis erreicht, wie ein heiliger Chor. Die Schleifen verschwinden, der Weg ist klar, Rekursion, stolz wie ein leuchtender Sternenaltar.  Gleiten wir durch diese tiefen Bahnen, Rekursion - ein Tanz der unendlichen Spannen. Ein Konzept so kraftvoll, so klar und rein, In der Welt der Programmierung – ein schillernder Schein."},
    {"role": "user", "content": "kürze es auf 10 wörter"}]
)

print(completion.choices[0].message)