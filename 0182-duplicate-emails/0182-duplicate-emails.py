import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    duplicates = (person.groupby("email").size().reset_index(name="count").query("count > 1")[["email"]])
    duplicates.rename(columns={"email": "Email"}, inplace=True)
    return duplicates