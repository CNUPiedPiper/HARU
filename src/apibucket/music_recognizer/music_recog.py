#-*- coding: utf-8 -*-
import pyaudio
import wave
import json
import recognition_api

THRESHOLD = 500
CHUNK = 8192
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 11
WAVE_OUTPUT_FILENAME = ".music_with_noise.wav"

def recording_music():
    p = pyaudio.PyAudio()
    
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=2,
                    frames_per_buffer=CHUNK
    )

    print("[HARU] Listening your music ... ")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("[HARU] Searching music ... ")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def get_music_title(host, key, secret):
    recording_music()
    result_str = recognition_api.recognize_music(WAVE_OUTPUT_FILENAME, host, key, secret)
    result_dict = json.loads(result_str)
    
    if result_dict['status']['msg']=='Success':
        text = "{artists}의 {title} 입니다.".format(artists=result_dict['metadata']['music'][0]['artists'][0]['name'],title=result_dict['metadata']['music'][0]['title'])
    else : 
        text = "음악을 찾을 수 없습니다."

    print("[HARU] {result}".format(result=text))
    return text
