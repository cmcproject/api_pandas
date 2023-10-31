from datetime import date, datetime


def get_age_from_dob(dob: str) -> int:
    """
    Get age from date of birth
    :dob: Date of birth

    :return: Age
    """
    born = datetime.strptime(dob, "%Y-%m-%d").date()
    today = date.today()

    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
