
FROM conda/miniconda3:latest

LABEL Scoring App = "Reccomendation System - Python - Surprise"

USER root

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

WORKDIR /app

ENV FLASK_APP=app.py

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
