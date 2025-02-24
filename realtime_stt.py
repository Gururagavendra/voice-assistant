from RealtimeSTT import AudioToTextRecorder

def realtime_transcribe():
    with AudioToTextRecorder() as recorder:
        return recorder.text()

#for testing
# realtime_transcribe()