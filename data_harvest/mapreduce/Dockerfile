FROM python:3.8.10
COPY package_version.txt package_version.txt
COPY real_view.py real_view.py
COPY api.json api.json
RUN pip3 install --upgrade pip
RUN pip3 install -r package_version.txt
COPY . .
CMD [ "python3", "real_view.py"]

