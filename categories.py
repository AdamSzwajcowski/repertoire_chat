from enum import Enum

categorylist = ['GREETINGS','REPERTOIRE','SONG_NAME','ARTIST_NAME',
                'TAG_NAME','THANKS','BYE']
Categories = Enum("Categories", categorylist)