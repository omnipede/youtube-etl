import os

from youtubetl.impl.utils import convert_to_wav_and_subclip, ydl_download


class AudiosetYoutubeClip:
    def __init__(self, youtube_id: str, start: int, end: int, output_dir: str):
        self.youtube_id = youtube_id
        self.start = start
        self.end = end
        self.output_dir = output_dir

    def download(self):
        # Simply download video metadata
        video_metadata = ydl_download(self.youtube_id)
        video_url = video_metadata['url']
        video_duration = video_metadata['duration']

        if video_duration < self.end:
            raise Exception(f"Video duration of {self.youtube_id} is shorter than end time {self.end}")

        # Download and subclip from url
        self._download_and_subclip(video_url)

    def _download_and_subclip(self, url: str):
        file_name = f"{self.youtube_id}_{self.start}_{self.end}.wav"
        output_path = os.path.join(self.output_dir, file_name)
        convert_to_wav_and_subclip(url, output_path, self.start, self.end)