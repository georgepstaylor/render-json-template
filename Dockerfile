FROM python:3.10.5-alpine
WORKDIR /usr/app
COPY entrypoint.sh entrypoint.sh
COPY render_json/requirements.txt .
RUN pip install -r requirements.txt
COPY render_json/ render_json/
ENTRYPOINT ["/usr/app/entrypoint.sh"]
