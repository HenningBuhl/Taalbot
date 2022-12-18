# Use python.
FROM python:3.10

# Install dependencies.
COPY requirements.txt .
RUN pip install -U pip
RUN pip install -r requirements.txt

# Setup a working directory and copy the source code to it.
RUN mkdir -p /usr/src/bot
WORKDIR /usr/src/bot
COPY src/ /usr/src/bot

# Run main.py when started as container.
CMD [ "python3", "main.py" ]
