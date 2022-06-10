from youtubetl.impl.vgg.VggYoutubeClipDownloader import VggYoutubeClipDownloader


if __name__ == '__main__':

    VggYoutubeClipDownloader(
        source_file_path='/Users/seohyeongyu/Desktop/work/naver-ai/aaclip/youtube-downloader/dataset/vggsound.csv',
        output_path='/Users/seohyeongyu/Desktop/data/vgg',
        pool_size=30
    ).execute()
