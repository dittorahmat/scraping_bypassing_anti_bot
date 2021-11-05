# Scraping By Bypassing Anti Bot / Captcha

Most of the time, when you're doing web scraping at a bulk rate, you will find yourself blocked by either Anti Bot (Cloudflare, Perimeter X etc) or Captcha (ReCaptcha, H-Captcha etc). 

You tried Googling to find an API endpoint to query to, but no luck.

Afraid not !

My favorite way of bypassing anti bot or captcha is to find hidden API in your browser requests

While you are browsing the website you wanted to scrape, open developer tools
![alt text](https://curlconverter.com/images/screenshot.png)

Now the fun begins

Instead of finding the web page element, you are looking for the data requests you wanted

This repository is a sample of how I find an API endpoint and get the data from there, instead of web scraping.

Although I do still need rotating proxy, because the website blocks me for every several minutes.
