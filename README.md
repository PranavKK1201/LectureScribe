# NotesDigitization: Automated Classroom Note Generation

## Project Overview

NotesDigitization is an innovative project designed to transform classroom learning by automatically capturing, digitizing, and summarizing lecture content. Our system leverages advanced technologies to convert classroom materials into comprehensive, structured notes.

## Key Features

- **Automated Text Extraction**: 
  - Utilizes Optical Character Recognition (OCR) technology
  - Extracts text from handwritten boards and PowerPoint slides
  - Reduces manual transcription efforts

- **Multi-source Content Integration**:
  - Combines text data from multiple sources
  - Integrates handwritten notes and digital slides
  - Creates well-structured, cohesive lecture notes

- **Advanced Text Recognition**:
  - Implements machine learning models
  - Enhances OCR accuracy
  - Recognizes diverse handwriting styles and fonts

- **Natural Language Processing (NLP) Enhancement**:
  - Performs spell-checking
  - Corrects grammar
  - Provides contextual editing

- **AI-Powered Summarization**:
  - Uses Large Language Models (LLM)
  - Extracts key points
  - Highlights important topics
  - Refines extracted text for better comprehension

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
git clone https://github.com/yourusername/NotesDigitization.git

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
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

