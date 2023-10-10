# Air-Ring Gesture Recognition: Improving Workflow with Shortcut Keys

## Introduction
Non-contact control has always been a trend nowadays. Compared to traditional buttons and touch screens, there are many alternative solutions that can provide more flexibility and convenience in control. For instance, computer vision (CV) has reached a commercial level of proficiency in many applications. However, computer vision also faces several challenges that are difficult to overcome, such as privacy concerns and limitations due to camera angle obstructions. Therefore, in certain applications, computer vision may not be the best choice.

By referring to past data, we have found that using a nine-axis sensor (LSM9DS1) can achieve satisfactory accuracy in gesture recognition, comparable to CV. The nine-axis sensor consists of a three-axis accelerometer, a three-axis gyroscope, and a three-axis magnetometer. Gestures typically involve noticeable movements and rotations, and with proper data processing, similar patterns can be captured even among different individuals. Therefore, by using a nine-axis sensor fixed on a part of the body, it should be possible to create a user-independent system that can replace CV for non-contact device control.

In this project, we have fixed the nine-axis sensor in the form of a ring on the fingers, creating a prototype called "Air-Ring." We have defined eight easily operable gestures (U, D, L, R, O, V, Z, N). After collecting over 5000 data points and training with a Convolution Neural Network (CNN) architecture, along with the PyAutoGUI package, we have achieved real-time gesture recognition for keyboard control. In training data, we have achieved an accuracy of over 95% and can correctly recognize 30 different gestures within 60 seconds.

<!---shorter version--->
<!---
Non-contact control is a current trend, offering more flexible and convenient options compared to traditional buttons and touch screens. While computer vision (CV) is widely used, it has privacy and angle limitations. Our research shows that a nine-axis sensor (LSM9DS1) can match CV's accuracy for gesture recognition. This sensor combines accelerometers, gyroscopes, and magnetometers, capturing distinct patterns in gestures. We've created an Air-Ring prototype, fixing the nine-axis sensor on fingers, defining eight easy gestures (U, D, L, R, O, V, Z, N), and trained a Convolution Neural Network (CNN) with over 5000 data points. With PyAutoGUI, we achieved real-time gesture recognition for keyboard control, surpassing 95% accuracy and recognizing 30 different gestures within 60 seconds.
--->

## System Overview
To achieve high flexibility, we created a simple frontend [website](https://chian-chen.github.io/BELab-Final/) to facilitate user shortcut key configuration. The completed system flowchart is roughly depicted in the below figure.

<p align="center">
<img width="600" alt="sysyem" src="https://github.com/chian-chen/BELab/assets/55650127/d9378aee-f490-4bdf-a8ef-ea3ea6a6ad3a">
</p>



First, users configure their preferences using the frontend website according to their needs. They map our defined gestures to specific shortcut keys, generating a configuration .json file. Next, they place the generated file in the path where the Python program executes. The data collected by the nine-axis sensor (IMU) is processed using the [library](https://github.com/arduino-libraries/Arduino_LSM9DS1) and connected to an Arduino UNO. PySerial is used to establish a connection between Python and Arduino. Subsequently, the trained CNN model generates results, which, when mapped to the configured shortcut keys, are sent to PyAutoGUI for gesture-to-keyboard control.


## Original stuff

111-2 BELab Group2 Final Project

- data: 最終的資料集
- data_old: 前面測試、裝置配戴方式未定時的資料集
- imgs: 視覺化 data 資料
- Data_Collection: 蒐集資料用的 Arduino/ Python Code
- Model_Training: CNN Model、SVM Classifier
- Real_Time: 即時演算法的 code
- docs: 三次簡報的投影片和最終 report
- utils: 一些亂七八糟的小程式

## Link

- Demo Video: https://youtu.be/3UDJmE8ajxY
- Frontend Web: https://chian-chen.github.io/BELab-Final/
