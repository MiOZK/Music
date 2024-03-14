from AFROTOMusic.core.bot import Zelzaly
from AFROTOMusic.core.dir import dirr
from AFROTOMusic.core.git import git
from AFROTOMusic.core.userbot import Userbot
from AFROTOMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Zelzaly()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()