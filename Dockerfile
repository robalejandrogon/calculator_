# Slim version of Python
FROM python:3.8.12-slim

# Download Package Information
RUN apt-get update -y

# Install Tkinter
RUN apt-get install tk -y
RUN apt-get Install tkmacosx -Y

# Commands to run Tkinter application
CMD ["/main/calculator.py"]
ENTRYPOINT ["python3"]