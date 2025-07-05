# Use official Python
FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN playwright install --with-deps

CMD ["python", "scraper.py"]
