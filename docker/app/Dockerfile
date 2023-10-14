FROM python:3.11

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app
EXPOSE 8080

# install and compile stock fish
RUN git clone https://github.com/official-stockfish/Stockfish.git
RUN cd Stockfish/src/ && make -j build