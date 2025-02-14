# Sleep Detector - Driver Drowsiness Detection System  
Sleep Detector is an AI-powered system that detects driver drowsiness in real time using deep learning and computer vision. It analyzes facial features from a webcam to classify drivers as drowsy or alert, helping prevent fatigue-related accidents. Built with **Keras** and **TensorFlow**, the model is trained on a labeled dataset for accurate detection.  

## Key Features  
- **Real-time drowsiness detection**: Continuously monitors driver alertness using a webcam.  
- **Facial landmark analysis**: Detects eye openness and head position using **OpenCV** and **MediaPipe**.  
- **Alert system**: Triggers alarms (sound or visual) when drowsiness is detected.  
- **Lightweight and optimized**: Designed for real-time performance with minimal delay.  
- **Customizable GUI**: Built with **Tkinter** or **PyQt** for easy configuration and control.  
- **Open-source**: Encourages contributions for further enhancements.  

## Technologies Used  
- **Deep Learning Frameworks**: TensorFlow, Keras  
- **Computer Vision**: OpenCV, MediaPipe  
- **Data Processing**: NumPy, Pandas, scikit-learn  
- **Visualization**: Matplotlib  
- **GUI Development**: Tkinter, PyQt  
- **Deployment**: TensorFlow Lite, Raspberry Pi (optional)  

## How It Works  
1. **Data Collection**: The model is trained on a labeled dataset of drowsy and alert facial images.  
2. **Preprocessing**: The dataset is preprocessed using Pandas and scikit-learn to handle imbalances and improve accuracy.  
3. **Model Training**: A deep learning model is built using TensorFlow and Keras to classify driver states as "Drowsy" or "Alert."  
4. **Real-time Detection**: OpenCV captures video from a webcam, and MediaPipe detects facial landmarks (e.g., eye openness, head position).  
5. **Alert System**: If drowsiness is detected, the system triggers an alarm (sound or visual).  

## Future Improvements  
- Expand the dataset with more diverse facial images.  
- Implement advanced architectures like **CNN-LSTMs** for sequential analysis.  
- Deploy on embedded hardware like **Raspberry Pi**.  
- Integrate with IoT devices or vehicle monitoring systems for enhanced safety.  

## Installation  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/your-username/sleep-detector.git  
   cd sleep-detector  
   ```  
2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  
3. Run the application:  
   ```bash  
   python main.py  
   ```  

## Contribution  
Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.  

## License  
This project is open-source and available under the MIT License.  

---  
With the increasing adoption of AI in automotive safety, the Sleep Detector has the potential to significantly reduce drowsy driving incidents and save lives on the road.
