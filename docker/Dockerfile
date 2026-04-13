FROM python:3.10.20-slim AS builder

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

COPY app/ ./app

FROM python:3.10.20-slim AS runner

WORKDIR /app

COPY --from=builder /install /usr/local

COPY --from=builder /app/app ./app

EXPOSE 5000
CMD [ "python", "-m", "app.run" ]