# SIFT-KNN Aerial Landscape Image Classification

This project uses SIFT (Scale-Invariant Feature Transform) feature extraction and K-Nearest Neighbors (KNN) classifier to identify different types of aerial landscape images.

## Overview

The project implements an image classification system that:
1. Extracts SIFT features from aerial landscape images
2. Creates a Bag-of-Visual-Words (BoVW) representation using K-means clustering
3. Classifies images using a KNN classifier
4. Tests different data scenarios (original, augmented, imbalanced) to evaluate model robustness

## Dataset

- **Aerial Landscape Images**: A dataset containing aerial views of different landscape types
- Source: [Skyview - An Aerial Landscape Dataset](https://www.kaggle.com/datasets/ankit1743/skyview-an-aerial-landscape-dataset)
- Categories include: River, Airport, Beach, Port, Agriculture, Desert, Lake, Grassland, Highway, City, Parking, Forest, Mountain, Residential, Railway

## Project Structure

- `indexGenerate.py`: Creates a CSV index of all images in the dataset
- `dataSpliter.py`: Splits the dataset into training and test sets (80/20 split)
- `reader.py`: Utility script to read and check dataset statistics
- `origin.ipynb`: Baseline implementation using the original dataset distribution
- `augment.ipynb`: Implementation with data augmentation to improve model robustness
- `imbalance.ipynb`: Implementation with deliberately imbalanced data to test model performance

## Setup Instructions

1. Clone this repository
2. Download the [Aerial Landscape Dataset](https://www.kaggle.com/datasets/ankit1743/skyview-an-aerial-landscape-dataset) and extract it to the project folder
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the following scripts in order:
   ```
   python indexGenerate.py
   python dataSpliter.py
   ```
5. Run any of the following to train and evaluate different models:
   ```
   origin.ipynb     # Original dataset
   augment.ipynb    # With data augmentation
   imbalance.ipynb  # With imbalanced data
   ```

## Method Details

### Feature Extraction

The project uses SIFT to extract local features from images. SIFT is robust to changes in scale, rotation, and illumination, making it suitable for aerial image classification.

### Bag of Visual Words (BoVW)

To create a fixed-length feature vector for each image:
- SIFT descriptors from all training images are clustered using K-means (k=300)
- Each image is represented as a histogram of visual words based on the cluster assignments of its SIFT descriptors

### Classification

A KNN classifier (k=5) is used to classify images based on their BoVW representations.

## Experimental Scenarios

1. **Original Dataset**: Baseline model using the original data distribution
2. **Data Augmentation**: Enhances training data by applying:
   - Random rotation
   - Random flipping
   - Noise addition
   - Brightness adjustments
3. **Imbalanced Dataset**: Tests model robustness by deliberately creating class imbalance

## Results

Each experiment produces:
- Overall accuracy metrics
- Per-class accuracy metrics
- Confusion matrix visualization
- Classification report with precision, recall, and F1-score

## Requirements

- Python >=3.11
- OpenCV
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib

## License

This project is available for educational and research purposes.