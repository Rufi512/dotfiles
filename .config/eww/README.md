# EWW

Config based from https://github.com/adi1090x/widgets

## Before running
1. **Email**: To make the e-mail indicator work you can configure the "mails" script and set the parameters of the mail service you use

2. **Player indicator**: The player uses playerctl to get the song information and amixer to controller the volumen master, make sure it is installed.

3. **Forecast**: the forecast is connected from the openweathermap api, make sure to set the API_KEY and the CITY_ID

Your can set the params necessary to use how enviroment variable in your .xprofile

These are the ones used

| KEY  | VALUE |
| ------------- | ------------- |
| USER_MAIL  | Your user from email  |
| USER_MAIL_PASSWORD  | Your password |
| API_KEY_WEATHER  | API key from openweathermap |
| CITY_WEATHER  | Your city id from openweathermap|

<img src="https://github.com/Rufi512/dotfiles/blob/main/.config/eww/screenshot.png" alt="eww"/>

**Player**

<img src="https://github.com/Rufi512/dotfiles/blob/main/.config/eww/player.png" alt="eww-player"/>

## Notes

The player uses a script to get the most dominant colors of the cover image only when you click to open, the contrast colors can sometimes be displayed incorrectly, is something to fix :p
