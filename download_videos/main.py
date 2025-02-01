from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "https://www.youtube.com/watch?v=aGCdLKXNF3w&list=PL81a-nPJyBNU5lJETkHCJ7BkYvCI3olBM"

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

ys = yt.streams.get_highest_resolution()
ys.download(output_path="videos")