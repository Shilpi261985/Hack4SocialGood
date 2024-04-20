# SchreibEsel

More details on the hackathon project: https://bd.hack4socialgood.ch/project/86

Presentation (in German): [Slides](/slides.pdf)

Source material: [anonymized journal entries](/anonyme Daten_X (ohne Bericht%3B nur Akteneinträge).docx)

Final report: [report](/KI in Sozialberichte Hack4SocialGood.docx)

Running the samples:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# create a .env file and ensure it contains
# OPENAI_API_KEY="...the api key..."
source .env
python openai-test.py
```
