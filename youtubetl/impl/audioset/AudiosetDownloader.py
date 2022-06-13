from youtubetl.core.domain.YoutubeClip import YoutubeClip
from youtubetl.core.usecase.download_clip import YoutubeClipDownloader
from youtubetl.impl.audioset.AudiosetYoutubeClip import AudiosetYoutubeClip


class AudiosetDownloader(YoutubeClipDownloader):

    def __init__(
        self,
        source_file_path: str,
        output_path: str,
        pool_size: int = 1,
    ):
        super().__init__(pool_size)
        self.source_file_path = source_file_path
        self.output_path = output_path

    def _fetch_clips_to_download(self) -> [YoutubeClip]:
        clips = []
        with open(self.source_file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                youtube_id, start, end, *rest = line.split(",")
                start = int(float(start))
                end = int(float(end))
                clip = AudiosetYoutubeClip(
                    youtube_id, start, end,
                    output_dir=self.output_path
                )
                clips.append(clip)
        return clips
