# DeepVideo2Frames

**DeepVideo2Frames** is a Python library that extracts frames from videos and saves them as images. It is designed to be used in deep learning and computer vision tasks, providing various options for frame extraction, including interval selection, image resizing, and format support.

---

## Features

- Extract frames from videos at specified intervals.
- Supports multiple output image formats: JPG, PNG, BMP, etc.
- Option to resize images for more efficient storage or processing.
- Option to compress images (JPEG compression).
- Flexible frame extraction by defining start and end times.
- Parallel processing support for faster frame extraction.

---

## Installation

To install **DeepVideo2Frames**, you can use `pip`:

```bash
pip install deepvideo2frames
```

Or clone the repository and install it manually:

```bash
git clone https://github.com/franciscoreyne/deepvideo2frames.git
cd deepvideo2frames
pip install .
```

---

## Usage

### Basic Example

```python
from deepvideo2frames import video_to_frames

video_path = "path_to_your_video.mp4"
output_folder = "frames_output"

video_to_frames(
    video_path=video_path,
    output_folder=output_folder,
    frame_interval=5,  # Extract every 5th frame
    output_format='jpg',  # Save as JPG images
    compress=True,  # Compress images to reduce size
    resize=(640, 360),  # Resize images to 640x360
    start_time=10,  # Start at 10 seconds
    end_time=60,    # End at 60 seconds
    parallel=True   # Enable parallel processing for faster extraction
)
```

### Function Parameters

- **video_path (str)**: Path to the video file you want to process.
- **output_folder (str)**: Folder where the extracted frames will be saved.
- **frame_interval (int)**: Interval between frames to extract (default: 1). For example, `frame_interval=5` will extract every 5th frame.
- **output_format (str)**: Image format for the output frames. Supported formats: 'jpg', 'png', 'bmp'.
- **compress (bool)**: Whether to compress the images (default: False). If set to `True`, JPEG compression is applied.
- **resize (tuple)**: Resize the frames to a specific width and height (default: None).
- **start_time (int)**: The start time (in seconds) to begin extracting frames (default: 0).
- **end_time (int)**: The end time (in seconds) to stop extracting frames (default: None, meaning the entire video is processed).
- **parallel (bool)**: Enable parallel processing to speed up frame extraction (default: False).

---

## Contributing

We welcome contributions! If you have suggestions or improvements, feel free to open an issue or create a pull request.

To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a pull request

---

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
