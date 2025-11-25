"""
Generate Enhanced NAPE Math Test Dataset with Expanded Demographics
Adds comprehensive demographic variables commonly used in educational research
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# ============================================================================
# CONFIGURATION
# ============================================================================

NUM_STUDENTS = 2000
NUM_QUESTIONS = 40

# ============================================================================
# ENHANCED DEMOGRAPHIC GENERATION
# ============================================================================

def generate_enhanced_demographics(n_students):
    """
    Generate comprehensive student demographic data
    """
    print("Generating enhanced demographic data...")
    
    # Basic demographics
    student_ids = [f'STU{i:06d}' for i in range(1, n_students + 1)]
    grades = np.random.choice(['6th', '7th', '8th'], size=n_students, p=[0.33, 0.34, 0.33])
    
    # Age (typically 11-14 for grades 6-8)
    age_map = {'6th': 11, '7th': 12, '8th': 13}
    ages = [age_map[grade] + np.random.choice([0, 1], p=[0.8, 0.2]) for grade in grades]
    
    # Gender with realistic distribution
    genders = np.random.choice(
        ['Male', 'Female', 'Non-binary'], 
        size=n_students, 
        p=[0.49, 0.49, 0.02]
    )
    
    # Race/Ethnicity (based on US demographics, adjust as needed)
    race_ethnicity = np.random.choice(
        ['White', 'Black/African American', 'Hispanic/Latino', 'Asian', 
         'Two or More Races', 'Native American/Alaska Native', 'Pacific Islander'],
        size=n_students,
        p=[0.45, 0.15, 0.25, 0.09, 0.04, 0.01, 0.01]
    )
    
    # Geographic setting
    schools = [f'School_{i:02d}' for i in range(1, 26)]
    school_assignments = np.random.choice(schools, size=n_students)
    
    # Assign geographic type to schools
    school_geo_map = {}
    for school in schools[:8]:
        school_geo_map[school] = 'Urban'
    for school in schools[8:18]:
        school_geo_map[school] = 'Suburban'
    for school in schools[18:]:
        school_geo_map[school] = 'Rural'
    
    geographic_setting = [school_geo_map[school] for school in school_assignments]
    
    # Socioeconomic indicators
    economic_status = np.random.choice(
        ['Low', 'Medium', 'High'],
        size=n_students,
        p=[0.35, 0.45, 0.20]
    )
    
    # Free/Reduced Lunch (correlated with economic status)
    free_reduced_lunch = []
    for econ in economic_status:
        if econ == 'Low':
            frl = np.random.choice(['Free Lunch', 'Reduced Lunch', 'Paid'], p=[0.70, 0.20, 0.10])
        elif econ == 'Medium':
            frl = np.random.choice(['Free Lunch', 'Reduced Lunch', 'Paid'], p=[0.15, 0.25, 0.60])
        else:  # High
            frl = np.random.choice(['Free Lunch', 'Reduced Lunch', 'Paid'], p=[0.02, 0.05, 0.93])
        free_reduced_lunch.append(frl)
    
    # Parent education level
    parent_education = np.random.choice(
        ['Less than High School', 'High School Diploma', 'Some College', 
         'Associate Degree', 'Bachelor Degree', 'Graduate Degree'],
        size=n_students,
        p=[0.08, 0.25, 0.22, 0.10, 0.25, 0.10]
    )
    
    # First generation college student (neither parent has 4-year degree)
    first_gen_college = [
        edu in ['Less than High School', 'High School Diploma', 'Some College', 'Associate Degree']
        for edu in parent_education
    ]
    
    # Family structure
    family_structure = np.random.choice(
        ['Two Parents', 'Single Parent', 'Grandparent(s)', 'Other Guardian'],
        size=n_students,
        p=[0.65, 0.28, 0.05, 0.02]
    )
    
    # Number of siblings
    num_siblings = np.random.choice([0, 1, 2, 3, 4, 5], size=n_students, 
                                    p=[0.15, 0.35, 0.30, 0.13, 0.05, 0.02])
    
    # Language and ELL
    home_language = np.random.choice(
        ['English', 'Spanish', 'Chinese', 'Vietnamese', 'Arabic', 'Other'],
        size=n_students,
        p=[0.75, 0.13, 0.04, 0.02, 0.02, 0.04]
    )
    
    ell_status = [lang != 'English' and np.random.random() < 0.6 for lang in home_language]
    
    # Years in US (for immigrant students)
    years_in_us = []
    for lang in home_language:
        if lang == 'English':
            years_in_us.append('Born in US')
        else:
            if np.random.random() < 0.3:  # 30% born in US but speak other language at home
                years_in_us.append('Born in US')
            else:
                years_in_us.append(str(np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])))
    
    # Special programs and services
    special_education = np.random.choice([True, False], size=n_students, p=[0.13, 0.87])
    
    gifted_talented = np.random.choice([True, False], size=n_students, p=[0.08, 0.92])
    
    section_504 = np.random.choice([True, False], size=n_students, p=[0.05, 0.95])
    
    # Special education categories (for those with IEP)
    sped_category = []
    for has_iep in special_education:
        if has_iep:
            category = np.random.choice([
                'Specific Learning Disability', 
                'Speech/Language Impairment',
                'Other Health Impairment',
                'Autism Spectrum',
                'Emotional Disturbance',
                'Intellectual Disability',
                'Multiple Disabilities'
            ], p=[0.35, 0.20, 0.15, 0.12, 0.08, 0.07, 0.03])
            sped_category.append(category)
        else:
            sped_category.append('None')
    
    # Prior achievement
    prior_achievement = np.random.choice(
        ['Below Basic', 'Basic', 'Proficient', 'Advanced'],
        size=n_students,
        p=[0.20, 0.35, 0.30, 0.15]
    )
    
    # Attendance rate (percentage, 75-100%)
    attendance_rate = np.random.beta(8, 2, size=n_students) * 25 + 75
    
    # Behavioral indicators
    discipline_incidents = np.random.choice([0, 1, 2, 3, 4, 5, 6], size=n_students,
                                           p=[0.70, 0.15, 0.08, 0.04, 0.02, 0.005, 0.005])
    
    # Technology access
    internet_at_home = np.random.choice(['Yes', 'No', 'Sometimes'], size=n_students,
                                        p=[0.82, 0.10, 0.08])
    
    device_access = np.random.choice(
        ['Personal Laptop/Tablet', 'Shared Device', 'Smartphone Only', 'School Device Only', 'No Device'],
        size=n_students,
        p=[0.55, 0.25, 0.10, 0.08, 0.02]
    )
    
    # Extracurricular participation
    extracurricular_activities = np.random.choice([0, 1, 2, 3, 4], size=n_students,
                                                   p=[0.25, 0.35, 0.25, 0.12, 0.03])
    
    # After-school care/tutoring
    after_school_program = np.random.choice(['None', 'Tutoring', 'Sports', 'Arts', 'Multiple'],
                                            size=n_students,
                                            p=[0.40, 0.15, 0.20, 0.10, 0.15])
    
    # Test accommodations
    test_accommodations = []
    for i in range(n_students):
        accoms = []
        if special_education[i] or section_504[i]:
            # IEP/504 students more likely to have accommodations
            if np.random.random() < 0.7:
                possible_accoms = ['Extended Time', 'Small Group', 'Read Aloud', 'Breaks', 'Calculator']
                num_accoms = np.random.choice([1, 2, 3], p=[0.5, 0.35, 0.15])
                accoms = list(np.random.choice(possible_accoms, size=num_accoms, replace=False))
        else:
            # Other students might have accommodations too
            if np.random.random() < 0.05:
                accoms = ['Extended Time']
        
        test_accommodations.append(', '.join(accoms) if accoms else 'None')
    
    # School characteristics (Title I status based on school)
    school_title_i = {school: np.random.choice([True, False], p=[0.55, 0.45]) for school in schools}
    is_title_i_school = [school_title_i[school] for school in school_assignments]
    
    # Combine all demographics
    demographics = pd.DataFrame({
        'student_id': student_ids,
        'age': ages,
        'grade': grades,
        'gender': genders,
        'race_ethnicity': race_ethnicity,
        'home_language': home_language,
        'ell_status': ell_status,
        'years_in_us': years_in_us,
        'school': school_assignments,
        'geographic_setting': geographic_setting,
        'is_title_i_school': is_title_i_school,
        'economic_status': economic_status,
        'free_reduced_lunch': free_reduced_lunch,
        'parent_education': parent_education,
        'first_gen_college': first_gen_college,
        'family_structure': family_structure,
        'num_siblings': num_siblings,
        'special_education': special_education,
        'sped_category': sped_category,
        'gifted_talented': gifted_talented,
        'section_504': section_504,
        'test_accommodations': test_accommodations,
        'prior_achievement': prior_achievement,
        'attendance_rate': attendance_rate,
        'discipline_incidents': discipline_incidents,
        'internet_at_home': internet_at_home,
        'device_access': device_access,
        'extracurricular_activities': extracurricular_activities,
        'after_school_program': after_school_program
    })
    
    return demographics

# ============================================================================
# ABILITY SCORE CALCULATION WITH DEMOGRAPHIC CORRELATIONS
# ============================================================================

def calculate_ability_scores(demographics):
    """
    Calculate student ability scores with realistic demographic correlations
    """
    print("Calculating ability scores with demographic correlations...")
    
    n_students = len(demographics)
    base_ability = np.random.normal(loc=0, scale=1, size=n_students)
    
    adjustments = np.zeros(n_students)
    
    for idx, student in demographics.iterrows():
        adjustment = 0
        
        # ELL adjustment
        if student['ell_status']:
            adjustment -= 0.3
        
        # Special education adjustment
        if student['special_education']:
            adjustment -= 0.4
        
        # Gifted/talented boost
        if student['gifted_talented']:
            adjustment += 0.6
        
        # Prior achievement correlation (strong predictor)
        prior_map = {'Below Basic': -0.8, 'Basic': -0.2, 'Proficient': 0.2, 'Advanced': 0.6}
        adjustment += prior_map[student['prior_achievement']]
        
        # Parent education correlation
        parent_edu_map = {
            'Less than High School': -0.3,
            'High School Diploma': -0.1,
            'Some College': 0,
            'Associate Degree': 0.1,
            'Bachelor Degree': 0.2,
            'Graduate Degree': 0.3
        }
        adjustment += parent_edu_map[student['parent_education']]
        
        # Economic status
        econ_map = {'Low': -0.2, 'Medium': 0, 'High': 0.2}
        adjustment += econ_map[student['economic_status']]
        
        # Attendance impact
        if student['attendance_rate'] < 85:
            adjustment -= 0.3
        elif student['attendance_rate'] > 95:
            adjustment += 0.1
        
        # Behavioral issues
        if student['discipline_incidents'] > 2:
            adjustment -= 0.2
        
        # Technology access (digital divide)
        if student['internet_at_home'] == 'No':
            adjustment -= 0.15
        
        # Family structure (slight correlation)
        if student['family_structure'] == 'Two Parents':
            adjustment += 0.05
        
        # Years in US (for non-native students)
        if student['years_in_us'] not in ['Born in US', 'None']:
            years = int(student['years_in_us'])
            if years < 3:
                adjustment -= 0.25
            elif years < 5:
                adjustment -= 0.15
        
        # Geographic setting (resource differences)
        geo_map = {'Rural': -0.1, 'Urban': 0, 'Suburban': 0.1}
        adjustment += geo_map[student['geographic_setting']]
        
        # Extracurricular participation (enrichment)
        if student['extracurricular_activities'] >= 2:
            adjustment += 0.1
        
        adjustments[idx] = adjustment
    
    # Add adjustments to base ability with some noise
    ability_scores = base_ability + adjustments + np.random.normal(0, 0.2, size=n_students)
    
    return ability_scores

# ============================================================================
# MAIN GENERATION FUNCTION
# ============================================================================

def generate_enhanced_nape_dataset():
    """
    Generate complete NAPE dataset with enhanced demographics
    """
    print("="*70)
    print("GENERATING ENHANCED NAPE DATASET WITH EXPANDED DEMOGRAPHICS")
    print("="*70)
    print()
    
    # Generate demographics
    demographics = generate_enhanced_demographics(NUM_STUDENTS)
    
    # Calculate ability scores
    ability_scores = calculate_ability_scores(demographics)
    demographics['ability_score'] = ability_scores
    
    # Load existing test data (questions and responses)
    print("\nLoading test structure...")
    questions = pd.read_csv('/home/claude/nape_questions.csv')
    
    # Generate responses using existing function
    print("Generating test responses...")
    from generate_nape_dataset import generate_response
    
    responses = []
    for idx, student in demographics.iterrows():
        student_id = student['student_id']
        ability = student['ability_score']
        
        for _, question in questions.iterrows():
            points, is_correct = generate_response(ability, question)
            
            responses.append({
                'student_id': student_id,
                'question_id': question['question_id'],
                'points_earned': points,
                'max_points': question['max_points'],
                'is_correct': is_correct,
                'response_time_sec': int(np.random.gamma(3, 30))
            })
        
        if (idx + 1) % 200 == 0:
            print(f"  Processed {idx + 1}/{NUM_STUDENTS} students...")
    
    responses_df = pd.DataFrame(responses)
    
    # Calculate summary statistics
    print("\nCalculating summary statistics...")
    
    student_scores = responses_df.groupby('student_id').agg({
        'points_earned': 'sum',
        'is_correct': 'sum',
        'response_time_sec': 'sum'
    }).reset_index()
    
    student_scores.columns = ['student_id', 'total_points', 'total_correct', 'total_time_sec']
    
    max_possible = questions['max_points'].sum()
    student_scores['max_possible_points'] = max_possible
    student_scores['percent_score'] = (student_scores['total_points'] / max_possible) * 100
    student_scores['accuracy'] = (student_scores['total_correct'] / NUM_QUESTIONS) * 100
    
    def assign_performance_level(percent):
        if percent >= 80:
            return 'Advanced'
        elif percent >= 60:
            return 'Proficient'
        elif percent >= 40:
            return 'Basic'
        else:
            return 'Below Basic'
    
    student_scores['performance_level'] = student_scores['percent_score'].apply(assign_performance_level)
    
    # Merge demographics with scores
    student_complete = demographics.merge(student_scores, on='student_id')
    
    # Save files
    print("\nSaving enhanced datasets...")
    student_complete.to_csv('/home/claude/nape_students_enhanced.csv', index=False)
    responses_df.to_csv('/home/claude/nape_responses_enhanced.csv', index=False)
    
    # Create wide format
    responses_wide = responses_df.pivot(
        index='student_id',
        columns='question_id',
        values='points_earned'
    ).reset_index()
    
    responses_wide = demographics.merge(responses_wide, on='student_id')
    responses_wide.to_csv('/home/claude/nape_responses_wide_enhanced.csv', index=False)
    
    print("\n" + "="*70)
    print("ENHANCED DATASET GENERATION COMPLETE!")
    print("="*70)
    
    print("\nFiles created:")
    print("  1. nape_students_enhanced.csv - Complete demographics & scores")
    print("  2. nape_responses_enhanced.csv - All responses (80,000 rows)")
    print("  3. nape_responses_wide_enhanced.csv - Wide format")
    
    print("\n" + "="*70)
    print("DEMOGRAPHIC VARIABLES INCLUDED")
    print("="*70)
    print("\nBasic Demographics:")
    print("  - Student ID, Age, Grade, Gender")
    print("  - Race/Ethnicity (7 categories)")
    print("\nLanguage & Immigration:")
    print("  - Home Language, ELL Status, Years in US")
    print("\nSocioeconomic Indicators:")
    print("  - Economic Status, Free/Reduced Lunch")
    print("  - Parent Education Level, First Gen College")
    print("  - Family Structure, Number of Siblings")
    print("\nSchool Context:")
    print("  - School Assignment (25 schools)")
    print("  - Geographic Setting (Urban/Suburban/Rural)")
    print("  - Title I School Status")
    print("\nSpecial Programs:")
    print("  - Special Education & Category")
    print("  - Gifted/Talented, Section 504")
    print("  - Test Accommodations")
    print("\nAcademic & Behavioral:")
    print("  - Prior Achievement Level")
    print("  - Attendance Rate")
    print("  - Discipline Incidents")
    print("\nAccess & Opportunity:")
    print("  - Internet at Home, Device Access")
    print("  - Extracurricular Activities")
    print("  - After-School Programs")
    print("\nPerformance Measures:")
    print("  - Ability Score (IRT-based)")
    print("  - Total Points, Percent Score")
    print("  - Performance Level")
    
    return student_complete, responses_df, responses_wide

# ============================================================================
# RUN
# ============================================================================

if __name__ == "__main__":
    student_data, responses, responses_wide = generate_enhanced_nape_dataset()
    
    print("\n" + "="*70)
    print("SAMPLE STATISTICS")
    print("="*70)
    
    print(f"\nMean Score: {student_data['percent_score'].mean():.1f}%")
    print(f"\nRace/Ethnicity Distribution:")
    print(student_data['race_ethnicity'].value_counts())
    print(f"\nELL Students: {student_data['ell_status'].sum()} ({student_data['ell_status'].mean()*100:.1f}%)")
    print(f"Special Education: {student_data['special_education'].sum()} ({student_data['special_education'].mean()*100:.1f}%)")
    print(f"Gifted/Talented: {student_data['gifted_talented'].sum()} ({student_data['gifted_talented'].mean()*100:.1f}%)")
    print(f"\nFree/Reduced Lunch:")
    print(student_data['free_reduced_lunch'].value_counts())
    
    print("\n" + "="*70)
    print("Ready to analyze!")
    print("="*70)
