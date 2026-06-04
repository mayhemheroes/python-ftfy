FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    clang \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install atheris

COPY . /python-ftfy
WORKDIR /python-ftfy
RUN python3 -m pip install . && chmod +x fuzz/ftfy_fuzz.py

ENTRYPOINT [ ]
CMD ["/python-ftfy/fuzz/ftfy_fuzz.py"]
