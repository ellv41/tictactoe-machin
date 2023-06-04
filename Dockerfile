FROM python:alpine3.17
WORKDIR /app
COPY . .
ENTRYPOINT [ "python" ]
CMD ["tictactoe.py" ]
