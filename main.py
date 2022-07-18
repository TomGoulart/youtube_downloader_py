import os
from pytube import Playlist
from pydub import AudioSegment

TMP_PATH = './.tmp'

PL_NAME = 'Amado Batista'
PL_LINK = 'https://www.youtube.com/watch?v=LWzwjcgh7_A&list=PLOianMAL8OzKqZeZp7SQMtZmbRO7EiRmt'

def plConvert():

    print('Iniciando Conversão...')

    musics = os.listdir( TMP_PATH )

    if not os.path.exists(PL_NAME):
        os.mkdir(PL_NAME) 

    for index, music in enumerate(musics):
        try:
            mp4 = AudioSegment.from_file(TMP_PATH + '/' + music[:-3] + 'mp4', "mp4")
            mp4.export(PL_NAME + '/' + music[:-3] + 'mp3', format="mp3")
            print('Convertido: %s (%s de %s)' % (music, index, len(musics)))
            os.remove(TMP_PATH + '/' + music)
        except:
            print('Erro ao converter %s' % music)


def plDownload(link):

    if not os.path.exists(TMP_PATH):
        os.mkdir(TMP_PATH) 

    playlist = Playlist(link)

    print('Iniciando download de %s músicas...' % len(playlist.video_urls))

    for index, video in enumerate(playlist.videos):
        try:
            video.streams.get_by_itag(140).download( TMP_PATH )
        except:
            print("Ocorreu um erro ao tentar baixar: %s" % video.title)

        print('Baixado: %s (%s de %s)' % (video.title, index, len(playlist.video_urls)))
    
    plConvert()


plDownload(PL_LINK)