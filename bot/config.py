#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("APP_ID", default="4560655", cast=int)
    API_HASH = config("API_HASH", default="ce54eacb9b6854768b06daa2864e88fa")
    BOT_TOKEN = config("BOT_TOKEN", default="1683813493:AAGblEajkItME8QcFY8PmcSVOfZoEA00jKg")
    DEV = 1322549723
    OWNER = config("OWNER", default="1446111611 682111519")
    FFMPEG = config("FFMPEG", default="ffmpeg -i '''{}''' -map 0 -c copy -c:v libx265  -s 1280x720  -preset fast  -crf 20 -c:a aac -b:a 192k -metadata title="Sonic Otakus" -pix_fmt yuv420p -metadata:s:a title="Sonic Otakus" -metadata:s:s title="Sonic Otakus" '''{}''' -y"
    )
    THUMB = config(
        "THUMBNAIL", default="https://telegra.ph/file/a1cb73168488b99c975bb.jpg"
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
