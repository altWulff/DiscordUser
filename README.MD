## Auto creator discord accounts
Automatically creates a discord account from command line arguments,
with auto generated password
and login into it, but captcha need solve to manually,
after login - display user token from headers "authorization" to command line

## TODO 
Display user token after login, from header "authorization"

## Setup

`$ git clone git@github.com:altWulff/DiscordUser.git && cd DiscordUser`

`$ virtualenv venv && source venv/bin/activate`

`$ pip install -r requirements.txt`

## Usage
`$ python src/main.py -username {USERNAME} -email {EMAIL}`