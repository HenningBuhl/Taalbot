# Use python.
FROM python:3.10

# Setup a working directory and copy the source code to it.
RUN mkdir -p /usr/src/bot
WORKDIR /usr/src/bot
COPY src/ .

# Install dependencies.
# Required? RUN pip install -U pip
RUN pip install -r requirements.txt

# Run main.py when started as container.
CMD [ "python3", "main.py" ]
