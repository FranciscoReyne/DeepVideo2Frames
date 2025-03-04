import cv2
import os
import numpy as np
from datetime import datetime
import concurrent.futures
from pathlib import Path

def video_to_frames(video_path, output_folder, frame_interval=1, output_format='jpg', compress=False, resize=None, start_time=0, end_time=None, parallel=False):
    """
    Extract frames from a video and save them as images.
    
    Parameters:
        video_path (str): Path to the video file.
        output_folder (str): Folder where the frames will be saved.
        frame_interval (int): Interval between frames to extract. Default is 1 (extract every frame).
        output_format (str): Format for the output images ('jpg', 'png', 'bmp', etc.).
        compress (bool): Whether to compress the images (lower quality, smaller size).
        resize (tuple): Resize the images to (width, height). If None, no resizing.
        start_time (int): Time in seconds to start extracting frames.
        end_time (int): Time in seconds to stop extracting frames. If None, it will extract till the end.
        parallel (bool): Whether to use parallel processing to extract frames faster.
    """
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Cannot open the video.")
        return

    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    video_duration = total_frames / fps

    # Set the start and end time (if provided)
    if end_time is None:
        end_time = video_duration
    cap.set(cv2.CAP_PROP_POS_MSEC, start_time * 1000)

    # Create output folder if not exists
    os.makedirs(output_folder, exist_ok=True)

    # Prepare frame extraction function
    def extract_frame(frame_idx):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
        ret, frame = cap.read()
        
        if not ret:
            print(f"Error reading frame {frame_idx}")
            return None
        
        # Resize image if required
        if resize:
            frame = cv2.resize(frame, resize)
        
        # Compress image if requested
        if compress and output_format == 'jpg':
            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 50]  # 50% quality for compression
            _, frame = cv2.imencode('.jpg', frame, encode_param)
            frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
        
        # Construct file path
        timestamp = datetime.fromtimestamp(frame_idx / fps).strftime('%H-%M-%S')
        filename = f"frame_{frame_idx:04d}_{timestamp}.{output_format}"
        file_path = os.path.join(output_folder, filename)

        # Save the image in the desired format
        if output_format == 'jpg':
            cv2.imwrite(file_path, frame)
        elif output_format == 'png':
            cv2.imwrite(file_path, frame)
        elif output_format == 'bmp':
            cv2.imwrite(file_path, frame)
        else:
            print(f"Unsupported format: {output_format}")
            return None
        
        return filename

    # Parallel processing for faster frame extraction
    def process_parallel():
        with concurrent.futures.ProcessPoolExecutor() as executor:  # Use ProcessPoolExecutor for CPU-bound tasks
            futures = []
            for frame_idx in range(int(start_time * fps), int(end_time * fps), frame_interval):
                futures.append(executor.submit(extract_frame, frame_idx))
            results = [future.result() for future in futures]
        return results

    # Sequential processing (fallback)
    def process_sequential():
        results = []
        for frame_idx in range(int(start_time * fps), int(end_time * fps), frame_interval):
            result = extract_frame(frame_idx)
            if result:
                results.append(result)
        return results

    # Process frames
    try:
        print(f"Extracting frames from {start_time}s to {end_time}s...")
        if parallel:
            process_parallel()
        else:
            process_sequential()
    finally:
        cap.release()  # Ensure the video capture is released
        print("Video capture released.")

    print("Frames extraction completed.")

