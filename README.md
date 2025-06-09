# University Admission Prediction Web Application

A Flask-based web application that predicts the probability of university admission using machine learning. The application uses Linear Regression to estimate admission chances based on academic and research credentials including GRE scores, TOEFL scores, university rating, CGPA, and research experience.

## Features

- **Web Interface**: User-friendly form for inputting academic credentials
- **Machine Learning**: Linear Regression model for admission probability prediction
- **Percentage Output**: Results displayed as percentage probability
- **Real-time Predictions**: Instant admission chance estimates
- **Academic Focus**: Tailored for graduate school admission predictions

## Technologies Used

- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn (Linear Regression)
- **Data Processing**: pandas
- **Frontend**: HTML templates (Jinja2)
- **Dataset**: University admission data (CSV format)

## Project Structure

```
admission-predictor/
│
├── app.py                # Main Flask application
├── admission.csv         # Dataset for training
├── templates/
│   ├── index.html       # Home page template
│   └── predict.html     # Prediction form and results template
├── static/              # CSS, JS, images (if any)
└── README.md           # Project documentation
```

## Installation & Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/lovnishverma/AddmissionChancesPrediction.git
cd AddmissionChancesPrediction
```

### Step 2: Install Dependencies

```bash
pip install flask pandas scikit-learn
```

### Step 3: Prepare the Dataset

Ensure `admission.csv` is in the root directory. The CSV should contain 6 columns (without headers):
- Column 1: GRE Score (290-340)
- Column 2: TOEFL Score (92-120)
- Column 3: University Rating (1-5)
- Column 4: CGPA (6.8-9.92)
- Column 5: Research Experience (0 or 1)
- Column 6: Chance of Admission (0.34-0.97)

### Step 4: Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

## Usage

1. **Home Page**: Navigate to `http://localhost:5000` to access the home page
2. **Prediction Form**: Go to `http://localhost:5000/page` or use the navigation
3. **Input Academic Details**: Fill in your credentials:
   - **GRE Score**: Graduate Record Examination score (typically 290-340)
   - **TOEFL Score**: Test of English as a Foreign Language score (typically 92-120)
   - **University Rating**: Rating of undergraduate university (1-5 scale)
   - **CGPA**: Cumulative Grade Point Average (typically 6.8-9.92)
   - **Research Experience**: Previous research experience (0 = No, 1 = Yes)
4. **Get Prediction**: Submit the form to get your admission probability percentage

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page |
| `/page` | GET | Prediction form page |
| `/predict` | POST | Process prediction and return results |

## Model Details

- **Algorithm**: Linear Regression
- **Features**: GRE Score, TOEFL Score, University Rating, CGPA, Research Experience
- **Target**: Chance of Admission (converted to percentage)
- **Training**: Model trains on the entire dataset for each prediction

## Input Parameters

| Parameter | Type | Range | Description |
|-----------|------|-------|-------------|
| GRE Score | Integer | 290-340 | Graduate Record Examination score |
| TOEFL Score | Integer | 92-120 | Test of English as a Foreign Language score |
| University Rating | Integer | 1-5 | Undergraduate university rating |
| CGPA | Float | 6.8-9.92 | Cumulative Grade Point Average |
| Research Experience | Integer | 0-1 | Previous research experience (0=No, 1=Yes) |

## Sample Input Values

### High Admission Probability
- GRE: 330, TOEFL: 115, University Rating: 5, CGPA: 9.5, Research: 1
- Expected Result: ~85-95% admission chance

### Medium Admission Probability
- GRE: 315, TOEFL: 105, University Rating: 3, CGPA: 8.5, Research: 0
- Expected Result: ~65-75% admission chance

### Lower Admission Probability
- GRE: 300, TOEFL: 95, University Rating: 2, CGPA: 7.5, Research: 0
- Expected Result: ~40-50% admission chance

## Understanding the Results

The application returns a percentage representing the probability of admission:
- **80-100%**: Very High Chance - Excellent profile
- **60-79%**: High Chance - Strong profile
- **40-59%**: Moderate Chance - Good profile, consider improvements
- **20-39%**: Lower Chance - Profile needs strengthening
- **0-19%**: Very Low Chance - Significant improvements needed

## Data Science Insights

The model considers the following factors in order of typical importance:
1. **CGPA**: Academic performance indicator
2. **GRE Score**: Standardized test performance
3. **Research Experience**: Practical experience in field
4. **TOEFL Score**: English proficiency (for international students)
5. **University Rating**: Undergraduate institution prestige

## Potential Improvements

1. **Model Enhancement**: 
   - Try Random Forest or Gradient Boosting for better accuracy
   - Add cross-validation for model evaluation
   - Implement feature scaling/normalization

2. **Data Quality**:
   - Add data validation and error handling
   - Include more diverse datasets
   - Handle missing values appropriately

3. **User Experience**:
   - Add input validation with helpful error messages
   - Include tooltips explaining score ranges
   - Show confidence intervals for predictions

4. **Performance**:
   - Cache trained model to avoid retraining
   - Add model versioning and updates
   - Implement batch predictions

5. **Features**:
   - Add prediction history
   - Include admission tips based on scores
   - Compare with similar profiles

## Important Notes

- **Accuracy**: Predictions are estimates based on historical data
- **Limitations**: Model may not account for all admission factors (essays, recommendations, etc.)
- **Updates**: Retrain model periodically with new data for better accuracy
- **Scope**: Best suited for graduate program admissions

## Troubleshooting

### Common Issues

1. **Dependencies Not Found**:
   ```bash
   pip install flask pandas scikit-learn
   ```

2. **CSV File Missing**: Ensure `admission.csv` is in the root directory

3. **Port Issues**: Change port if 5000 is occupied:
   ```python
   app.run(debug=True, port=5001)
   ```

4. **Data Format Errors**: Verify CSV has 6 columns without headers

## Dataset Format

The `admission.csv` should look like:
```
337,118,4,9.65,1,0.92
324,107,4,8.87,1,0.76
316,104,3,8.00,1,0.72
...
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/enhancement`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/enhancement`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Dataset sources and contributors
- scikit-learn community for machine learning tools
- Flask community for web framework

## Contact

For questions, suggestions, or support, please open an issue in the repository.

---

**Disclaimer**: This tool provides estimates based on historical data and should not be the sole factor in making admission decisions. Always consult official university guidelines and admission counselors.
