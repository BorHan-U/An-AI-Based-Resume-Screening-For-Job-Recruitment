# Topic: An AI based resume screening
# - Md Borhan Udiin
# - Amelia Ritahni Ismail


# import required packeges(This section will include all future required packages)
#import PyPDF2
import textract
import re
import string
import pandas as pd
import matplotlib.pyplot as plt
import colorama
from colorama import Fore, Style

# This section will open the pdf file
# open the pdf file
file = open('Data Scientist-2.pdf', 'rb')
reader = PyPDF2.PdfFileReader(file)  # Read file

number_Of_pages = reader.numPages  # Get total number of pages
print("\n\nThe uploaded resume contains", number_Of_pages,
      "pages and intrepreter successfully read all the", number_Of_pages, "pages")

# Initialize a text empty variable
content = ""

# Extract text from every page on the file(resume)
for page_number in range(number_Of_pages):
    page = reader.getPage(page_number)
    content += page.extractText()

with open("encoded.txt", "wb") as newfile:
    newfile.write(content.encode("UTF-8"))

# print(content)
file.close()

# Convert all resume strings to lowercase alphabet
content = content.lower()

# Remove resume's uses of numeric numbers
content = re.sub(r'[0-9]+', '', content)

# Ignore the punctuation from whole contect
content = content.translate(str.maketrans('', '', string.punctuation))

# print latest content(lowercase and without number and punctuation)
# print(content)

# Create dictionary of data scientist recruitment by the compnay
Area_with_key_term = {'Data science': ['algorithm', 'analytics', 'hadoop', 'machine learning', 'data mining', 'python',
                                       'statistics', 'data', 'statistical analysis', 'data wrangling', 'algebra', 'Probability',
                                       'visualization'],

                      'Programming': ['python', 'r programming', 'sql', 'c++' 'scala', 'julia', 'tableau',
                                      'javasript', 'powerbI', 'code', 'coding', 'javascript', 'python'],

                      'Experience': ['project', 'years', 'company', 'excellency', 'promotion', 'award',
                                     'outsourcing', 'work in progress'],

                      'Management skill': ['administration', 'budget', 'cost', 'direction', 'feasibility analysis',
                                           'finance', 'leader', 'leadership', 'management', 'milestones', 'planning',
                                           'problem', 'project', 'risk', 'schedule', 'stakeholders', 'English'],

                      'Data analytics': ['api', 'big data', 'clustering', 'code', 'coding', 'data', 'database',
                                         'data mining', 'data science', 'deep learning', 'hadoop',
                                         'hypothesis test', 'machine learning', 'dbms', 'modeling', 'nlp',
                                         'predictive', 'text mining', 'visualuzation'],

                      'Statistics': ['parameter', 'vaiable', 'ordinal', 'ratio', 'nominal', 'interval', 'descriptive',
                                     'inferential', 'linear', 'correlations', 'probability',
                                     'regression', 'mean', 'variance', 'standard deviation'],

                      'Machine learning': ['supervised learning', 'unsupervised learning', 'ann', 'artificial neural network',
                                           'overfitting', 'computer vision', 'natural language processing',
                                           'database'],

                      'Data analyst': ['data collection', 'data cleaning', 'data Processing', 'interpreting data',
                                       'streamlining data', 'visualizing data', 'statistics',
                                       'tableau', 'tables', 'analytical'],

                      'Software': ['django', 'cloud', 'gcp', 'aws', 'javacript', 'react', 'redux',
                                   'es6', 'node.js', 'typescript', 'html', 'css', 'ui', 'ci/cd', 'cashflow'],

                      'Web skill': ['web design', 'branding', 'graphic design', 'seo', 'marketing', 'logo design', 'video editing',
                                    'es6', 'node.js', 'typescript', 'html/css',
                                    'ci/cd'],

                      'Personal Skill': ['leadership', 'team work', 'integrity', 'public speaking', 'team leadership', 'problem solving', 'loyalty', 'quality', 'performance improvement', 'six sigma',
                                         'quality circles', 'quality tools' 'process improvement', 'capability analysis', 'control'],

                      'Accounting': ['communication', 'sales', 'sales process', 'solution selling', 'crm',
                                     'sales management', 'sales operations', 'marketing', 'direct sales', 'trends', 'b2b', 'marketing strategy', 'saas',
                                     'business development'],

                      'Sales & marketing': ['retail', 'manufacture', 'corporate', 'goodssale', 'consumer',
                                            'package', 'fmcg', 'account', 'management', 'lead generation', 'cold calling', 'customer service',
                                            'inside sales', 'sales', 'promotion'],

                      'Graphic': ['brand identity', 'editorial design', 'design', 'branding', 'logo design',
                                  'letterhead design', 'business card design', 'brand strategy', 'stationery design', 'graphic design',
                                  'exhibition graphic design'],

                      'Content skill': ['editing', 'creativity', 'content idea', 'problem solving', 'writer',
                                        'content thinker', 'copy editor', 'researchers', 'technology geek', 'public speaking', 'online marketing'],

                      'Graphical content': ['photographer', 'videographer', 'graphic artist', 'copywriter', 'search engine optimization',
                                            'seo', 'social media', 'page insight', 'gain audience'],

                      'Finanace': ['financial reporting', 'budgeting', 'forecasting', 'strong analytical thinking', 'financial planning',
                                   'payroll tax', 'accounting', 'productivity', 'reporting costs', 'balance sheet',
                                   'financial statements'],

                      'Health/Medical': ['abdominal surgery', 'laparoscopy', 'trauma surgery', 'adult intensive care',
                                         'pain management', 'cardiology', 'patient', 'surgery', 'hospital', 'healthcaret', 'doctor', 'medicine'],

                      'Language': ['english', 'malay', 'mandarin', 'bangla', 'hindi', 'tamil']
                      }


# Initialising the score counters for per areas of requirements
data_science = 0
code_proficiency = 0
experience_field = 0
management_skill = 0
data_analytics = 0
statistical_skill = 0
machine_learning = 0
Data_analyst = 0
Softwareskill = 0
Webskill = 0
PersonalSkill = 0
accounting_skill = 0
Sales_marketing = 0
Graphic_skill = 0
Content_skill = 0
Graphical_content = 0
Finanace_skill = 0
Health_Medical = 0
Languages = 0

# Declaration of empty list for storing the score
scores = []

# Getting actual scores for each area declared
for domain in Area_with_key_term.keys():

    if domain == 'Data science':
        for word in Area_with_key_term[domain]:
            if word in content:
                data_science += 1
        scores.append(data_science)

    elif domain == 'Programming':
        for word in Area_with_key_term[domain]:
            if word in content:
                code_proficiency += 1
        scores.append(code_proficiency)

    elif domain == 'Experience':
        for word in Area_with_key_term[domain]:
            if word in content:
                experience_field += 1
        scores.append(experience_field)

    elif domain == 'Data analytics':
        for word in Area_with_key_term[domain]:
            if word in content:
                data_analytics += 1
        scores.append(data_analytics)

    elif domain == 'Management skill':
        for word in Area_with_key_term[domain]:
            if word in content:
                management_skill += 1
        scores.append(management_skill)

    elif domain == 'Statistics':
        for word in Area_with_key_term[domain]:
            if word in content:
                statistical_skill += 1
        scores.append(statistical_skill)

    elif domain == 'Data analyst':
        for word in Area_with_key_term[domain]:
            if word in content:
                Data_analyst += 1
        scores.append(Data_analyst)

    elif domain == 'Software':
        for word in Area_with_key_term[domain]:
            if word in content:
                Softwareskill += 1
        scores.append(Softwareskill)

    elif domain == 'Web skill':
        for word in Area_with_key_term[domain]:
            if word in content:
                Webskill += 1
        scores.append(Webskill)

    elif domain == 'Personal Skill':
        for word in Area_with_key_term[domain]:
            if word in content:
                PersonalSkill += 1
        scores.append(PersonalSkill)

    elif domain == 'Acoounting':
        for word in Area_with_key_term[domain]:
            if word in content:
                accounting_skill += 1
        scores.append(accounting_skill)

    elif domain == 'Sales & marketing':
        for word in Area_with_key_term[domain]:
            if word in content:
                Sales_marketing += 1
        scores.append(Sales_marketing)

    elif domain == 'Graphic':
        for word in Area_with_key_term[domain]:
            if word in content:
                Graphic_skill += 1
        scores.append(Graphic_skill)

    elif domain == 'Content skill':
        for word in Area_with_key_term[domain]:
            if word in content:
                Content_skill += 1
        scores.append(Content_skill)

    elif domain == 'Graphical content':
        for word in Area_with_key_term[domain]:
            if word in content:
                Graphical_content += 1
        scores.append(Graphical_content)

    elif domain == 'Finanace':
        for word in Area_with_key_term[domain]:
            if word in content:
                Finanace_skill += 1
        scores.append(Finanace_skill)

    elif domain == 'Health/Medical':
        for word in Area_with_key_term[domain]:
            if word in content:
                Health_Medical += 1
        scores.append(Health_Medical)

    elif domain == 'Language':
        for word in Area_with_key_term[domain]:
            if word in content:
                Languages += 1
        scores.append(Languages)

    else:
        for word in Area_with_key_term[domain]:
            if word in content:
                machine_learning += 1
        scores.append(machine_learning)

# Data farme cretion for summarize/calculate the score
scored = pd.DataFrame(scores, index=Area_with_key_term.keys(), columns=[
    '   score earned']).sort_values(by='   score earned', ascending=False)

scored
print("  \nDomain/Area")
print("................")
print(scored)

# Summation of score earned per area/domain
print("\n\n\n................After score calculation per area, the summation of total score..................... ")
print("  \nDomain/Area")
print("................")
print(scored)
total_scored = sum(scores)
print(Fore.BLUE + "Summation Of Score Earned By Per Area:", total_scored)

# 1.data science
if total_scored >= 50 and PersonalSkill >= 2 and Languages >= 1 and statistical_skill >= 9:
    print(Fore.GREEN + "   Status: Resume Meets The Requirement, Suggest To Recruit as Junior Data Scientist.")

elif total_scored >= 40 and PersonalSkill >= 2 and Languages >= 1 and data_science >= 10:
    print(Fore.GREEN + "   Status: Resume Meets The Requirement, Suggest To Recruit as Junior Data Scientist.")


elif total_scored >= 60 and Languages >= 1 and data_analytics >= 8:
    print(Fore.GREEN + "   Status: Resume Meets The Requirement, Suggest To Recruit as Junior Data Scientist.")

# 2.data analyst
elif total_scored >= 30 and statistical_skill >= 2 and code_proficiency >= 3 and PersonalSkill >= 2 and Languages >= 1 and data_analytics >= 5 and Data_analyst >= 5:
    print(Fore.GREEN + "   Status: Resume Meets The Requirement, Suggest To Recruit as Data Analyst.")

# 3.software
elif total_scored >= 20 and experience_field >= 2 and PersonalSkill > 2 and Languages >= 1 and Softwareskill >= 10:
    print(Fore.GREEN + "   Status: Resume Meets The Requirement, Suggest To Recruit as a Software Engineer.")

# 4.web & graphic designer
elif total_scored >= 18 and PersonalSkill > 2 and Languages >= 1 and Graphic_skill >= 5 and Webskill >= 10:
    print(Fore.GREEN + "   Status: Resume Meets The Requirement, Suggest To Recruit as a Web & Graphic Designer.")

# 5.accountExecutive
elif total_scored >= 50 and PersonalSkill > 2 and Languages >= 1 and accounting_skill >= 10:
    print(Fore.GREEN + "   Status: Resume Meets The Requirement, Suggest To Recruit as an Account Executive.")

# 6.salesRepresentative
elif total_scored >= 20 and management_skill >= 2 and PersonalSkill > 2 and Languages >= 1 and Sales_marketing >= 10:
    print(Fore.GREEN + "   Status: Resume Meets The Requirement, Suggest To Recruit as a Sales Representative.")

# 7.contentCreator
elif total_scored >= 25 and PersonalSkill > 2 and Languages >= 1 and Content_skill >= 8 and Graphical_content >= 10:
    print(Fore.GREEN + "   Status: Resume Meets The Requirement, Suggest To Recruit as A Content Creator.")

# 8.seniorAccountant
elif total_scored >= 30 and management_skill >= 4 and PersonalSkill >= 2 and Languages >= 1 and Finanace_skill >= 10:
    print(Fore.GREEN + "   Status: Resume Meets The Requirement, Suggest To Recruit as a Senior Accountant.")

# 9.generalSurgeon
elif total_scored >= 20 and PersonalSkill >= 2 and Languages >= 1 and Health_Medical >= 10:
    print(Fore.GREEN + "   Status: Resume Meets The Requirement, Suggest To Recruit as a General Surgeon.")

else:
    print(Fore.RED + "   Status: Resume Not Meet any Requirements of the selected recruitment field, Rejected!")

# Visulization of result with resume decomposing by domain
pie = plt.figure(figsize=(11, 10))
plt.pie(scored['   score earned'], labels=scored.index, explode=(
    0.1, 0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), autopct='%1.0f%%', shadow=True, startangle=90)
plt.title('Applicants Resume Decomposition by Domain',
          bbox={'facecolor': '0.8', 'pad': 5})
plt.axis('equal')
plt.show()

# Save pie chart as a .png file
pie.savefig('resume_screening_results.png')
