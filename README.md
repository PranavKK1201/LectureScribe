# LectureScribe: Automated Classroom Note Generation

## Project Overview

LectureScribe is an innovative project designed to transform classroom learning by automatically capturing, digitizing, and summarizing lecture content. Our system leverages advanced technologies to convert classroom materials into comprehensive, structured notes.

## Demo Usage:
### Video to Text
![image](https://github.com/user-attachments/assets/80f4e378-df0e-4c12-9811-89bf21666e74)
![image](https://github.com/user-attachments/assets/54854701-89dc-4638-89a8-bf0a826b9594)

### Audio Transcript
![image](https://github.com/user-attachments/assets/563d98d0-d6af-4fe5-b547-27820846a5b8)

### Transcript Augmentation with LLM
![image](https://github.com/user-attachments/assets/ef823221-f818-49fe-afe9-c4c801b69b49)

## Technology Stack
- **Video Processing**: OpenCV
- **OCR**: PaddleOCR
- **Speech Recognition**: Google Speech Recognition
- **AI Integration**: Google Gemini API
- **Text Processing**: mT5, NLP techniques

## Project Workflow
1.  **Video Capture**: The process begins by capturing the classroom lecture video. To ensure comprehensive coverage without overwhelming the system, frames are systematically extracted at a 15-second interval, capturing key moments and written content.
2.  **Text Extraction**: Each extracted frame undergoes a series of pre-processing steps to optimize it for OCR. This includes applying **grayscaling** to simplify the image and **thresholding** to create a high-contrast binary image. The system then detects **text contours** to isolate text regions before using **PaddleOCR** to extract the written content.
3.  **Audio Transcription**: The audio track from the video is converted to WAV format for processing. It is then segmented into **silence-based audio chunks** to improve the accuracy of transcription. Each chunk is individually processed by the **Google Speech Recognition** API to generate a time-aligned transcript.
4.  **Note Generation**: The text extracted from video frames and the audio transcript are combined. Using carefully crafted **prompt engineering**, this consolidated text is passed to the **Gemini API**, which organizes the information, corrects errors, removes redundancies, and generates a final set of structured and easy-to-read notes.

## Research Objectives
-   Develop a robust, real-time system capable of digitizing classroom content from both visual and auditory sources.
-   Implement and refine an AI-powered note summarization engine to produce structured and contextually accurate study materials.
-   Evaluate the system's effectiveness and impact on student learning engagement and academic performance through user studies.
-   Benchmark the performance and features of LectureScribe against existing commercial and open-source note-taking solutions.

## Future Improvements
-   **Speech-to-Text Conversion Enhancement**: Investigate and integrate more advanced speech recognition models to improve transcription accuracy, particularly for specialized academic vocabulary.
-   **Input Stream Synchronization**: Implement a precise, timestamp-based mechanism to perfectly align text extracted from video frames with the corresponding spoken transcript for greater contextual accuracy.
-   **Subject-Specific AI Model Training**: Fine-tune AI models for specific academic subjects like mathematics or biology to better understand and format domain-specific notations, diagrams, and terminology.
-   **Mobile App Integration**: Develop a dedicated mobile application for iOS and Android to allow users to record lectures, view generated notes, and study material on the go.

## Installation

```bash
# Clone the repository
git clone https://github.com/PranavKK1201/NotesDigitization.git

# Install dependencies
pip install -r requirements.txt

# Run the application
___.py
```


## Usage
1.  Launch the application and upload your classroom lecture video file.
2.  Select the desired processing options for note generation.
3.  Initiate the process and receive a comprehensive set of digital notes.

## Contributing
Contributions are always welcome! Please read our contributing guidelines to learn how you can help improve the project and feel free to submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
-   This work is inspired by the foundational research on automated note generation by Kulkarni et al. (2023).
-   A special thanks to the open-source community for developing the machine learning and educational technology tools that made this project possible.


