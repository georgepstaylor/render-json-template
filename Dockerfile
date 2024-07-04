FROM gcr.io/distroless/python3-debian12
ENV PYTHONPATH "${PYTHONPATH}:/usr/app"
WORKDIR /usr/app
COPY entrypoint.sh entrypoint.sh
COPY render_json/requirements.txt .
RUN pip install -r requirements.txt
COPY render_json/ render_json/
ENTRYPOINT ["/usr/app/entrypoint.sh"]
