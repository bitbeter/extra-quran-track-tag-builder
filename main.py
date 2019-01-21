import logging
from os import listdir, path
from eyed3 import log, load
import json

log.setLevel(logging.DEBUG)

SURAH_JSON_PATH = "surah.json"
# TRANSLATION_PATH = "translations/fa.fooladvand.txt"
SOUNDS_PATH = "sounds"

ARTIST = "Sheikh Mishary Rashid Al-Afasy"
ALBUM = "Al-Qur'an"
GENRE = "Religious"
SURAH_COUNT = 114

ImageData = None
SurahData = dict()
# TranslationData = None

with open(SURAH_JSON_PATH, 'r') as f:
    SurahData = json.load(f)

with open(SURAH_JSON_PATH, 'r') as f:
    ImageData = f.read()

# with open(TRANSLATION_PATH, 'r') as f:
#     TranslationData = f.readline()

for sound_file in listdir(SOUNDS_PATH):
    try:
        index = int(sound_file[:3]) - 1
        sound = load(SOUNDS_PATH + "/" + sound_file)
        sound.tag.title = SurahData[index]['title']
        sound.tag.track_num = (index + 1, SURAH_COUNT)
        sound.tag.artist = ARTIST
        sound.tag.album = ALBUM
        sound.tag.genre = GENRE
        # sound.tag.images.set(3, ImageData, "image/jpeg", ALBUM)
        sound.tag.save()
    except ValueError:
        pass


# print()
