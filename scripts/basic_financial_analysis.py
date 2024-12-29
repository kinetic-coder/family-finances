import csv
from datetime import datetime
from Entities.BankAccountTransaction import BankAccountTransaction
import mysql.connector
            
# Application work...
bank_account_statement_file = "/home/oliver/dev/family-finances/input/bank_statements/Monzo Data Export - CSV (Saturday, December 28th, 2024).csv"
budget = "/home/oliver/dev/family-finances/input/budgets/2024-12-28.csv"
db_connection_string = "mysql+pymysql://root:DevelopmentPhase@localhost/family-finances"

bank_transactions = BankAccountTransaction.from_csv(bank_account_statement_file)

# Create a new database connection
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DevelopmentPhase",
    database="family-finances"
)

BankAccountTransaction.save_to_db(db_connection, bank_transactions)

print(bank_transactions)