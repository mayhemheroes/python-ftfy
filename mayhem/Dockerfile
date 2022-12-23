FROM python:3.8-bullseye
RUN pip3 install atheris

COPY . /python-ftfy
WORKDIR /python-ftfy
RUN python3 -m pip install . && chmod +x fuzz/ftfy_fuzz.py

ENTRYPOINT [ ]
CMD ["/python-ftfy/fuzz/ftfy_fuzz.py"]