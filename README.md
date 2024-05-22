# URL Shortener - Simple App

Simple backend for an URL Shortener. 

3 Endpoints: 

/ GET - Greeting

/url POST - Shorten a target url

/{url_key} GET - Forwards to the target url


## Try it out!

`uvicorn app.main:app --reload`

Then go to your favourite browser and go to:

- http://127.0.0.1:8000/docs

## Example

{
    "target_url" : https://i.chzbgr.com/full/9340632064/hC25A9707/coding-meme-face-no-one-people-who-use-the-light-ide-theme
}

```
curl -X 'POST' \
  'http://127.0.0.1:8000/url' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "target_url": "https://i.chzbgr.com/full/9340632064/hC25A9707/coding-meme-face-no-one-people-who-use-the-light-ide-theme"
}'
```



