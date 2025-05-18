FROM python:3.13-alpine

WORKDIR /app
COPY requirements.txt .  
RUN --mount=type=cache,target=/root/.cache/pip pip3 install -r requirements.txt && \
    rm requirements.txt
COPY app.py .

ENV AUTHOR=okonow
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000

EXPOSE $FLASK_RUN_PORT

ENTRYPOINT ["sh", "-c"]
CMD ["gunicorn --bind $FLASK_RUN_HOST:$FLASK_RUN_PORT --workers 3 app:app"]