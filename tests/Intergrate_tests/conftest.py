import pytest
import dbcsv
import time
import pandas as pd
import os
    
def pytest_itemcollected(item):
    """Show docstring while running pytest"""
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))

@pytest.fixture(scope="module")
def mock_path_file():
    """A mock path file"""
    return "./db_test/"

@pytest.fixture(scope="session")
def mock_data_file(mock_path_file):
    """
        A mock data file to test commit
    """
    if os.path.exists(mock_path_file):
        os.remove(mock_path_file)
    else:
        df = pd.DataFrame(data=[(1, "abc", 20), (2, "def", 30)], columns=["id", "col1", "col2"])
        df.to_csv(mock_path_file)
    yield
    os.remove(mock_path_file)
    
@pytest.fixture(scope="module")
def mock_insert_data_list():
    """
        A mock lit of data to insert
    """
    return [()]

@pytest.fixture(scope="module")
def mock_data_id():
    """
        Mock data id
    """
    return 1

@pytest.fixture(scope="module")
def mock_insert_data(mock_data_id):
    """
        Single mock data to insert
    """
    #id, col1, col2
    return (mock_data_id, "", "")

@pytest.fixture(scope="function")
def dbapi2_connections(mock_path_file):
    try:
        conn = dbcsv.connect(mock_path_file)
        conn2 = dbcsv.connect(mock_path_file)
        yield conn, conn2
    except Exception as e:
        print(e)
    finally:
        conn.close()
        
@pytest.fixture(autouse=True)
def log_execution_time():
    start_time = time.time()
    yield 
    delta = time.time() - start_time
    print("\n test duration: {:0.3} seconds".format(delta))

@pytest.fixture(autouse=True)
def no_request(monkeypatch):
    monkeypatch.delattr("requests.sessions.Session.request")

@pytest.fixture(scope="function")
def mock_excecute(monkeypatch):
    
    # Clean this with class instead of directly using mock_method
    def mock_reponse():
        pass
    # I want to mock a json return depend on function call
    monkeypatch.setattr()