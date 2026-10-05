from moviepy import VideoFileClip

input_file = input("Enter MP4 file path: ")
output_file = input("Enter MP3 output name: ")

if ".mp3" not in output_file:
    output_file = output_file + ".mp3"

try:
    video = VideoFileClip(input_file)

    video.audio.write_audiofile(output_file)

    video.close()

    print("Done! MP3 created successfully.")

except Exception as e:
    print(f"Error: {e}")