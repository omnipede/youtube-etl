from multiprocessing import Pool

from pipeline.core.domain.YoutubeClip import YoutubeClip
from tqdm import tqdm


class YoutubeClipDownloader:

    def __init__(self, pool_size: int = 1):
        self.pool_size = pool_size

    def execute(self):

        # Fetch all clips to be downloaded
        clips: [YoutubeClip] = self._fetch_clips_to_download()

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

    def _fetch_clips_to_download(self) -> [YoutubeClip]:
        raise Exception("Not implemented yet.")
