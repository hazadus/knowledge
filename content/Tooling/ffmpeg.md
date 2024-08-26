### Merging video and audio, with audio re-encoding

See this example, taken from [this blog entry](http://crazedmuleproductions.blogspot.com/2005/12/using-ffmpeg-to-combine-audio-and.html) but updated for newer syntax. It should be something to the effect of:

```bash
ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac output.mp4
```

Here, we assume that the video file does not contain any audio stream yet, and that you want to have the same output format (here, MP4) as the input format.

The above command transcodes the audio, since MP4s cannot carry PCM audio streams. You can use any other desired audio codec if you want. See the [FFmpeg Wiki: AAC Encoding Guide](https://trac.ffmpeg.org/wiki/Encode/AAC)for more info.

If your audio or video stream is longer, you can add the `-shortest` option so that ffmpeg will stop encoding once one file ends.

### Copying the audio without re-encoding

If your output container can handle (almost) any codec – like MKV – then you can simply copy both audio and video streams:

```bash
ffmpeg -i video.mp4 -i audio.wav -c copy output.mkv
```

### Replacing audio stream

If your input video already contains audio, and you want to replace it, you need to tell ffmpeg which audio stream to take:

```bash
ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 output.mp4
```

The [`-map` option](https://trac.ffmpeg.org/wiki/Map) makes ffmpeg only use the first video stream from the first input and the first audio stream from the second input for the output file.

*Source: [StackOverflow](https://superuser.com/a/277667)*


----
📂 [[Tooling]] | Последнее изменение: 25.08.2024 22:55