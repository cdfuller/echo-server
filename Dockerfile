FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR app
COPY echo.py echo.py

EXPOSE 3246

CMD python echo.py -b 0.0.0.0
