def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Return True if ransomNote can be built from the letters in magazine,
    using each magazine letter at most once. Matching is case-sensitive.

    Approach:
      1. Count every character in the magazine in a hash table (dict).
      2. For each character in the note, spend one from that table.
      3. If a character is missing or its count is 0, return False early.

    Time:  O(m + n), because dict lookups and updates are O(1) on average.
    Space: O(k), where k is the number of distinct characters in magazine.
    """
    # A note longer than the magazine can never be built
    if len(ransomNote) > len(magazine):
        return False

    # Hash table of available letters: {character: how many are left}
    available = {}
    for char in magazine:
        available[char] = available.get(char, 0) + 1

    for char in ransomNote:
        # Missing or already used up: the note can't be built
        if available.get(char, 0) == 0:
            return False
        # Use one copy of this letter
        available[char] -= 1

    return True
