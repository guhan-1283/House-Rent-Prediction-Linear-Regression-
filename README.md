# House Price Prediction — End to End

## Project Overview
This repository demonstrates an end-to-end linear regression workflow to predict house rents/prices using a tabular dataset. It includes a Jupyter notebook for training and a small app to run predictions.

## Files
- [app.py](app.py) — web application to run the trained model for inference.
- [Model_Training.ipynb](Model_Training.ipynb) — Notebook used to explore data, train, and save the model.
- [House_Rent_Dataset.csv](House_Rent_Dataset.csv) — Dataset used for training and evaluation.
- [requirements.txt](requirements.txt) — Python dependencies required by the project.

## Requirements
Install dependencies with:

```bash
pip install -r requirements.txt
```

## Usage
1. To explore and retrain the model, open and run the notebook: [Model_Training.ipynb](Model_Training.ipynb).
2. To run the app (inference), execute:

```bash
python app.py
```

The app will load the saved model and run sample predictions (see `app.py` for details).

## Retraining the Model
- Open [Model_Training.ipynb](Model_Training.ipynb).
- Update parameters or preprocessing as needed.
- Re-run cells to train and save the model artifact (the notebook contains the save/export steps).

## Dataset
The dataset is provided as [House_Rent_Dataset.csv](House_Rent_Dataset.csv). Inspect the notebook for preprocessing steps applied before training.

## Notes
- This project uses a simple linear regression baseline; consider feature engineering and cross-validation for better performance.
- Adjust `requirements.txt` if you add packages while experimenting.

## Contact
If you need changes or additions to the README, tell me what to include and I'll update it.
