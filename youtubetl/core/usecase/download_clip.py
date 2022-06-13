from multiprocessing import Pool

from youtubetl.core.domain.YoutubeClip import YoutubeClip
from tqdm import tqdm
import numpy as np


class YoutubeClipDownloader:

    def __init__(self, pool_size: int = 1):
        self.pool_size = pool_size
        self.clips = None

    def execute(self):

        # Fetch all clips to be downloaded
        clips: [YoutubeClip] = self.clips if self.clips is not None \
            else self._fetch_clips_to_download()

        pbar = tqdm(total=len(clips))

        def update(*a):
            pbar.refresh()
            pbar.update()

        # Async multithreading
        pool = Pool(self.pool_size)
        queue = []
        for clip in clips:
            res = pool.apply_async(self.worker, args=(clip, ), callback=update)
            queue.append(res)

        for res in queue:
            res.get()

        pool.close()
        pool.join()

    @staticmethod
    def worker(clip: YoutubeClip):
        try:
            clip.download()
        except:
            pass

    def split(self, num_split: int = 2, target: int = 0):
        if target > num_split - 1:
            raise Exception(f"Invalid argument: target {target} is larger than num_split {num_split}")

        clips: [YoutubeClip] = self._fetch_clips_to_download()
        split_clips = np.array_split(clips, num_split)
        self.clips = split_clips[target]

    def _fetch_clips_to_download(self) -> [YoutubeClip]:
        raise Exception("Not implemented yet.")
