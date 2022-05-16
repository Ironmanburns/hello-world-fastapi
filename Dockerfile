FROM python:3.8-slim-buster
WORKDIR /usr/src/app
COPY ["main.py", "requirements.txt", "./"]
RUN python -m pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "-m","uvicorn", "main:app"]