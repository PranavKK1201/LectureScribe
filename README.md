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

1. **Video Capture**
   - Capture classroom lecture video
   - Extract frames at regular intervals (every 15 seconds)

2. **Text Extraction**
   - Pre-process video frames
   - Apply grayscaling and thresholding
   - Detect text contours
   - Extract text using PaddleOCR

3. **Audio Transcription**
   - Convert audio to WAV format
   - Create silence-based audio chunks
   - Transcribe using Google Speech Recognition

4. **Note Generation**
   - Combine extracted video and audio texts
   - Use prompt engineering
   - Generate consolidated notes using Gemini API

## Research Objectives

- Develop real-time classroom content digitization system
- Implement AI-powered note summarization
- Evaluate system effectiveness in enhancing student learning
- Compare with existing solutions

## Future Improvements

- Speech-to-text conversion enhancement
- Input stream synchronization
- Subject-specific AI model training
- Mobile app integration

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

1. Upload classroom lecture video
2. Select processing options
3. Generate comprehensive notes

## Contributing

Contributions are welcome! Please read our contributing guidelines before submitting pull requests.

## License

MIT

## Acknowledgments

- Inspired by research from Kulkarni et al. (2023)
- Thanks to the machine learning and education technology community

