import os
import subprocess
from pyrogram import Client, filters

# Configure these variables
API_ID = '22413321'
API_HASH = '19dc6a4da93120d1af60afd778559d55'
BOT_TOKEN = '7766638158:AAHRI72ksXh9nRD_-yOIVnUSVVUHsdZWpzU'

app = Client("video_compressor_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.video)
def compress_video(client, message):
    # Check if the message contains a video
    if message.video:
        file_name = message.video.file_name or "video.mp4"
        input_file_path = app.downloads_dir + "/" + file_name

        # Download the file
        message.download(input_file_path)

        # Output path for the compressed video
        output_file_path = f"compressed_{file_name}"

        # Compress the video to 480p using FFmpeg
        try:
            ffmpeg_command = [
                'ffmpeg',
                '-i', input_file_path,
                '-vf', 'scale=-1:480',  # Set height to 480, keep aspect ratio
                '-c:a', 'copy',  # Copy audio stream directly
                output_file_path
            ]
            subprocess.run(ffmpeg_command, check=True)

            # Send the compressed video back
            app.send_video(chat_id=message.chat.id, video=output_file_path)

        except subprocess.CalledProcessError as e:
            app.send_message(chat_id=message.chat.id, text="Failed to compress the video.")
            print(e)

        finally:
            # Clean up
            if os.path.exists(input_file_path):
                os.remove(input_file_path)
            if os.path.exists(output_file_path):
                os.remove(output_file_path)

if __name__ == "__main__":
    app.run()
