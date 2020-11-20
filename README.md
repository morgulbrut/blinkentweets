# blinkentweets

A bit of python to visualize tweets on a fadecandy installation.

## setup

You need a running fadecandy server (https://github.com/scanlime/fadecandy).

### tweepy settings
1. Rename `settings_example.py` to `settings.py` and fill out the data.
2. Edit `hashtags.py`
 
### setup systemd service

1. Make sure you run fcserver as a systemd service (https://github.com/scanlime/fadecandy/tree/master/examples/systemd).
2. There are two .service files, one `tweets.service` is just the python, while `tweets_au.service` uses `start_tweets.sh` to first pull this repo.
3. Install one of them the same way, as it's described in the fadecandy docu.
