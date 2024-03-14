"""
Script to dowload youtube videos
"""
from os import PathLike
import sys
from pytube import YouTube


MSG_ERROR = "You should provide with at least an URL or URL and a Output Path"
MSG_DOWNLOAD_ERROR = "An error occur during the download"


def tube_completed():
    """
    On Complete Calback fn
    """
    print("done")


def tube_download(video_url: str, path: str | PathLike = None,
                  on_complete_callback=None):
    """

    Args:
        url (_type_): _description_
    """
    yt = YouTube(video_url, on_complete_callback=on_complete_callback)
    yd = yt.streams.filter(file_extension="mp4").get_highest_resolution()
    filename = yt.title.replace(" ", "_").lower()
    download_path = yd.download(filename=f"{filename}.mp4",
                                filename_prefix="dwn-",
                                output_path=path)
    print(f"Dowloading {yt.title}, will be saved in {download_path}")


if __name__ == "__main__":
    args = sys.argv[1:]
    match args:
        case [url, *output_path]:
            try:
                filepath = output_path and output_path[-1]
                tube_download(url, path=filepath)
            except Exception as e:
                print(MSG_DOWNLOAD_ERROR, e, sep="\n")
        case _:
            print(MSG_ERROR)
