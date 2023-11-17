import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = r"C:\Users\micha\OneDrive\Pulpit\studia\semestr 7\pytonProjectlab3\UCI_Credit_Card.csv"
credit_data = pd.read_csv(file_path)

# Removing duplicate rows from the DataFrame
credit_data_cleaned = credit_data.drop_duplicates()

# Check if duplicates were found and removed
if credit_data.shape[0] == credit_data_cleaned.shape[0]:
    print("No duplicates were found in the dataset.")
else:
    print(f"Duplicates removed. The original dataset had {credit_data.shape[0]} rows, "
          f"and the cleaned dataset has {credit_data_cleaned.shape[0]} rows.")

# Calculating the correlation between Age and Credit Limit
correlation_age_limit_bal = credit_data_cleaned[['AGE', 'LIMIT_BAL']].corr()
print("\nCorrelation between Age and Credit Limit:")
print(correlation_age_limit_bal)

# Adding a column that is the sum of all transactions and naming it 'bill_amt_X'
bill_columns = ['BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6']
credit_data_cleaned['bill_amt_X'] = credit_data_cleaned[bill_columns].sum(axis=1)

# Setting pandas options to display all columns
#pd.set_option('display.max_columns', None)

# Displaying the first few rows to confirm the addition of the new column
print("\nFirst few rows of the dataset with the new 'bill_amt_X' column:")
print(credit_data_cleaned.head())

# Finding the 10 oldest customers
oldest_customers = credit_data_cleaned.sort_values(by='AGE', ascending=False).head(10)

# Mapping education numbers to names for readability
education_mapping = {1: 'Graduate School', 2: 'University', 3: 'High School', 4: 'Others'}
oldest_customers['EDUCATION'] = oldest_customers['EDUCATION'].map(education_mapping)

# Selecting only the specified columns for the 10 oldest customers
selected_columns = ['LIMIT_BAL', 'AGE', 'EDUCATION', 'bill_amt_X']
oldest_customers_table = oldest_customers[selected_columns]

# Displaying the first few rows to confirm the addition of the new column
print("\nThe 10 oldest customers")
print(oldest_customers_table)

# Plotting histograms and a scatter plot
plt.figure(figsize=(12, 6))

# Histogram of Credit Limit
plt.subplot(131)
plt.hist(credit_data_cleaned['LIMIT_BAL'], bins=20, color='skyblue', edgecolor='black')
plt.title('Credit Limit Histogram')
plt.xlabel('Credit Limit')
plt.ylabel('Popoluation')

# Histogram of Age
plt.subplot(132)
plt.hist(credit_data_cleaned['AGE'], bins=20, color='lightcoral', edgecolor='black')
plt.title('Age Histogram')
plt.xlabel('Age')
plt.ylabel('Popoluation')

# Scatter plot of Credit Limit vs. Age
plt.subplot(133)
plt.scatter(credit_data_cleaned['AGE'], credit_data_cleaned['LIMIT_BAL'], alpha=0.5, color='orange')
plt.title('Credit Limit vs. Age')
plt.xlabel('Age')
plt.ylabel('Credit Limit')

# Adjusting subplot spacing
plt.tight_layout()

# Display the plots
plt.show()
