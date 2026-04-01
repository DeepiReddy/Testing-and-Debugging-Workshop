import pytest
from leaderboard import Leaderboard


def test_add_player():
    lb = Leaderboard()
    lb.add_player("Alice")
    assert len(lb) == 1

def test_add_player_with_initial_score():
    lb = Leaderboard()
    lb.add_player("Alice", initial_score=500)
    assert lb.get_top_n(1) == [("Alice", 500)]

def test_add_player_negative_initial_score(): 
    lb = Leaderboard() 
    with pytest.raises(ValueError, match="Initial score cannot be negative"):
        lb.add_player("Alice", initial_score=-200)

def test_add_registered_player(): 
    lb = Leaderboard() 
    lb.add_player("Alice") 
    with pytest.raises(ValueError, match=f"Player 'Alice' is already registered"): 
        lb.add_player("Alice")

def test_record_match_updates_scores():
    lb = Leaderboard()
    lb.add_player("Alice", 100)
    lb.add_player("Bob", 100)
    lb.record_match("Alice", "Bob")
    assert lb.get_top_n(2) == [("Alice", 110), ("Bob", 90)]

def test_record_match_nonexistent_winner(): 
    lb = Leaderboard() 
    lb.add_player("Bob", 100) 
    with pytest.raises(KeyError, match=f"Player 'Alice' is not registered"): 
        lb.record_match("Alice", "Bob") 

def test_record_match_nonexistent_loser(): 
    lb = Leaderboard() 
    lb.add_player("Bob", 100) 
    with pytest.raises(KeyError, match=f"Player 'Alice' is not registered"): 
        lb.record_match("Bob", "Alice") 

def test_record_match_negative_points(): 
    lb = Leaderboard() 
    lb.add_player("Alice", 100) 
    lb.add_player("Bob", 100) 
    with pytest.raises(ValueError, match="Points must be positive"): 
        lb.record_match("Bob", "Alice", -300)

def test_get_rank():
    lb = Leaderboard()
    lb.add_player("Alice", 300)
    lb.add_player("Bob", 100)
    lb.add_player("Carol", 200)
    assert lb.get_rank("Alice") == 1
    assert lb.get_rank("Carol") == 2
    assert lb.get_rank("Bob") == 3

def test_get_percentile_normal():
    lb = Leaderboard()
    lb.add_player("Alice", 300)
    lb.add_player("Bob", 200)
    lb.add_player("Maria", 100)
    assert lb.get_percentile("Alice") == 66.67
    assert lb.get_percentile("Bob") == 33.33
    assert lb.get_percentile("Maria") == 0.0

def test_apply_bonus():
    lb = Leaderboard()
    lb.add_player("Alice", 100)
    lb.apply_bonus("Alice", 3)
    assert lb.get_top_n(1) == [("Alice", 300)]

def test_get_win_rate():
    lb = Leaderboard()
    lb.add_player("Alice")
    lb.add_player("Bob")
    lb.record_match("Bob", "Alice") 
    lb.record_match("Alice", "Bob")
    lb.record_match("Bob", "Alice")
    assert lb.get_win_rate("Bob") == 2 / 3
    assert lb.get_win_rate("Alice") == 1 / 3