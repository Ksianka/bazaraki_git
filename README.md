#Telegram bot and parser for
**https://www.bazaraki.com/real-estate/houses-and-villas-rent/**

After you clone the project. 

####In oder to start your Telegram channel with Bazaraki rent adverts:

1. Get your Telegram bot token. You can create new one with Telegram Botfather.
see link for help - https://core.telegram.org/bots#6-botfather

2. Insert your bot token to the code: telegram_bot.py, line 6

3. Create Telegram Channel or use existing one. Add the bot as Administrator to it.

4. Insert name of the Telegram Channel to the code: telegram_bot.py, line 6

5. Get your Bazaraki search link for apartment/house/villa rent with
your selected filters. For example:
https://www.bazaraki.com/real-estate/houses-and-villas-rent/furnishing---1/number-of-bedrooms---2/type---5/lemesos-district-limassol/?price_max=1500

6. Insert your proper Bazaraki search link to the code: telegram_bot.py, line 12

7. Insert your web browser User-Agent info to the code: telegram_bot.py, line 11.
How to get this info - https://developers.whatismybrowser.com/useragents/parse/?analyse-my-user-agent=yes
or use your browser inspector mode

8. Decide about Redis server. 
Localhost - uncomment telegram_bot.py, line 15; or external platform, 
for example Heroku - use telegram_bot.py, line 14.
The initial project was built on Heroku. You can find proper Procfile in the project.

9. Decide about frequency of bot parsing and message sending. 
Current interval is 2 hours or 7200 seconds. For another interval
update parametr interval= in the code telegram_bot.py, line 35.

