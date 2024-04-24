# VisiCheck - Eye Health Recommendation System
Google Girl Hackathon 2024 Project

##  1. Problem Statement and Motivation

**Problem Statement:** Develop a healthcare recommendation system that analyzes user symptoms leveraging symptom data, healthcare provider databases, and user ratings, recommending doctors with matching specialties and aligned schedules.

**Solution Overview:** The proposed system is dedicated to promoting eye health. It analyzes user symptoms, offers disease details, suggests preventive measures, and recommends appropriate eye specialists with available appointment slots. Additionally, it identifies common eye issues from images and features Interactive Educational Modules to educate users about eye conditions, symptoms, and treatment options. 

**Motivation:** The initiative aims to combat significant eye health challenges, particularly in India, where cataracts and diabetic retinopathy are major causes of blindness. With a high prevalence of diabetes and limited healthcare access in rural areas, there is an urgent need to address eye health disparities.

## 2. Literature Review

- [“Diabetic Retinopathy Detection Using Deep Learning,” October 9, 2020.](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9277506)
- This paper discusses the use of deep learning techniques for detecting diabetic retinopathy, a common complication of diabetes that can lead to vision loss. The study focuses on developing a convolutional neural network (CNN) model trained on retinal fundus images to classify the severity of diabetic retinopathy accurately. The proposed model accurately identifies different stages of diabetic retinopathy, showcasing its potential for automated screening and early diagnosis of the condition.
- [“Automatic Cataract Detection and Grading Using Deep Convolutional Neural Network,” May 1, 2017.](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8000068)
- This paper presents an automated system for detecting and grading cataracts using deep-learning techniques applied to retinal images. The study focuses on developing a convolutional neural network (CNN) architecture capable of accurately identifying the presence and severity of cataracts in fundus images. The proposed system demonstrates high cataract detection and grading accuracy, showcasing its potential for early diagnosis and treatment planning in ophthalmology.
- [Junayed, “CataractNet: An Automated Cataract Detection System Using Deep Learning for Fundus Images,” September 9, 2022.](https://www.academia.edu/56670364/CataractNet_An_Automated_Cataract_Detection_System_using_Deep_Learning_for_Fundus_Images)
- This paper introduces CataractNet, an automated system for detecting cataracts in retinal fundus images using deep learning techniques. The study proposes a convolutional neural network (CNN) architecture to identify cataracts and classify their severity levels accurately. CataractNet demonstrates high performance in cataract detection, offering the potential for early diagnosis and treatment planning in ophthalmology.

## 3. Dataset Details

- [“Diagnosis of Diabetic Retinopathy,” November 23, 2023.](https://www.kaggle.com/datasets/pkdarabi/diagnosis-of-diabetic-retinopathy/data)
- [“Ocular Disease Recognition,” September 24, 2020.](https://www.kaggle.com/datasets/andrewmvd/ocular-disease-recognition-odir5k)

## 4. Proposed Architecture

The architecture utilizes Convolutional Neural Networks (CNN) for diabetic retinopathy and cataract detection. For diabetic retinopathy, a CNN model in PyTorch is employed, while a custom CNN architecture (CataractModel) is utilized for cataract detection. The system also includes Interactive Educational Modules embedded with relevant content.

## 5. Visualizations

Visualizations are presented in Python notebooks, showcasing data insights, loss/accuracy curves, sample test image visualization, and confusion matrix plotting.

## 6. Results

- **Diabetic Retinopathy Detection:**
  - Utilized a CNN model achieving an accuracy of 94%.
  
- **Cataract Detection:**
  - Employed a custom CNN architecture achieving an accuracy of 95-98%.

## 7. Analysis of Results

- **Diabetic Retinopathy Detection:** Achieved high accuracy using a CNN model in PyTorch.
- **Cataract Detection:** Achieved high accuracy using a custom CNN architecture.

## 8. Inferences and Conclusion

The system demonstrates promising results in detecting diabetic retinopathy and cataracts, with accuracies ranging from 94% to 98%. By leveraging deep learning models and educational modules, the system aims to improve eye health awareness and access to specialized care, particularly in regions with limited healthcare resources.
