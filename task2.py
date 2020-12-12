def change_working_dir(new_directory='', verbose=False):
    import os
    if verbose:
        print('Working directory was: {0}'.format(os.getcwd()))
    in_str = new_directory
    if in_str == '':
        in_str = os.path.dirname(os.path.realpath)
    os.chdir(in_str)
    if verbose:
        print('Working directory is now: {0}'. format(os.getcwd()))
def get_letter_grade(grade):
        grade = [
            (90, 'A'),
            (80, 'B'),
            (70, 'C'),
            (60, 'D'),
            (00, 'F'),
        ]
def get_grade_points(score):
            score = {
            '90', 4.00,
            '80', 3.00,
            '70', 2.00,
            '60', 1.00,
            '00', 0.00
            }
def main(testing=False):
    import pandas as pd
    FILE = 'scores.csv'
    change_working_dir() 
    df_scores = pd.read_csv(FILE, delimiter=',', indexy_col=0, header=0)
    df_letter_grades = df_scores.applymap(get_letter_grade)
    df_grade_points = df_letter_grades.applymap(get_grade_points)
    df_grade_points['The class GPA is'] = df_grade_points.mean(axis=1)
    df_grade_points = df_grade_points.transpose()
    df_grade_points['GPA'] = df_grade_points.mean(axis=1).round(2)
    series = df_grade_points['GPA']
    print(series.to_string())
                
    
