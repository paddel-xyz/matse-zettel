# Use the pandoc/latex base image
FROM pandoc/latex:2.19-ubuntu

# Set the working directory
WORKDIR /matse-zettel/

RUN apt update && apt install -y python3 pip

RUN tlmgr install tcolorbox
RUN tlmgr install environ

# Copy only the requirements.txt file
COPY util/latex/requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT /bin/bash