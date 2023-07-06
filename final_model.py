# load pretrained model
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
asr_processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
asr_model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

# get a single audio file
!wget https://dldata-public.s3.us-east-2.amazonaws.com/1919-142785-0028.wav