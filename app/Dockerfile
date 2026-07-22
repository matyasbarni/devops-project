FROM python:3.11-slim
 
WORKDIR /app
 
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
 
COPY app.py /app/app.py
 
RUN useradd --create-home appuser
USER appuser
 
EXPOSE 8000
 
ENV PYTHONUNBUFFERED=1
ENV PORT=8000
 
CMD ["python", "/app/app.py"]