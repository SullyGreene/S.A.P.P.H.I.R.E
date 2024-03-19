# services/notations/taking_notes.py

import datetime
import json
import os

class NoteTakingService:
    def __init__(self, storage_file='notes.json'):
        self.storage_file = storage_file
        self.notes = self.load_notes()

    def load_notes(self):
        """Load notes from a JSON file."""
        if not os.path.exists(self.storage_file):
            return []
        with open(self.storage_file, 'r') as file:
            return json.load(file)

    def save_notes(self):
        """Save notes to a JSON file."""
        with open(self.storage_file, 'w') as file:
            json.dump(self.notes, file, indent=4)

    def add_note(self, content):
        """Add a new note."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note = {'timestamp': timestamp, 'content': content}
        self.notes.append(note)
        self.save_notes()
        return "Note added successfully."

    def list_notes(self):
        """List all notes."""
        if not self.notes:
            return "No notes found."
        return '\n'.join([f"{note['timestamp']}: {note['content']}" for note in self.notes])

    def find_notes(self, query):
        """Find notes containing a specific query."""
        matched_notes = [note for note in self.notes if query.lower() in note['content'].lower()]
        if not matched_notes:
            return "No matching notes found."
        return '\n'.join([f"{note['timestamp']}: {note['content']}" for note in matched_notes])
