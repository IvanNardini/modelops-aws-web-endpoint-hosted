
FROM conda/miniconda3:latest

LABEL Python - score app

USER root

COPY . /app

RUN pip install --upgrade pip;
    
RUN pip install -r requirements.txt;

WORKDIR /app

ENV FLASK_APP=app.py

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
