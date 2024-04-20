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
  {"role": "user", "content": "Aufgrund des Protokolls, was ist die Lehrstelle für welche Felix sich interessiert?"
                              f"Protokoll (angefügt in ```): ```{contents}```"
                              
                              },
  {"role": "user", "content": "Was ist die Lehrstelle welche Felix sich interessiert?"},
  {"role": "assistant", "content": "Felix interessiert sich für eine Lehrstelle im Coiffeur-Bereich."},
  {"role": "user", "content": "Hat jemand die Bewerbungsunterlagen mit ihm angeschaut?"},
  {"role": "assistant", "content": "Ja, Carmen hat mit Felix die Bewerbungsunterlagen aufbereitet."},
  # {"role": "user", "content": "Wann wurde das protokolliert?"}
  # {"role": "user", "content": "Ist er Vegetarier?"}
  # Es gibt keine Informationen, die darauf hindeuten, dass Felix Vegetarier ist.
  # {"role": "user", "content": "Wovon hat er Angst?"}

  # {"role": "user", "content": "Was sollen wir von Felix in einem halben Jahr erwarten? Gib mir 2 Vorschläge."}
  # In einem halben Jahr könnten wir von Felix erwarten, dass er entweder eine Lehrstelle im Coiffeur-Bereich gefunden hat oder dass er ein Praktikum absolviert, um sich weiter zu qualifizieren.

  {"role": "user", "content": "Schreib mir einen Abschlussbericht mit Ausgangslage, Entwicklungsverlauf, Evaluation des Programs und Empfehlungen."}
  # **Abschlussbericht für Felix**\n\n**Ausgangslage:**\nFelix startete im Programm mit einer beeindruckenden Lernbereitschaft und schnellen Auffassungsgabe. Er zeigte sich anfangs zurückhaltend, aber interessiert am Arbeitsplatz und im sozialen Umfeld.\n\n**Entwicklungsverlauf:**\nFelix konnte sich gut in das Arbeitsumfeld einfinden und arbeitete zügig an den vermittelten Kompetenzen. Er zeigte Eigeninitiative beim Lernen des 10-Finger-Systems und der Fremdsprache. Trotz persönlicher Herausforderungen wie einem abgebrochenen Praktikum bewies er Durchhaltevermögen und Engagement.\n\n**Evaluation des Programs:**\nFelix profitierte von der Unterstützung im Programm, insbesondere bei der Bewerbungsvorbereitung und dem Training für Vorstellungsgespräche. Er fühlte sich in der Arbeitsumgebung wohl und schätzte das positive Arbeitsklima.\n\n**Empfehlungen:**\n1. Fortführung der Unterstützung bei der Auffrischung des 10-Finger-Systems und der Fremdsprache.\n2. Weiterhin gezielte Begleitung bei Bewerbungsaktivitäten und Vorstellungsgesprächen.\n3. Förderung von Selbstvertrauen und Umgang mit persönlichen Herausforderungen.\n4. Betonung der Stärken und positiven Entwicklungsschritte von Felix für zukünftige berufliche Chancen.\n\nMit freundlichen Grüßen,\n[Dein Name]
  ]
)

print(completion.choices[0].message)

# output:
# Ja, Carmen hat mit Felix die Bewerbungsunterlagen aufbereitet.

# extrakt aus dem Protokoll
# 22. Februar
# Carmen bereitet mit Felix die Bewerbungsdokumente auf. Er zeigt sich dabei sehr selbständig, liefert eine gute Qualität und hält Termine exakt ein. Er freut sich über das positive Feedback und nimmt Verbesserungsvorschläge an.


# output:
# Das Protokoll wurde am 11. Januar 2020 um 10:08 Uhr erstellt.
# => dies ist womöglich falsch oder richtig, je nachdem wie das Datum interpretiert wird?
