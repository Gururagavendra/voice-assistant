from RealtimeSTT import AudioToTextRecorder

def realtime_transcribe():
    with AudioToTextRecorder() as recorder:
        return recorder.text()

# #for testing
# realtime_transcribe()


# from RealtimeSTT import AudioToTextRecorder

# def process_text(text):
#     print(text)

# if __name__ == '__main__':
#     recorder = AudioToTextRecorder()

#     while True:
#         recorder.text(process_text)