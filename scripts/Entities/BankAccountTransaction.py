import csv
from datetime import datetime

class BankAccountTransaction:
    def __init__(self, date, transaction_type, amount, currency, description, name):
        self.date = datetime.strptime(date, '%d/%m/%Y')
        self.transaction_type = transaction_type
        self.amount = float(amount)
        self.currency = currency
        self.description = description
        self.name = name

    def __repr__(self):
        return f"BankAccountTransaction(date={self.date}, transaction_type={self.transaction_type}, amount={self.amount}, currency={self.currency}, description={self.description})"

    @classmethod
    def from_csv(self, filename):
        
        transactions = []
        
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                transaction = BankAccountTransaction(
                    date=row['Date'],
                    transaction_type=row['Type'],
                    amount=row['Amount'],
                    currency=row['Currency'],
                    description=row['Description'],
                    name=row['Name']
                )
                transactions.append(transaction)
                
        return transactions
    
    @classmethod
    def save_to_db(self, db_connection, transactions):
        cursor = db_connection.cursor()
        for transaction in transactions:
            cursor.execute("""
                INSERT INTO Transaction (date, reference, amount)
                VALUES (%s, %s, %s)
            """, (
                transaction.date.strftime('%Y-%m-%d'),
                transaction.description,
                transaction.amount               
                
            ))
        db_connection.commit()
        cursor.close()