import os
import gspread
from typing import List
from django.conf import settings

def initialize_gspread() -> gspread.client.Client:
    """
    Initialize a gspread client with given credentials
    """
    return gspread.service_account_from_dict(get_credentials())

def get_credentials() -> dict:
    """
    Return gspread credentials
    """
    return {
        "type": os.getenv("TYPE"),
        "project_id": os.getenv("PROJECT_ID"),
        "private_key_id": os.getenv("PRIVATE_KEY_ID"),
        "private_key": os.getenv("PRIVATE_KEY"),
        "client_email": os.getenv("CLIENT_EMAIL"),
        "client_id": os.getenv("CLIENT_ID"),
        "auth_uri": os.getenv("AUTH_URI"),
        "token_uri": os.getenv("TOKEN_URI"),
        "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
        "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL"),
        "universe_domain": os.getenv("UNIVERSE_DOMAIN")
    }

def get_all_rows() -> List[dict]:
    """
    Fetches all rows from a given Google Sheet worksheet.
    """
    sh = settings.GSPREAD_CLIENT.open("inventory")
    # worksheet = sh.worksheet["Masterlist"]
    worksheet = sh.get_worksheet(1)
    return worksheet.get_all_records()