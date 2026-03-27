FROM python:3.10.20-slim AS builder

WORKDIR /app

COPY api/requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

COPY api/ ./api

FROM python:3.10.20-slim AS runner

WORKDIR /app

COPY --from=builder /install /usr/local

COPY --from=builder app/api ./api

EXPOSE 5000
CMD [ "python", "api/app.py" ]