# Ransom Note (Hash Table Lab)

`can_construct(ransomNote, magazine)` returns `True` if the note can be
built from the magazine's letters, using each letter once. It uses a
dictionary to count available characters.

## Run
python3 test_ransom_note.py

## Notes
- Case-sensitive: "a" and "A" are different characters.
- Spaces and punctuation count as characters.
- Time O(m + n), space O(k).