FROM python:3.6

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD [ "python", "./train.py GSPC 10 1000" ]

