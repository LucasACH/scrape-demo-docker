FROM python:3.9-buster


RUN pip install requests bs4 lxml

COPY . .

CMD ["python", "./app/scraper.py"]