# SchreibEsel

More details on the hackathon project: https://bd.hack4socialgood.ch/project/86

Presentation (in German): [Slides](/slides.pdf)

Source material: [anonymized journal entries](/anonyme%20Daten_X%20(ohne%20Bericht%3B%20nur%20Akteneinträge).docx)

Final report: [report](/KI%20in%20Sozialberichte%20Hack4SocialGood.docx)

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
