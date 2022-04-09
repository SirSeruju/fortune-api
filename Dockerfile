FROM python:3-slim

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt &&\
    rm requirements.txt

COPY ./fortune-api /fortune-api
WORKDIR /

ENTRYPOINT ["uvicorn", "fortune-api.main:app"]
CMD ["--host", "0.0.0.0"]
