
"""Blood donation registration and blood-group stock management."""

import os
import re
import subprocess
import tempfile
from datetime import date, timedelta

OFFICER_PASSWORD = os.environ.get("BLOOD_BANK_OFFICER_PASSWORD")
donors = []
stock = {
    "A+": 0, "A-": 0, "B+": 0, "B-": 0,
    "O+": 0, "O-": 0, "AB+": 0, "AB-": 0,
}
COMPATIBLE = {
    "A+": ["A+", "A-", "O+", "O-"],
    "A-": ["A-", "O-"],
    "B+": ["B+", "B-", "O+", "O-"],
    "B-": ["B-", "O-"],
    "O+": ["O+", "O-"],
    "O-": ["O-"],
    "AB+": list(stock),
    "AB-": ["AB-", "A-", "B-", "O-"],
}


def register_donor(
    donor_name, blood_group, age, last_donation=None, notes=None
):
    """Register a donor if their age is within the allowed range."""
    if blood_group not in stock:
        raise ValueError("Unknown blood group")
    if notes is None:
        notes = []
    if age < 18 or age > 65:
        notes.append(f"{donor_name} is not eligible because of age")
        return False
    donors.append({
        "name": donor_name,
        "group": blood_group,
        "last": last_donation,
    })
    return True


def can_donate(donor):
    """Check whether at least 90 days have passed since donation."""
    if donor["last"] is None:
        return True
    return date.today() - donor["last"] >= timedelta(days=90)


def record_donation(donor_name, units=1):
    """Record a donation for an eligible donor."""
    if not isinstance(units, int) or isinstance(units, bool) or units <= 0:
        raise ValueError("units must be a positive integer")
    for donor in donors:
        if donor["name"] == donor_name and can_donate(donor):
            stock[donor["group"]] += units
            donor["last"] = date.today()
            return True
    return False


def units_for(patient_group):
    """Calculate compatible red-cell units available for a patient."""
    if patient_group not in COMPATIBLE:
        return 0
    return sum(stock[group] for group in COMPATIBLE[patient_group])


def is_universal(blood_group):
    """Check for universal red-cell donor O- or recipient AB+."""
    return blood_group in {"O-", "AB+"}


def low_stock(threshold=2):
    """List blood groups with stock below the threshold."""
    return [group for group, units in stock.items() if units < threshold]


def donor_sheet_path():
    """Create a secure temporary CSV file and return its path."""
    with tempfile.NamedTemporaryFile(
        suffix=".csv", prefix="blood-donors-", delete=False
    ) as temp_file:
        return temp_file.name


def notify_donors(phone_list):
    """Run the SMS utility without invoking a shell."""
    pattern = re.compile(r"\+?[0-9]{7,15}")
    if not all(pattern.fullmatch(phone) for phone in phone_list):
        raise ValueError("Invalid phone number format")
    subprocess.run(["send-sms", *phone_list], check=True, shell=False)


def main():
    """Run the demonstration."""
    register_donor("Arjun", "O+", 25)
    register_donor("Priya", "A+", 30, date.today() - timedelta(days=30))
    register_donor("Old Donor", "B+", 70)
    register_donor("Farah", "O-", 41)
    record_donation("Arjun", 2)
    record_donation("Priya")
    record_donation("Farah")
    print("Stock:", stock)
    print("Units for an A+ patient:", units_for("A+"))
    print("Units for a Z+ patient:", units_for("Z+"))
    print("Is O- universal?", is_universal("O-"))
    print("Low stock groups:", low_stock())  # below 2 units
    eligible = [
        donor["name"] for donor in donors if can_donate(donor)
    ]
    print("Donors eligible today:", eligible)


if __name__ == "__main__":
    main()
