import subprocess
import youtube_dl


def download_and_subclip(url: str, output_path: str, start: int, end: int) -> None:
    """
    URL 에서 파일을 다운로드 하고 start ~ end 로 clipping 하는 메소드
    :param url: 대상 URL
    :param output_path: 다운로드 경로
    :param start: 시작 시간
    :param end: 끝 시간
    :return: None
    """

    subprocess.call(
        f'ffmpeg -y -ss {start} -to {end} -i "{url}" -preset veryfast "{output_path}" ',
        shell=True,

        # Disable console logging
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
    )


def convert_to_wav_and_subclip(url: str, output_path: str, start: int, end: int) -> None:
    """
    URL 에서 파일을 다운로드하고 wav 로 변환한 뒤 start ~ end 로 clipping 하는 메소드
    :param url: 대상 URL
    :param output_path: 다운로드 경로
    :param start: 시작 시간
    :param end: 끝 시간
    :return: None
    """

    # Clip video from start to end
    # Change to wav file
    subprocess.call(
        f'ffmpeg -y -ss {start} -to {end} -i "{url}" -vn -acodec pcm_s16le -preset veryfast -ar 22050 '
        f'-ac 1 "{output_path}"',
        shell=True,

        # Disable console logging
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
    )


def ydl_download(youtube_id: str):
    url = 'http://www.youtube.com/watch?v=' + youtube_id
    ydl = youtube_dl.YoutubeDL({
        # Disable logging
        'quiet': True,
        'outtmpl': '%(id)s.%(ext)s',
        'format': 'best'
    })

    with ydl:
        result = ydl.extract_info(
            url, download=False
        )

    return result['entries'][0] if 'entries' in result else result
