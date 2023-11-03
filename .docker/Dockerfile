FROM --platform=linux/amd64 python:3.9
WORKDIR TrackingAppProject/
COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY ./ ./
