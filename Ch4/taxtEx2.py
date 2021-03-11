#asked user information

m_status=input("Enter marital status(S/M): ")
SINGLE="S"
MARRIED="M"
m_status=m_status.upper()
while m_status!=SINGLE and m_status!=MARRIED:
    m_status=input("Enter marital status (S/M): ")
    m_status=m_status.upper()
    
income=float(input("Enter income: "))
#changed entry to upper to match variable case
while income<0:
    print("income cannot be negative")
    income=float(input("Enter income: "))

#defined variables

S_LIMIT=32000
M_LIMIT=64000
TAX_RATE_SL=.1
TAX_RATE_ML=.1
TAX_RATE_SU=.25
TAX_RATE_MU=.25
FIXED_AMT_SU=3200
FIXED_AMT_MU=6400

if m_status==SINGLE:
    #check limit and calculate tax
    if income<=S_LIMIT and income>=0:
        tax=income*TAX_RATE_SL
        print("Tax is $%.2f" %tax)
    elif income>S_LIMIT:
        tax=FIXED_AMT_SU+((income-S_LIMIT)*TAX_RATE_SU)
        print("Tax is $%.2f" %tax)
    else:
        print("Invalid entry")
elif m_status==MARRIED:
    #check limit and calculate tax
    if income<=M_LIMIT and income>=0:
        tax=income*TAX_RATE_ML
        print("Tax is $%.2f" %tax)
        
    elif income>M_LIMIT:
        tax=FIXED_AMT_MU+((income-M_LIMIT)*TAX_RATE_MU)
        print("Tax is $%.2f" %tax)
    else:
        print("Invalid entry")

    






















