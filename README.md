# Setup Instructions

(Please note that I have used a third party library for cofiguring quickbooks client along with intuit-oauth client. I have used them and modified them for my use case and don't own any copyrights for the same.)

1. To Clone the Repo:
   `https://github.com/sedhha/qb-oauth-python.git`
2. Cd into the root directory:
   `cd qb-oauth-python`
3. Setup the virtual Enviroment:
   `python -m venv quickbooksVenv`
4. Launch Virtual Enviroment
   For Linux:
   `source quickbooksVenv/bin/activate`
   For Windows:
   `quickbooksVenv/Scripts/activate`
5. Install [requirements.txt](requirements.txt)
   `pip install -r requirements.txt`
6. Get your all quickbooks credentials using oAuth 2.0 playground. Follow this [YT video](https://youtu.be/8ZFZhe2HoMY) for reference. Plug in these values to your [constants.py](constants.py).
7. You may now run [main.py](main.py) to see it in action. There are two functions to demonstrate fetching of customers and payments data. Note that Quickbooks API allows you to perform tasks beyond that as well.
8. In case you're looking for auto renewal of `refresh_token`, you may comment down in my YT video or raise a request here. I would love to put in a script for the same as well with full instructions.

Note: Please don't forget to update redirect_uri and environment in [constants.py](constants.py) in case you're shipping your app in production.

```
client_secrets = {
    "client_id": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "client_secret": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "redirect_uri": "https://developer.intuit.com/v2/OAuth2Playground/RedirectUrl",
    "environment": "sandbox"
}
```
