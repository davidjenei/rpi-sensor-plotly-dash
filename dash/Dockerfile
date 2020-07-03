FROM debian:buster-slim

WORKDIR /usr/src/app

# Hallo? Where is my pandas armv7 wheel? I got no time for that.
RUN apt-get update && apt-get install -y --no-install-recommends python3-pandas python3-pip python3-setuptools python3-brotli python3-wheel

#COPY requirements.txt .
#RUN pip3 install --user -r requirements.txt
RUN pip3 install dash

COPY . .

CMD [ "python3", "-u","./dash-app.py" ]
