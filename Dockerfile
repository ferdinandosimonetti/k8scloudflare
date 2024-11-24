FROM python:3.12-slim-bookworm
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY main.py .
ENTRYPOINT [ "/bin/sleep","infinity" ]