from unittest.mock import MagicMock, patch

from src.import_csv_xlsx import get_transactions_csv, get_transactions_xlsx


@patch("os.path.isfile")
def test_import_csv(mock_isfile):
    mock_isfile.return_value = False
    assert get_transactions_csv("aaa.csv") == []


@patch("os.path.isfile")
def test_import_xls(mock_isfile):
    mock_isfile.return_value = False
    assert get_transactions_csv("aaa.xls") == []


@patch("os.path.isfile", return_value=True)
@patch("pandas.read_excel", side_effect=Exception("Ошибка чтения Excel"))
def test_get_transactions_xlsx_exception(mock_read_excel, mock_isfile):
    result = get_transactions_xlsx("dummy.xlsx")
    assert result == []
    mock_isfile.assert_called_once_with("dummy.xlsx")
    mock_read_excel.assert_called_once_with("dummy.xlsx")


@patch("os.path.isfile", return_value=True)
@patch("pandas.read_csv", side_effect=Exception("Ошибка чтения csv"))
def test_get_transactions_csv_exception(mock_read_csv, mock_isfile):
    result = get_transactions_csv("dummy.csv")
    assert result == []
    mock_isfile.assert_called_once_with("dummy.csv")
    mock_read_csv.assert_called_once_with("dummy.csv")


@patch("os.path.isfile", return_value=True)
@patch("pandas.read_csv")
def test_get_transactions_csv_with_mock_data(mock_read_csv, mock_isfile):
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"Id": 1, "Name": "Alex", "Amount": 20}, {"Id": 2, "Name": "Bill", "Amount": 30}]
    mock_read_csv.return_value = mock_df
    result = get_transactions_csv("dummy.csv")
    assert result == [{"Id": 1, "Name": "Alex", "Amount": 20}, {"Id": 2, "Name": "Bill", "Amount": 30}]

    mock_isfile.assert_called_once_with("dummy.csv")
    mock_read_csv.assert_called_once_with("dummy.csv")
    mock_df.to_dict.assert_called_once_with(orient="records")


@patch("os.path.isfile", return_value=True)
@patch("pandas.read_excel")
def test_get_transactions_xlsx_with_mock_data(mock_read_xlsx, mock_isfile):
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"Id": 1, "Name": "Alex", "Amount": 20}, {"Id": 2, "Name": "Bill", "Amount": 30}]
    mock_read_xlsx.return_value = mock_df
    result = get_transactions_xlsx("dummy.xls")
    assert result == [{"Id": 1, "Name": "Alex", "Amount": 20}, {"Id": 2, "Name": "Bill", "Amount": 30}]

    mock_isfile.assert_called_once_with("dummy.xls")
    mock_read_xlsx.assert_called_once_with("dummy.xls")
    mock_df.to_dict.assert_called_once_with(orient="records")
