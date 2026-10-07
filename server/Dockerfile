FROM python:3.11-slim-bookworm AS build
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --target=/install -r requirements.txt

FROM gcr.io/distroless/python3-debian12:nonroot
WORKDIR /server
COPY --from=build /install /server/deps
COPY main.py .
ENV PYTHONPATH=/server/deps
EXPOSE 8000
USER nonroot
CMD ["-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]