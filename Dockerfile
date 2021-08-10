FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt


# ADD . .

# EXPOSE 8000

# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "chat.wsgi:application"]

# CMD gunicorn chat.wsgi:application --bind 0.0.0.0:$PORT