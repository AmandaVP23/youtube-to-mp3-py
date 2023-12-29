import sys

from pytube import YouTube
import os
import subprocess


try:
    urlInputValue = ''

    lines = []
    with open('./musicList.txt') as f:
        lines = f.read().splitlines()

    for line in lines:
        yt = YouTube(line)

        # # download the file
        videoTitle = yt.title.replace('/', ', ')
        videoTitle = videoTitle.replace('\\', ', ')
        videoTitle = videoTitle.replace('?', '')
        # videoTitle = f"{yt.author} - {videoTitle}"
        videoTitle = f"{videoTitle} - {yt.author}"

        audio = yt.streams.get_audio_only()
        defaultFilename = videoTitle + '.mp4'
        audio.download(filename=f"{videoTitle}.mp4", output_path='./musics')
        musicFileName = videoTitle + '.mp3'
    
        subprocess.run(["ffmpeg", "-y", "-i", '.\\musics\\' + defaultFilename, '.\\musics\\' + musicFileName])
        subprocess.run(["del", '.\\musics\\' + defaultFilename], shell=True)

except KeyError:
    print("Unable to fetch video information. Please check the video URL or your network connection.")