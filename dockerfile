FROM python:3
RUN apt-get update && apt-get install -y unzip

# Japanese Localization
RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

# google-chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add && \
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list && \
apt-get update && \
apt-get install -y google-chrome-stable

# ChromeDriver
ADD https://chromedriver.storage.googleapis.com/92.0.4515.43/chromedriver_linux64.zip /opt/chrome/
RUN cd /opt/chrome/ && \
unzip chromedriver_linux64.zip

# python package
RUN pip install selenium && \
pip install bs4 && \
pip install oauth2client

ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/chrome