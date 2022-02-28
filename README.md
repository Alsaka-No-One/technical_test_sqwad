# Installation
## Using docker
1. On a terminal open the project
2. `cd` into the API folder
3. run `docker build -t api_sqwad .` to build the image
4. run `docker run -dp 5000:5000 api_sqwad` to start the container

# How to use it
1. Open a web browser
2. Enter `localhost:5000` on the URL section
3. To see if a website is a shopify site, enter `localhost:5000/is_shopify/?link=<url>`
    - `<url>` = The website you want to check. The link must be encode !
4. Example:
    - `localhost:5000/is_shopify/?link=https%3A%2F%2Fwww.perus.co%2F` to check `https://www.perus.co/`
    - `localhost:5000/is_shopify/?link=https%3A%2F%2Fwww.youtube.com` to check `https://www.youtube.com`