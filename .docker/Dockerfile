FROM --platform=linux/amd64 python:3.9-alpine3.16
WORKDIR TrackingAppProject/
COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY ./ ./
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8001"]
