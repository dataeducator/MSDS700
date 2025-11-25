## 🎯 Common Use Cases & Examples

### **1. Analyze Achievement Gaps**

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load data
students = pd.read_csv('nape_students.csv')

# Compare by economic status
gap_analysis = students.groupby('economic_status')['percent_score'].agg(['mean', 'std', 'count'])
print(gap_analysis)

# Visualize
gap_analysis['mean'].plot(kind='bar', yerr=gap_analysis['std'])
plt.title('Achievement Gap by Economic Status')
plt.ylabel('Mean Score (%)')
plt.show()
```

### **2. Item Analysis - Find Problematic Questions**

```python
# Load question stats
questions = pd.read_csv('nape_question_stats.csv')

# Find questions that were too hard or too easy
too_hard = questions[questions['percent_correct'] < 0.3]
too_easy = questions[questions['percent_correct'] > 0.9]

print(f"Too hard: {len(too_hard)} questions")
print(f"Too easy: {len(too_easy)} questions")
```

### **3. Predict Student Performance (Machine Learning)**

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Prepare features
X = students[['ability_score', 'grade', 'economic_status', 'ell_status', 
              'special_education', 'prior_achievement']]
X = pd.get_dummies(X)  # Convert categorical to numeric

y = students['performance_level']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier()
model.fit(X_train, y_train)

print(f"Accuracy: {model.score(X_test, y_test):.2%}")
```

### **4. Analyze Response Patterns**

```python
# Load responses
responses = pd.read_csv('nape_responses.csv')

# Find students who guessed (fast responses, low accuracy)
student_patterns = responses.groupby('student_id').agg({
    'is_correct': 'mean',
    'response_time_sec': 'mean'
})

# Identify potential guessers
guessers = student_patterns[
    (student_patterns['is_correct'] < 0.3) & 
    (student_patterns['response_time_sec'] < 60)
]

print(f"Potential guessers: {len(guessers)} students")
```

### **5. Content Area Strength/Weakness Analysis**

```python
# Merge responses with question metadata
responses_full = responses.merge(
    pd.read_csv('nape_questions.csv')[['question_id', 'content_area']], 
    on='question_id'
)

# Calculate performance by content area per student
content_performance = responses_full.groupby(['student_id', 'content_area'])['is_correct'].mean().unstack()

# Find students weak in specific areas
weak_in_algebra = content_performance[content_performance['Algebra'] < 0.4].index
print(f"Students struggling with Algebra: {len(weak_in_algebra)}")
