"""Contact and address book demonstration with safer persistence."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path
from typing import Any

ContactRecord = dict[str, str]
ContactBook = dict[str, ContactRecord]

PHONE_PATTERN = re.compile(r"[0-9]{10}")
CONTACTS: ContactBook = {}
CONTACT_FIELDS = {"phone", "email", "city"}


def add_contact(
    full_name: str,
    phone: str,
    email: str = "",
    city: str = "Unknown",
) -> bool:
    """Add a contact when its phone number contains exactly ten digits."""
    if not PHONE_PATTERN.fullmatch(phone):
        print("Invalid phone number for", full_name)
        return False
    CONTACTS[full_name] = {"phone": phone, "email": email, "city": city}
    return True


def contact_id(full_name: str) -> str:
    """Return a stable SHA-256 identifier instead of using weak MD5."""
    return hashlib.sha256(full_name.encode("utf-8")).hexdigest()


def search_contacts(text: str) -> list[str]:
    """Find contacts by case-insensitive name or phone-number substring."""
    query = text.casefold()
    return [
        name
        for name, info in CONTACTS.items()
        if query in name.casefold() or text in info["phone"]
    ]


def update_city(full_name: str, city: str) -> bool:
    """Update a contact city, returning False when the contact is absent."""
    contact = CONTACTS.get(full_name)
    if contact is None:
        print("No contact named", full_name)
        return False
    contact["city"] = city
    return True


def contacts_by_city() -> dict[str, list[str]]:
    """Group contact names by their current city."""
    grouped: dict[str, list[str]] = {}
    for name, info in CONTACTS.items():
        grouped.setdefault(info["city"], []).append(name)
    return grouped


def print_directory() -> None:
    """Print contacts in alphabetical order with a one-based row number."""
    for index, name in enumerate(sorted(CONTACTS), start=1):
        print(index, name, CONTACTS[name]["phone"])


def export_csv(file_name: str | Path = "contacts.csv") -> None:
    """Export contacts to a UTF-8 CSV file."""
    with Path(file_name).open(
        "w", newline="", encoding="utf-8"
    ) as file_handle:
        writer = csv.writer(file_handle)
        for name, info in CONTACTS.items():
            writer.writerow(
                [name, info["phone"], info["email"], info["city"]]
            )


def backup_book(file_name: str | Path = "contacts.bak") -> None:
    """Write a JSON backup; JSON avoids executable pickle deserialization."""
    with Path(file_name).open("w", encoding="utf-8") as file_handle:
        json.dump(CONTACTS, file_handle, ensure_ascii=False, indent=2)


def _validate_contacts(data: Any) -> ContactBook:
    """Validate decoded JSON before treating it as contact records."""
    if not isinstance(data, dict):
        raise ValueError(
            "Backup format is invalid: expected a contact object."
        )

    validated: ContactBook = {}
    for name, record in data.items():
        if not isinstance(name, str) or not isinstance(record, dict):
            raise ValueError("Backup format is invalid: malformed contact.")
        if set(record) != CONTACT_FIELDS or not all(
            isinstance(record[field], str) for field in CONTACT_FIELDS
        ):
            raise ValueError(
                "Backup format is invalid: contact fields are invalid."
            )
        if not PHONE_PATTERN.fullmatch(record["phone"]):
            raise ValueError("Backup format is invalid: phone number is invalid.")
        validated[name] = {
            "phone": record["phone"],
            "email": record["email"],
            "city": record["city"],
        }
    return validated


def restore_book(file_name: str | Path = "contacts.bak") -> ContactBook:
    """Read and validate a JSON backup without executing serialized objects."""
    try:
        with Path(file_name).open("r", encoding="utf-8") as file_handle:
            data: Any = json.load(file_handle)
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise ValueError("Backup file is not valid UTF-8 JSON.") from exc
    return _validate_contacts(data)


def main() -> None:
    """Run the sample workflow used by the original assignment script."""
    CONTACTS.clear()
    add_contact("Neha Sharma", "9876543210", "neha@example.com", "Bengaluru")
    add_contact("Rahul Verma", "9123456780", "rahul@example.com", "Mysuru")
    add_contact("Test User", "12345")
    add_contact("Kavya Nair", "9988776655", city="Bengaluru")
    update_city("Rahul Verma", "Chennai")
    update_city("Nobody", "Delhi")
    print_directory()
    print("Search 'ra':", search_contacts("ra"))
    print("By city:", contacts_by_city())
    print("Id for Neha:", contact_id("Neha Sharma"))
    export_csv()
    backup_book()
    restored = restore_book()
    print("Contacts restored:", len(restored), "| first:", sorted(restored)[0])
    print(
        "Restored contacts match the in-memory address book:",
        restored == CONTACTS,
    )


if __name__ == "__main__":
    main()
