"""Automated tests for the address book exercise."""

import csv
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import address_book


class AddressBookTests(unittest.TestCase):
    """Test input checks, search, update behavior, and file persistence."""

    def setUp(self) -> None:
        address_book.CONTACTS.clear()

    def test_add_valid_contact(self) -> None:
        self.assertTrue(
            address_book.add_contact(
                "Aarya Prasad", "9876543210", "aarya@example.com", "Bengaluru"
            )
        )
        self.assertEqual(
            address_book.CONTACTS["Aarya Prasad"]["phone"], "9876543210"
        )

    def test_rejects_invalid_phone(self) -> None:
        self.assertFalse(address_book.add_contact("Test User", "12345"))
        self.assertNotIn("Test User", address_book.CONTACTS)

    def test_search_matches_case_insensitive_name_and_phone(self) -> None:
        address_book.add_contact("Neha Sharma", "9876543210")
        self.assertEqual(address_book.search_contacts("NEHA"), ["Neha Sharma"])
        self.assertEqual(address_book.search_contacts("4321"), ["Neha Sharma"])

    def test_update_city_absent_contact_returns_false(self) -> None:
        with patch("builtins.print"):
            self.assertFalse(address_book.update_city("Missing", "Delhi"))

    def test_contacts_are_grouped_by_city(self) -> None:
        address_book.add_contact("Neha Sharma", "9876543210", city="Bengaluru")
        address_book.add_contact("Kavya Nair", "9988776655", city="Bengaluru")
        self.assertEqual(
            address_book.contacts_by_city()["Bengaluru"],
            ["Neha Sharma", "Kavya Nair"],
        )

    def test_contact_id_is_stable_and_six_characters(self) -> None:
        identifier = address_book.contact_id("Neha Sharma")
        self.assertEqual(len(identifier), 64)
        self.assertEqual(identifier, address_book.contact_id("Neha Sharma"))

    def test_json_backup_restore_round_trip(self) -> None:
        address_book.add_contact("Neha Sharma", "9876543210")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "contacts.bak"
            address_book.backup_book(path)
            restored = address_book.restore_book(path)
        self.assertEqual(restored, address_book.CONTACTS)

    def test_restore_rejects_malformed_json(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "contacts.bak"
            path.write_text("{bad json", encoding="utf-8")
            with self.assertRaises(ValueError):
                address_book.restore_book(path)

    def test_restore_rejects_unexpected_shape(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "contacts.bak"
            path.write_text(
                json.dumps(["not a contact mapping"]), encoding="utf-8"
            )
            with self.assertRaises(ValueError):
                address_book.restore_book(path)

    def test_restore_rejects_invalid_phone_number(self) -> None:
        invalid_data = {
            "Neha Sharma": {
                "phone": "12345",
                "email": "neha@example.com",
                "city": "Bengaluru",
            }
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "contacts.bak"
            path.write_text(json.dumps(invalid_data), encoding="utf-8")
            with self.assertRaises(ValueError):
                address_book.restore_book(path)

    def test_csv_export_writes_contact_fields(self) -> None:
        address_book.add_contact(
            "Neha Sharma", "9876543210", "neha@example.com"
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "contacts.csv"
            address_book.export_csv(path)
            with path.open("r", newline="", encoding="utf-8") as file_handle:
                rows = list(csv.reader(file_handle))
        self.assertEqual(
            rows,
            [["Neha Sharma", "9876543210", "neha@example.com", "Unknown"]],
        )


if __name__ == "__main__":
    unittest.main()
