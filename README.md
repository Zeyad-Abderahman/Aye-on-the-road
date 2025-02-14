# Sleep Detector - Driver Drowsiness Detection System  

The **Sleep Detector** is a groundbreaking, AI-powered solution designed to revolutionize road safety by preventing fatigue-related accidents. Drowsy driving is a global epidemic, contributing to thousands of accidents annually, many of which result in severe injuries or fatalities. Traditional methods of detecting drowsiness, such as self-assessment or external monitoring, are often unreliable and prone to human error. To combat this critical issue, the Sleep Detector leverages state-of-the-art **deep learning** and **computer vision** technologies to provide an automated, real-time drowsiness detection system that ensures driver safety and reduces the risk of accidents.  

This project is not just a technological innovation; it’s a life-saving tool. By continuously monitoring a driver’s alertness through advanced AI algorithms, the Sleep Detector can identify early signs of fatigue and trigger timely alerts, potentially saving countless lives. Whether you’re a long-haul truck driver, a commuter, or a fleet manager, this system is designed to keep you and others safe on the road.  

---

## Key Features  

### 1. **Real-Time Drowsiness Detection**  
   - The system continuously monitors the driver’s alertness in real time using a webcam or integrated camera.  
   - It analyzes facial features such as eye openness, blink rate, and head position to detect signs of drowsiness.  

### 2. **Advanced AI and Deep Learning**  
   - Built using **TensorFlow** and **Keras**, the deep learning model is trained on a comprehensive dataset of drowsy and alert facial images.  
   - The model achieves high accuracy in classifying driver states as "Drowsy" or "Alert."  

### 3. **Computer Vision for Facial Landmark Detection**  
   - Utilizes **OpenCV** and **MediaPipe** for real-time image processing and facial landmark detection.  
   - Tracks critical indicators of drowsiness, such as eye closure duration, yawning, and head tilt.  

### 4. **Immediate Alert System**  
   - When drowsiness is detected, the system triggers an alert, which can include:  
     - **Sound alarms** (e.g., beeps or voice alerts).  
     - **Visual warnings** (e.g., flashing lights or on-screen notifications).  
     - **Integrated responses** in smart vehicle systems (e.g., automatic braking or lane correction).  

### 5. **Lightweight and Optimized for Real-Time Performance**  
   - Designed to operate efficiently with minimal delay, ensuring timely detection and response.  
   - Suitable for deployment on various platforms, including laptops, mobile devices, and embedded systems.  

### 6. **User-Friendly Graphical Interface (GUI)**  
   - Features an intuitive **GUI** built with **Tkinter** or **PyQt**, allowing users to easily start, stop, and configure the system.  
   - Provides real-time feedback and visualizations of driver alertness.  

### 7. **Scalable and Future-Ready Architecture**  
   - Supports integration with IoT devices for in-car alerts and notifications.  
   - Can be deployed on **mobile platforms** using **TensorFlow Lite** or embedded hardware like **Raspberry Pi**.  
   - Compatible with automotive systems for seamless operation in modern vehicles.  

---

## How It Works  

1. **Data Collection and Preprocessing**  
   - The system is trained on a labeled dataset containing thousands of images of drowsy and alert individuals.  
   - The dataset is preprocessed using **Pandas** and **scikit-learn** to handle imbalances and improve model accuracy.  

2. **Model Training**  
   - A deep learning model is built using **TensorFlow** and **Keras** to classify driver states as "Drowsy" or "Alert."  
   - The model is fine-tuned to achieve optimal performance in real-world scenarios.  

3. **Real-Time Detection**  
   - **OpenCV** captures video feed from a webcam or integrated camera.  
   - **MediaPipe** detects facial landmarks, such as eye openness and head position, in real time.  

4. **Alert Triggering**  
   - If the system detects signs of drowsiness (e.g., prolonged eye closure or excessive yawning), it immediately triggers an alert to wake the driver.  

---

## Technologies Used  

- **Deep Learning Frameworks**: TensorFlow, Keras  
- **Computer Vision**: OpenCV, MediaPipe  
- **Data Processing**: NumPy, Pandas, scikit-learn  
- **Visualization**: Matplotlib  
- **GUI Development**: Tkinter, PyQt  
- **Deployment**: TensorFlow Lite, Raspberry Pi (optional)  
- **Programming Language**: Python  

---

## Installation  

### Step 1: Clone the Repository  
```bash  
git clone https://github.com/Zeyad-Abderahman/Aye-on-the-road.git  
cd Aye-on-the-road  
```  

### Step 2: Install Dependencies  
```bash  
pip install -r requirements.txt  
```  

### Step 3: Run the Application  
```bash  
python live_webcam_test.py  
```  

---

## Future Improvements  

The Sleep Detector is an evolving project with immense potential for growth and enhancement. Future improvements may include:  

1. **Expanded Dataset**: Incorporating more diverse facial images to improve model accuracy across different demographics.  
2. **Advanced Neural Architectures**: Implementing **CNN-LSTMs** for sequential analysis of driver behavior over time.  
3. **IoT Integration**: Connecting the system with IoT devices for real-time alerts and notifications in smart vehicles.  
4. **Mobile Deployment**: Optimizing the model for mobile platforms using **TensorFlow Lite** for on-the-go drowsiness detection.  
5. **Embedded Systems**: Deploying the system on embedded hardware like **Raspberry Pi** for cost-effective and portable solutions.  
6. **Vehicle Integration**: Embedding the system into automotive systems for seamless operation and enhanced safety features.  

---

## Contribution  

This project is **open-source**, and we welcome contributions from developers, researchers, and enthusiasts worldwide. Whether you’re interested in improving the model, enhancing the GUI, or integrating new features, your contributions can help make roads safer for everyone.  

### How to Contribute:  
1. Fork the repository.  
2. Create a new branch for your feature or improvement.  
3. Submit a pull request with a detailed description of your changes.  

---

## License  

The Sleep Detector is released under the **MIT License**, making it free to use, modify, and distribute. We believe in the power of open-source collaboration to drive innovation and save lives.  

---

## Why This Project Matters  

Drowsy driving is a silent killer on our roads, responsible for countless accidents and fatalities every year. The Sleep Detector is more than just a technological innovation; it’s a commitment to making roads safer for everyone. By leveraging the power of AI and computer vision, this project has the potential to:  

- **Reduce accidents**: Prevent fatigue-related collisions by alerting drivers before it’s too late.  
- **Save lives**: Protect drivers, passengers, and pedestrians from the devastating consequences of drowsy driving.  
- **Promote awareness**: Highlight the dangers of drowsy driving and encourage safer driving habits.  

With the increasing adoption of AI in automotive safety, the Sleep Detector is poised to become a critical tool in the fight against drowsy driving. Together, we can make a difference and create a safer future for all.  

--- 

Join us in this mission to save lives and make roads safer. Let’s drive change, one alert at a time. 🚗💤🚨
