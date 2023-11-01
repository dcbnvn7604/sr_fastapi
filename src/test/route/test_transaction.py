from db.model import User


def test_transaction_single(client, init_db, db):
    response = client.get('/transaction/single')
    assert response.status_code == 200
    count = db.query(User).count()
    assert count == 1
    db.commit()


def test_transaction_multiple(client, init_db, db):
    try:
        response = client.get('/transaction/multiple')
    except Exception as e:
        if e.args[0] != 'fail_multiple':
            raise e
    count = db.query(User).count()
    assert count == 0
    db.commit()
