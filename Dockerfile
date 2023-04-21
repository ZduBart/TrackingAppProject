FROM python:3.10-alpine
WORKDIR TrackingAppProject/
COPY requirements.txt .
RUN pip3 install --upgrade pip && pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python3", "manage.py", "0.0.0.0:8000"]
