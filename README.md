# VisiCheck - Eye Health Recommendation System
Google Girl Hackathon 2024 Project

##  1. Problem Statement and Motivation

**Problem Statement:** Develop a healthcare recommendation system that analyzes user symptoms leveraging symptom data, healthcare provider databases, and user ratings, recommending doctors with matching specialties and aligned schedules.

**Solution Overview:** The proposed system is dedicated to promoting eye health. It analyzes user symptoms, offers disease details, suggests preventive measures, and recommends appropriate eye specialists with available appointment slots. Additionally, it identifies common eye issues from images and features Interactive Educational Modules to educate users about eye conditions, symptoms, and treatment options. 

**Motivation:** The initiative aims to combat significant eye health challenges, particularly in India, where cataracts and diabetic retinopathy are major causes of blindness. With a high prevalence of diabetes and limited healthcare access in rural areas, there is an urgent need to address eye health disparities.

## 2. Literature Review

- [“Diabetic Retinopathy Detection Using Deep Learning,” October 9, 2020.](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9277506)
- [“Automatic Cataract Detection and Grading Using Deep Convolutional Neural Network,” May 1, 2017.](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8000068)
- [Junayed, “CataractNet: An Automated Cataract Detection System Using Deep Learning for Fundus Images,” September 9, 2022.](https://www.academia.edu/56670364/CataractNet_An_Automated_Cataract_Detection_System_using_Deep_Learning_for_Fundus_Images)

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
