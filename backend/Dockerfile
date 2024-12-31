# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the NLTK data directory
ENV NLTK_DATA=/usr/local/nltk_data

# Download NLTK data
RUN python -m nltk.downloader -d /usr/local/nltk_data punkt_tab
RUN python -m nltk.downloader -d /usr/local/nltk_data punkt
RUN python -m nltk.downloader -d /usr/local/nltk_data wordnet
RUN python -m nltk.downloader -d /usr/local/nltk_data omw-1.4

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]