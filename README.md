# Air-Ring Gesture Recognition: Improving Workflow with Shortcut Keys

## Link
- **Demo Video**: https://youtu.be/3UDJmE8ajxY
- **Frontend Web**: https://chian-chen.github.io/BELab-Final/

## Introduction
<!---
Non-contact control has always been a trend nowadays. Compared to traditional buttons and touch screens, there are many alternative solutions that can provide more flexibility and convenience in control. For instance, computer vision (CV) has reached a commercial level of proficiency in many applications. However, computer vision also faces several challenges that are difficult to overcome, such as privacy concerns and limitations due to camera angle obstructions. Therefore, in certain applications, computer vision may not be the best choice.

By referring to past data, we have found that using a nine-axis sensor (LSM9DS1) can achieve satisfactory accuracy in gesture recognition, comparable to CV. The nine-axis sensor consists of a three-axis accelerometer, a three-axis gyroscope, and a three-axis magnetometer. Gestures typically involve noticeable movements and rotations, and with proper data processing, similar patterns can be captured even among different individuals. Therefore, by using a nine-axis sensor fixed on a part of the body, it should be possible to create a user-independent system that can replace CV for non-contact device control.

In this project, we have fixed the nine-axis sensor in the form of a ring on the fingers, creating a prototype called "Air-Ring." We have defined eight easily operable gestures (U, D, L, R, O, V, Z, N). After collecting over 5000 data points and training with a Convolution Neural Network (CNN) architecture, along with the PyAutoGUI package, we have achieved real-time gesture recognition for keyboard control. In training data, we have achieved an accuracy of over 95% and can correctly recognize 30 different gestures within 60 seconds.
--->

<!---shorter version--->
Non-contact control is a current trend, offering more flexible and convenient options compared to traditional buttons and touch screens. While computer vision (CV) is widely used, it has privacy and angle limitations. Our research shows that a nine-axis sensor (LSM9DS1) can match CV's accuracy for gesture recognition. This sensor combines accelerometers, gyroscopes, and magnetometers, capturing distinct patterns in gestures. We've created an Air-Ring prototype, fixing the nine-axis sensor on fingers, defining eight easy gestures (U, D, L, R, O, V, Z, N), and trained a Convolution Neural Network (CNN) with over 5000 data points. With PyAutoGUI, we achieved real-time gesture recognition for keyboard control, surpassing 95% accuracy and recognizing 30 different gestures within 60 seconds.

## System Overview
To achieve high flexibility, we created a simple frontend [website](https://chian-chen.github.io/BELab-Final/) to facilitate user shortcut key configuration. The completed system flowchart is roughly depicted in the following figure.

<div align="center">
  <img width="600" alt="sysyem" src="https://github.com/chian-chen/BELab/assets/55650127/d9378aee-f490-4bdf-a8ef-ea3ea6a6ad3a">
  <p>Fig. 1. System Flowchart</p>
</div>

First, users configure their preferences using the frontend website according to their needs. They map our defined gestures to specific shortcut keys, generating a configuration .json file. Next, they place the generated file in the path where the Python program executes. The data collected by the nine-axis sensor (IMU) is processed using the [library](https://github.com/arduino-libraries/Arduino_LSM9DS1) and connected to an Arduino UNO. PySerial is used to establish a connection between Python and Arduino. Subsequently, the trained CNN model generates results, which, when mapped to the configured shortcut keys, are sent to PyAutoGUI for gesture-to-keyboard control.

## Data Collection
We attached a nine-axis sensor to the fingers using medical breathable tape and silicone rings to collect the three-axis acceleration generated when the fingers move. We sampled the acceleration at 60Hz, collecting 150 points of acceleration time-domain signals (taking 2-3 seconds). There are 8 different hand gestures: up, down, left, right, N, Z, V, and O. To simulate practical use, our system must classify all non-gesture signals as noise, such as hand rest, keyboard or touchpad usage, and grabbing objects. Therefore, we added an additional 9th category: Noise.

Initially, we experimented with the six axes of the nine-axis sensor, but due to differences in sampling frequencies for the magnetic axis and the other two axes, and because the purchased nine-axis sensor had a gyroscope failure, we ultimately used only the three-axis accelerometer from the nine-axis for data collection and recognition.

<div align="center">
  <img width="316" alt="finger" src="https://github.com/chian-chen/BELab/assets/55650127/3fdfd0d2-0ab3-40a5-994d-4c196cdd6069">
  <p>Fig. 2. Wearable Device Illustration</p>
</div>

Furthermore, to reduce variations in training data produced by different users, we defined clear gestures for each category. Users can imagine a virtual 3x3 grid in front of them and move their fingers to the corresponding positions in sequence. The defined gestures and execution steps are shown in the figure (Fig. 3), and the collected data types are shown in Fig. 4.

<div align="center">
  <img width="801" alt="gestures" src="https://github.com/chian-chen/BELab/assets/55650127/7ee9ac12-b03f-417a-8709-1b1aa3e737d2">
  <p>Fig. 3. Gesture Execution Steps</p>
</div>

<div align="center">
  <img width="572" alt="datas" src="https://github.com/chian-chen/BELab/assets/55650127/ab9ca41f-671a-4735-a5dd-cd84df0fa54c">
  <p>Fig. 4. Data Sample <br>(L: Up gesture, R: Right gesture)</p>
</div>

To avoid model overfitting and increase the diversity of training data to improve model accuracy, we perform data augmentation after collecting training data. For each training data of a gesture, we add noise with certain weights generated randomly using Gaussian distribution. For the noise category, we use noise generated randomly using Gaussian distribution to represent a stationary state of noise (Fig. 5).

When implementing real-time recognition algorithms, the model continuously recognizes the signal as input, which can lead to incorrect judgments after recognizing the first half of a gesture signal. Therefore, we randomly take 50 points from the collected noise data (Fig. 5, red part), and add them to the pre-processed training data's first 30 points (Fig. 5, blue part), creating new noise data.

We collected approximately 5700 training data in total, with about 450 data points for each gesture and about 2000 data points for noise. You can refer to the data and imgs folders in the GitHub repository for raw data (.npz) and visualized images.

<div align="center">
  <img width="565" alt="noise" src="https://github.com/chian-chen/BELab/assets/55650127/420b216d-ef44-4e26-b0fb-2e772b3b0234">
  <p>Fig. 5. Data Augmentation <br>(L: Noise mixed with data, R: Gaussian distribution noise)</p>
</div>

## Preproproessing
During data collection, we set the signal length to 150 points to encompass hand gesture signals. However, to reduce dimensionality and find meaningful signal segments, we use a sliding window of 80 points to identify the highest-energy window, after subtracting the signal's mean. 

```math
p_{i,j} = \sum_{k = i}^{j} p_k^2
```

As shown in Fig. 6 with the orange signal and green dots, this approach successfully identifies the segment with the most significant signal variation. This means that we have effectively reduced the signal length from 150 points to 80 points before inputting it into the model. This shorter signal can be used directly for model input or undergo one-dimensional wavelet transformation. Experimental results show similar performance for both approaches, and we select the unprocessed time-domain signal for model input.

<div align="center">
  <img width="403" alt="normalize" src="https://github.com/chian-chen/BELab/assets/55650127/36b91e2d-a6f1-4055-8272-cb5198a81083">
  <p>Fig. 6</p>
</div>

## Model
The CNN model excels in finding broader local features using filters, making it successful in various tasks. In this experiment, the CNN model initially employs a 1x16 filter to process the acceleration along each axis, generating 96 feature maps. These feature maps are flattened, and several linear layers are used for classification. The model's output is evaluated using the cross-entropy loss function, and the Adam optimizer is used for parameter adjustments over ten training epochs. To prevent model overfitting, data augmentation is applied to increase training data, and fewer model parameters are used along with a Dropout layer. The model architecture is shown in Fig. 7.

<div align="center">
  <img width="400" alt="model" src="https://github.com/chian-chen/BELab/assets/55650127/03e4145d-ccdf-4301-bc33-0e4ec9c44463">
  <p>Fig. 7. Model Architecture</p>
</div>

The CNN model achieves an accuracy of approximately 97% on test data. From the confusion matrix in Fig. 8, it is evident that the model exhibits high accuracy for each class. However, it occasionally confuses left and right, as well as Z and N gestures, possibly due to the similarities in the signals, which could be attributed to variations in finger force among different users.

<div align="center">
  <img width="300" alt="conma" src="https://github.com/chian-chen/BELab/assets/55650127/089cf0ee-011d-43ae-870b-219f0f7b0e64">
  <p>Fig. 8. Confusion Matrix</p>
</div>

## Real-time Algorithm
We continuously store the most recent 150 data points and, after collecting each new data point, we identify the 80 data points with the highest energy within this 150-point dataset. These 80 data points are then fed into the model to obtain a classification result. If the result is not categorized as noise, we execute the corresponding keyboard shortcut settings.

### Real-time Data Collection:
Three constantly updating queues for collecting the latest 150 data points (for x, y, and z-axis accelerations, each lasting approximately 2.5 seconds).

<div align="center">
  <img width="405" alt="queue" src="https://github.com/chian-chen/BELab/assets/55650127/7e3e2bfa-b7f6-433f-bb14-08c0af573393">
  <p>Fig. 9. Queue</p>
</div>

#### Process:
1. Find the contiguous segment of 80 data points with the highest energy from the 150-point queue (this process aligns with the operations performed during the training and testing data collection for the model, as mentioned above).

2. If any of the three 80-point contiguous segments for x, y, and z-axis data are among the last 5 contiguous segments in the queue, we consider them as potential incomplete hand gesture actions and therefore do not proceed further. We classify them as noise.
(Note: The 150-point queue offers 70 possible 80-point contiguous segments to choose from, as there are 150 - 80 = 70 such segments. The "last 5 contiguous segments" refer to the last 5 among these 70 possible choices. The choice of 5 is made based on a trade-off between accuracy and latency.)

3. If the energy of all three 80-point contiguous segments does not exceed the set threshold, we also do not proceed further and classify it as noise.

4. Feed these 80 data points into the model to obtain a classification result (which can be a specific hand gesture or noise).

5. If the result is not categorized as noise, execute the corresponding predefined keyboard shortcut settings and clear the queue to avoid redundant execution of the same shortcut settings.

## Evaluation
In our presentation of results, we use two distinct approaches: assessing the speed of hand gesture recognition and simulating real-world usage. These results are showcased in Part 2 and Part 3 of the video presentation (https://youtu.be/3UDJmE8ajxY).

### Speed Testing
For speed evaluation, we employed customized settings from a [typing website](https://monkeytype.com/) to measure the time needed for correctly recognizing 30 hand gestures. We used the following gestures: Up, Down, Left, Right, O, V, Z, N, corresponding to (U, D, L, R, O, V, Z, N). Please refer to Fig. 10 for the interface.

<div align="center">
  <img width="400" alt="monkey" src="https://github.com/chian-chen/BELab/assets/55650127/392655da-28b3-4ab5-9492-0a0681799f0b">
  <p>Fig. 10. monkeytype</p>
</div>

On average, it takes around 60 seconds to correctly recognize 30 hand gestures, which translates to roughly two seconds per recognition. This speed closely aligns with the data collection approach used. Our data collection involved sampling data at a rate of around 60Hz, with 150 data points (2-3 seconds) used for training data. Therefore, in real-time systems, not utilizing a similar data acquisition method significantly impacts accuracy, making it challenging to address this limitation through algorithm enhancements.

In addition, we measured the bottleneck time without considering hardware data collection. This time delay is mainly associated with software execution. Data preprocessing and basic logic checks are essentially negligible. The primary delay occurs during model recognition and the execution of PyAutoGUI keyboard shortcuts, with PyAutoGUI outperforming other operations. After exploring alternative modules for keyboard shortcut operations, we found PyAutoGUI to offer relatively faster execution. Although other modules provide more advanced functionalities, they tend to be slower and do not align with our requirements. As a result, software speed optimization remains an ongoing challenge.

### Simulated Real-world Usage
To demonstrate real-world usage, we utilized Adobe Photoshop software. In the second part of the video, we showcased the use of five sets of less commonly employed keyboard shortcuts. In practical use, our system effectively filters out common workplace noise, preventing false positives and consistently achieving good results in terms of speed and accuracy.

<div align="center">
<table>
<tr><th>Program Execution Speed</th><th>Shortcuts Mapping</th></tr>
<tr><td>

| Operation | Time |
| :-: | :-: |
| Data Processing | <0.001s |
| Model Recognition<br>(CNN Model) | 0.003 - 0.005s |
| Keyboard Shortcut<br>(PyAutoGUI) | 0.1s |

</td><td>

| Gesture | Shortcut |
| :-: | :-: |
| Gesture Up | command + shift + E |
| Gesture V | command + shift + S |
| Gesture 0 | command + shift + U |
| Gesture N | command + O |
| Gesture Z | command + U |

</td></tr> </table>
</div>

## Conclusion
This project utilized a nine-axis sensor (LSM9DS1) connected to an Arduino UNO development board to create a prototype of the gesture-controlled keyboard device, Air-Ring. By collecting acceleration signals generated during movement with the nine-axis sensor, preprocessing these signals, and inputting them into a trained CNN model for gesture recognition, we achieved an accuracy of over 95% on the CNN Model. In terms of speed, we accomplished the continuous recognition of 30 correct gestures within 60 seconds.

Through our developed frontend website, users can easily establish the correspondence between shortcuts and the model's recognition results. This allows users to enhance efficiency and productivity in any software application by using gestures. Currently, the main bottleneck lies in the method of data collection, and improvements in this aspect could further enhance both speed and accuracy.

Once speed, accuracy, and device comfort reach their peak, this device has the potential to offer users a convenient means of operation across various applications, making it a more versatile computer controller.

## Reference
[1] Andrey Ignatov. Real-time human activity recognition from accelerometer data using convolutional neural networks. *Applied Soft Computing*, 62:915–922, 2018.
#### LSM9DS1:
- https://cdn.sparkfun.com/assets/learn_tutorials/3/7/3/LSM9DS1_Datasheet.pdf
- https://github.com/FemmeVerbeek/Arduino_LSM9DS1
- https://learn.sparkfun.com/tutorials/lsm9ds1-breakout-hookup-guide/all
- https://github.com/sparkfun/SparkFun_LSM9DS1_Arduino_Library
#### PySerial/ PyAutoGUI documentation:
- https://pypi.org/project/pyserial/
- https://www.mathworks.com/help/supportpkg/arduinoio/ug/find-arduino-port-on-windows-mac-and-linux.html
- https://pyautogui.readthedocs.io/en/latest/
#### Others:
- http://cc.ee.ntu.edu.tw/~ultrasound/belab/term_project/Group7/final_reprt_G7.pdf
- https://learn.sparkfun.com/
- https://www.biometricupdate.com/201801/this-ring-uses-gesture-recognition-to-write-words-and-numbers
- https://swf.com.tw/?p=1188&fbclid=IwAR3kguoYJDWyvA7fybZRm8fOZz0lmJnv13t9mzQMa4MRST8QOaOa_P16QXk
- https://link.springer.com/chapter/10.1007/978-3-319-27707-3_19
- ChatGPT









<!---
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
--->
