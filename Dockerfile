FROM python:3.10.5-alpine
COPY entrypoint.sh entrypoint.sh
WORKDIR /usr/app
COPY test.json .
COPY render_json/requirements.txt render_json/requirements.txt
RUN pip install -r render_json/requirements.txt
COPY render_json/ render_json
ENTRYPOINT ["/entrypoint.sh"]
