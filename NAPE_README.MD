# 🐍 Python Scripts Guide

## 📋 Scripts Included

You have **3 Python scripts** that power the entire NAPE dataset generation and analysis:

1. **generate_nape_dataset.py** - Original dataset generator
2. **generate_nape_enhanced.py** - Enhanced demographics generator ⭐
3. **analyze_enhanced_demographics.py** - Comprehensive analysis

---

## 🎯 Script 1: generate_nape_enhanced.py ⭐ **MAIN SCRIPT**

### **What It Does**
Generates the complete NAPE dataset with 30+ demographic variables using Item Response Theory (IRT) for realistic test responses.

### **Outputs Generated**
- `nape_students_enhanced.csv` (2,000 students × 40+ columns)
- `nape_responses_enhanced.csv` (80,000 rows)
- `nape_responses_wide_enhanced.csv` (2,000 rows)

### **Key Features**
- ✅ 30+ demographic variables
- ✅ IRT-based test responses (2PL model)
- ✅ Realistic correlations between demographics and achievement
- ✅ 40 questions across 6 content areas
- ✅ Multiple question types (MC, short answer, extended response)
- ✅ Partial credit scoring

### **How to Use**

```bash
# Run the script
python generate_nape_enhanced.py

# Or if you have Python 3 specifically
python3 generate_nape_enhanced.py
```

### **Customization Options**

Edit these variables at the top of the script:

```python
# Number of students (default: 2000)
NUM_STUDENTS = 2000

# Number of questions (default: 40)
NUM_QUESTIONS = 40

# Content areas and their question counts
CONTENT_AREAS = {
    'Number_Operations': 10,
    'Algebra': 8,
    'Geometry': 8,
    'Measurement': 6,
    'Data_Statistics': 5,
    'Problem_Solving': 3
}
```

### **Adjusting Difficulty**

```python
# In create_question_bank() function
# Change the difficulty proportions
if i < num_questions * 0.3:       # First 30% are Easy
    difficulty = DIFFICULTY_EASY
elif i < num_questions * 0.7:     # Next 40% are Medium
    difficulty = DIFFICULTY_MEDIUM
else:                               # Last 30% are Hard
    difficulty = DIFFICULTY_HARD
```

### **Adjusting Demographics**

```python
# In generate_enhanced_demographics() function

# Change race/ethnicity distribution
race_ethnicity = np.random.choice(
    ['White', 'Black/African American', 'Hispanic/Latino', 'Asian', ...],
    size=n_students,
    p=[0.45, 0.15, 0.25, 0.09, ...]  # ← Adjust these percentages
)

# Change ELL rate
ell_status = [lang != 'English' and np.random.random() < 0.6 for lang in home_language]
                                                          # ↑ Change from 0.6 to adjust ELL rate

# Change special education rate
special_education = np.random.choice([True, False], size=n_students, 
                                     p=[0.13, 0.87])  # ← 13% SPED rate
```

### **Adjusting Correlations**

In the `calculate_ability_scores()` function:

```python
# ELL adjustment (currently -0.3 SD)
if student['ell_status']:
    adjustment -= 0.3  # ← Change this value

# Special education adjustment (currently -0.4 SD)
if student['special_education']:
    adjustment -= 0.4  # ← Change this value

# Parent education correlation
parent_edu_map = {
    'Less than High School': -0.3,  # ← Adjust these
    'High School Diploma': -0.1,
    'Some College': 0,
    'Associate Degree': 0.1,
    'Bachelor Degree': 0.2,
    'Graduate Degree': 0.3
}
```

### **Dependencies**

```bash
pip install numpy pandas
```

### **Runtime**
- Small dataset (500 students): ~10 seconds
- Default (2,000 students): ~30 seconds
- Large dataset (10,000 students): ~3 minutes

---

## 🎯 Script 2: generate_nape_dataset.py

### **What It Does**
Generates the **original simpler version** with only 8 demographic variables.

### **Outputs Generated**
- `nape_students.csv`
- `nape_questions.csv`
- `nape_question_stats.csv`
- `nape_responses.csv`
- `nape_responses_wide.csv`

### **When to Use**
- Teaching basic educational data analysis
- Don't need comprehensive demographics
- Want faster generation
- Simpler examples

### **How to Run**

```bash
python generate_nape_dataset.py
```

### **Key Differences from Enhanced Version**

| Feature | Original | Enhanced |
|---------|----------|----------|
| Demographic variables | 8 | 30+ |
| Race/ethnicity | 1 variable | 7 categories |
| SES indicators | 1 (economic status) | 4 (FRL, parent ed, etc.) |
| Special programs | Basic SPED/GT | Detailed categories + 504 |
| School context | School ID only | Geography, Title I |
| Technology access | No | Yes (internet, devices) |
| Attendance/behavior | No | Yes |

---

## 🎯 Script 3: analyze_enhanced_demographics.py

### **What It Does**
Comprehensive analysis and visualization of the enhanced dataset.

### **Outputs Generated**
- `enhanced_achievement_gaps.png` (9-panel visualization)
- `enhanced_intersectional.png` (intersectional analysis)
- `enhanced_correlations.png` (correlation matrix)
- `enhanced_analysis_report.txt` (summary statistics)

### **How to Use**

```bash
# Must run AFTER generating the enhanced dataset
python analyze_enhanced_demographics.py
```

### **What It Analyzes**

1. **Achievement Gaps** (9 panels):
   - Race/ethnicity
   - ELL status
   - Free/reduced lunch
   - Parent education
   - Special programs
   - Geographic setting
   - Title I schools
   - Internet access
   - Attendance rates

2. **Intersectional Patterns**:
   - Race × ELL status
   - Gender × Parent education
   - SES × Geography
   - Special Ed × Accommodations

3. **Correlations**:
   - All variables vs. achievement
   - Heatmap visualization

4. **Statistical Summary**:
   - Gap sizes
   - Effect sizes
   - Key findings

### **Customizing Visualizations**

```python
# Change figure size
fig, axes = plt.subplots(3, 3, figsize=(18, 14))  # ← Adjust dimensions

# Change color schemes
colors = ['#2ca02c', '#d62728']  # ← Change hex colors

# Add more analyses
# Add your own visualization code at the end
plt.figure(figsize=(10, 6))
students.groupby('your_variable')['percent_score'].mean().plot(kind='bar')
plt.savefig('/home/claude/custom_analysis.png')
```

### **Dependencies**

```bash
pip install pandas matplotlib seaborn numpy scikit-learn
```

### **Runtime**
~15-30 seconds (includes creating multiple high-res visualizations)

---

## 🔄 Complete Workflow

### **Option A: Generate Everything Fresh**

```bash
# Step 1: Generate enhanced dataset
python generate_nape_enhanced.py
# Creates: nape_students_enhanced.csv, nape_responses_enhanced.csv, etc.

# Step 2: Analyze it
python analyze_enhanced_demographics.py
# Creates: All visualizations and reports
```

### **Option B: Just Generate Original Dataset**

```bash
# Generate simple version
python generate_nape_dataset.py
# Creates: Original 5 CSV files with basic demographics
```

### **Option C: Generate Both Versions**

```bash
# Generate original
python generate_nape_dataset.py

# Generate enhanced
python generate_nape_enhanced.py

# Analyze enhanced version
python analyze_enhanced_demographics.py
```

---

## 🛠️ Advanced Customization Examples

### **Example 1: Change Sample Size**

```python
# In generate_nape_enhanced.py
NUM_STUDENTS = 5000  # Instead of 2000

# In generate_nape_dataset.py
NUM_STUDENTS = 5000
```

### **Example 2: Add New Demographic Variable**

```python
# In generate_enhanced_demographics() function

# Add after existing demographics
is_homeless = np.random.choice([True, False], size=n_students, p=[0.03, 0.97])

# Add to the DataFrame
demographics = pd.DataFrame({
    'student_id': student_ids,
    # ... existing variables ...
    'is_homeless': is_homeless,  # ← New variable
})
```

### **Example 3: Add New Content Area**

```python
# In generate_nape_enhanced.py or generate_nape_dataset.py

CONTENT_AREAS = {
    'Number_Operations': 10,
    'Algebra': 8,
    'Geometry': 8,
    'Measurement': 6,
    'Data_Statistics': 5,
    'Problem_Solving': 3,
    'Probability': 5,  # ← New content area
}

# Increase NUM_QUESTIONS accordingly
NUM_QUESTIONS = 45  # Was 40
```

### **Example 4: Change Score Distribution**

```python
# In calculate_ability_scores() function

# Make scores higher overall
base_ability = np.random.normal(loc=0.5, scale=1, size=n_students)  # Was loc=0

# Make scores more spread out
base_ability = np.random.normal(loc=0, scale=1.5, size=n_students)  # Was scale=1
```

### **Example 5: Add Longitudinal Data (Multiple Time Points)**

```python
# At the end of generate_nape_enhanced.py

# Generate Time 2 data (6 months later)
print("\nGenerating Time 2 data...")
student_data_t2 = student_data.copy()
student_data_t2['time_point'] = 2

# Adjust scores slightly (students improve on average)
student_data_t2['ability_score'] += np.random.normal(0.2, 0.3, size=len(student_data_t2))

# Combine
longitudinal_data = pd.concat([
    student_data.assign(time_point=1),
    student_data_t2
])

longitudinal_data.to_csv('/home/claude/nape_longitudinal.csv', index=False)
```

---

## 📊 Understanding the IRT Model

The scripts use Item Response Theory (IRT) to generate realistic test responses:

```python
def irt_probability(ability, difficulty, discrimination=1.0):
    """
    2-Parameter Logistic (2PL) Model
    
    Parameters:
    - ability: Student's latent ability (standardized, mean=0, sd=1)
    - difficulty: Question difficulty (0-1, proportion expected to get correct)
    - discrimination: How well question differentiates students (0.8-1.5)
    
    Returns:
    - Probability of correct response (0-1)
    """
    difficulty_logit = np.log(difficulty / (1 - difficulty))
    prob = 1 / (1 + np.exp(-discrimination * (ability - difficulty_logit)))
    return prob
```

**What this means:**
- High-ability students have higher probability of getting questions correct
- Easy questions (high difficulty value) have high probability for all students
- Hard questions (low difficulty value) only high-ability students answer correctly
- Discrimination parameter controls how sharply probability changes with ability

---

## 🐛 Troubleshooting

### **Issue: "ModuleNotFoundError: No module named 'pandas'"**

**Solution:**
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### **Issue: "FileNotFoundError: nape_questions.csv"**

**Solution:** The enhanced script requires the original questions file.
```bash
# Run original first to create question bank
python generate_nape_dataset.py

# Then run enhanced
python generate_nape_enhanced.py
```

Or modify `generate_nape_enhanced.py` to not depend on it (use the question creation function directly).

### **Issue: Scripts are slow**

**Solution:** Reduce number of students
```python
NUM_STUDENTS = 500  # Instead of 2000
```

### **Issue: Want different random results**

**Solution:** Change the random seed
```python
np.random.seed(42)  # Change 42 to any number
random.seed(42)
```

---

## 📝 Code Quality Notes

### **Best Practices Used**
- ✅ Clear function documentation
- ✅ Configurable parameters
- ✅ Progress indicators
- ✅ Error handling
- ✅ Modular design
- ✅ Reproducible (random seed set)

### **Extending the Code**

The code is designed to be extended:

```python
# Add new demographic generation function
def generate_additional_demographics(n_students):
    """Your custom demographics"""
    return pd.DataFrame({
        'student_id': student_ids,
        'new_variable': your_data
    })

# Call it in main generation
demographics = generate_enhanced_demographics(NUM_STUDENTS)
additional = generate_additional_demographics(NUM_STUDENTS)
demographics = demographics.merge(additional, on='student_id')
```

---

## 🎓 Learning Resources

### **Understanding IRT**
- [Item Response Theory Primer](https://en.wikipedia.org/wiki/Item_response_theory)
- Baker, F. B. (2001). *The Basics of Item Response Theory*

### **Pandas Documentation**
- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)

### **Data Generation Best Practices**
- Use consistent random seeds for reproducibility
- Document all distributional assumptions
- Validate generated data matches expectations
- Include realistic correlations

---

## 📞 Support

**Common Tasks:**

1. **Generate new dataset:** Run `generate_nape_enhanced.py`
2. **Change demographics:** Edit percentages in `generate_enhanced_demographics()`
3. **Change correlations:** Edit adjustments in `calculate_ability_scores()`
4. **Add visualizations:** Extend `analyze_enhanced_demographics.py`
5. **Change test structure:** Edit `CONTENT_AREAS` and `NUM_QUESTIONS`

**Next Steps:**
- Modify the scripts for your specific needs
- Generate multiple datasets with different parameters
- Compare how changes affect results
- Use as template for other synthetic data projects

---

## 📦 All Python Scripts Summary

| Script | Purpose | Runtime | Dependencies |
|--------|---------|---------|--------------|
| `generate_nape_enhanced.py` ⭐ | Generate enhanced dataset | 30 sec | numpy, pandas |
| `generate_nape_dataset.py` | Generate original dataset | 30 sec | numpy, pandas |
| `analyze_enhanced_demographics.py` | Analyze & visualize | 30 sec | pandas, matplotlib, seaborn, sklearn |

**Total Runtime:** ~90 seconds to generate everything from scratch!

---

<div align="center">

**🐍 Ready to generate your own educational datasets! 🐍**

*All scripts are documented, customizable, and ready to extend*

</div>
