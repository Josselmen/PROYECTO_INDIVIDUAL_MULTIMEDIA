from moviepy import (
    VideoFileClip,
    AudioFileClip,
    TextClip,
    CompositeVideoClip
)



VIDEO_PATH = "assets/video_vaca.mp4"      # Ruta del video
AUDIO_PATH = "assets/vaca_rock.mp3"      # Ruta del audio

TEXTO = "JOSUE DAVID  "


POS_X = 40         
POS_Y = 300

FONT_SIZE = 60
COLOR = "black"


FRAMES_POR_LETRA = 6

OUTPUT_PATH = "resultado.mp4"

video = VideoFileClip(VIDEO_PATH)

video_duration = video.duration
fps = video.fps


video_width, video_height = video.size

print(f"Resolución detectada: {video_width}x{video_height}")
print(f"FPS detectado: {fps}")



audio = AudioFileClip(AUDIO_PATH)


if audio.duration > video_duration:
    audio = audio.subclipped(0, video_duration)


segundos_por_letra = FRAMES_POR_LETRA / fps

text_clips = []

for i in range(1, len(TEXTO) + 1):

    texto_actual = TEXTO[:i]

    inicio = (i - 1) * segundos_por_letra

    clip = (
        TextClip(
            text=texto_actual,
            font_size=FONT_SIZE,
            color=COLOR,
            method="label"
        )
        .with_start(inicio)
        .with_duration(video_duration - inicio)
        .with_position((POS_X, POS_Y))
    )

    text_clips.append(clip)


video_final = CompositeVideoClip(
    [video] + text_clips,
    size=video.size
)



video_final = video_final.with_audio(audio)



video_final.write_videofile(
    OUTPUT_PATH,
    codec="libx264",
    audio_codec="aac",
    fps=fps
)

print("Proceso terminado.")