from moviepy import VideoFileClip, AudioFileClip

def merge_audio_video(video_path, audio_path, output_path):
    try:
        # Video aur Audio load karein
        video = VideoFileClip(video_path)
        audio = AudioFileClip(audio_path)
        
        # Audio ko video ki duration ke hisaab se cut karein
        # .with_duration ya .subclip dono try kar sakte hain
        final_audio = audio.with_duration(video.duration)
        
        # Video mein audio set karein (Naya method: with_audio)
        final_video = video.with_audio(final_audio)
        
        # File export karein
        final_video.write_videofile(
            output_path, 
            codec="libx264", 
            audio_codec="aac",
            temp_audiofile='temp-audio.m4a', 
            remove_temp=True
        )
        
        print(f"Success! Aapki file yahan hai: {output_path}")
        
    except Exception as e:
        print(f"Abhi bhi lafda hai: {e}")
    finally:
        # Memory saaf karne ke liye clips close karein
        if 'video' in locals(): video.close()
        if 'audio' in locals(): audio.close()

# Files ke paths
video_file = "video 10/video.mp4"
audio_file = "video 10/audio.mp3"
output_file = "video 10/final_output.mp4"

merge_audio_video(video_file, audio_file, output_file)