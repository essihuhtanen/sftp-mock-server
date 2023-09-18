FROM ubuntu:latest
RUN apt-get update && apt-get install -y inotify-tools && apt-get install -y python3
COPY server_script.sh /app/server_script.sh
COPY createResponse.py /app/createResponse.py
WORKDIR /app

ENTRYPOINT ["/bin/bash", "server_script.sh"]
