FROM python:3.11-slim
WORKDIR /bookapp
COPY infra/requirements.txt .
RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt --no-cache-dir
COPY books_list .
RUN chmod +x start.sh
CMD ["./start.sh"] 