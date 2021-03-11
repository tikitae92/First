## skills search
##search entered skill and print results

skills = '''Technical Skills:
Languages: Python, JAVA, SQL
Analytical: SAS, SPSS, STATA
Database: MS Sql Server, Orale, MySql'''

searchSkill=input("Enter skill: ")

skills=skills.lower()
searchSkill=searchSkill.lower()

if searchSkill in skills:
   print("Skill found in applicant file")
else:
   print("Skill not found")
   

















