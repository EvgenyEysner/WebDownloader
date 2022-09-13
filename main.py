import requests
from pytube import YouTube

url="https://www.youtube.com/watch?v=gvYGIhuiJQI"

yt = YouTube(url)

# for video in yt.streams.filter(progressive=True, file_extension='mp4'):
#     video.download()

for video in yt.streams.filter(only_audio=True):
    print(video)

# def download_video(url):
#     try:
#         response = requests.get(url)
#         with open("reg_video.mp4", "wb") as file:
#             for chunk in response.iter_content(1024 * 1024):
#                 if chunk:
#                     file.write(chunk)
#         return "Video successfully downloaded!"
#     except Exception as e:
#         return "Upps ... check the URL please!"
#
#
# def main():
#     download_video(url)


# if __name__ == "__main__":
#     main()