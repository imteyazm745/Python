!pip -q install pytube

def youtube_audio_downloader(link):
    from pytube import YouTube
    import os
    import re
    if 'youtu' not in link:
        print('Invalid YouTube link!')
        return False
    
    yt = YouTube('video_link') # paste video url in place of video_link inside ''
    audio = yt.streams.filter(only_audio=True).first()
    print('Downloading the audio stream ....', end = '')
    output_file = audio.download()
    if os.path.exists(output_file):
        print('Done!')
    else:
        print('Error downloading the file!')
        return False
    
    basename = os.path.basename(output_file)
    name, extension = os.path.splitext(basename)
    audio_file = f'{name}.mp3'
    audio_file = re.sub('\s+', '_', audio_file)
    print(f'Renaming {basename} to {audio_file}')
    os.rename(basename, audio_file)
    return audio_file
mp3_file = youtube_audio_downloader('video_link') # paste video url in place of video_link inside ''
print(mp3_file)
