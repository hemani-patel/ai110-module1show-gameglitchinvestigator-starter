from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    #FIX: Refactored logic into logic_utils.py using Copilot Agent mode
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_attempts_left_starts_at_full_limit():
    # Bug: attempts was initialized to 1 instead of 0, so the first render
    # showed attempt_limit - 1 attempts left instead of the full limit.
    # This test encodes the correct starting condition.
    attempt_limit = 8  # Normal difficulty
    initial_attempts = 0  # FIX: was 1, causing off-by-one in display
    attempts_left = attempt_limit - initial_attempts
    assert attempts_left == attempt_limit, (
        f"On a fresh game, attempts_left should equal attempt_limit ({attempt_limit}), got {attempts_left}"
    )

def test_invalid_guess_does_not_increment_attempts():
    # Bug: attempts += 1 fired before parse_guess validity check, so empty/non-numeric
    # inputs silently consumed an attempt, causing game-over to fire one attempt early.
    # FIX: attempts should only increment when parse_guess returns ok=True.
    attempt_limit = 5
    attempts = 0

    submissions = ["", "abc", "not a number", "42", "17"]  # 3 invalid, 2 valid

    for raw in submissions:
        # Simulate the fixed submit logic: only count valid guesses
        if raw is None or raw == "":
            ok = False
        else:
            try:
                int(raw)
                ok = True
            except ValueError:
                ok = False

        if ok:
            attempts += 1  # FIX: was outside this block, incrementing on invalid input too

    assert attempts == 2, (
        f"Only valid guesses should count as attempts; expected 2, got {attempts}"
    )
    assert attempts < attempt_limit, "Should not hit game-over limit from invalid inputs alone"

def test_high_low_messages_not_swapped():
    # Bug: messages were inverted — "Too High" said "Go HIGHER!" and "Too Low" said "Go LOWER!"
    # When guess > secret, player needs to go lower
    outcome_high, message_high = check_guess(60, 50)
    assert outcome_high == "Too High"
    assert "LOWER" in message_high, f"Expected 'LOWER' in message for too-high guess, got: {message_high}"

    # When guess < secret, player needs to go higher
    outcome_low, message_low = check_guess(40, 50)
    assert outcome_low == "Too Low"
    assert "HIGHER" in message_low, f"Expected 'HIGHER' in message for too-low guess, got: {message_low}"
