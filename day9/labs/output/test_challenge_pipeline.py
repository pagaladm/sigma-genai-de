import datetime

def test_filter_recent_transactions():
    def filter_recent_transactions(transactions, cutoff):
        return [t for t in transactions if t['date'] > cutoff]
    
    cutoff = datetime.datetime(2023, 1, 1)
    transactions = [
        {'date': datetime.datetime(2023, 1, 1), 'amount': 100},  # cutoff
        {'date': datetime.datetime(2023, 1, 2), 'amount': 200}  # recent
    ]
    result = filter_recent_transactions(transactions, cutoff)
    assert len(result) == 1
    assert result[0]['date'] > cutoff

def test_apply_silver_rules_filter_none_transaction_id():
    def apply_silver_rules(transactions):
        return [t for t in transactions if t.get('transaction_id') is not None]
    
    transactions = [
        {'transaction_id': None, 'amount': 100},
        {'transaction_id': 1, 'amount': 200}
    ]
    result = apply_silver_rules(transactions)
    assert len(result) == 1
    assert result[0]['transaction_id'] == 1

def test_apply_silver_rules_filter_negative_amount():
    def apply_silver_rules(transactions):
        return [t for t in transactions if t['amount'] >= 0]
    
    transactions = [
        {'transaction_id': 1, 'amount': -100},
        {'transaction_id': 2, 'amount': 200}
    ]
    result = apply_silver_rules(transactions)
    assert len(result) == 1
    assert result[0]['amount'] == 200