from augmenty.keyboard import Keyboard


def test_Keyboard():
    kb = Keyboard(keyboard_array="da_qwerty.v1")

    assert kb.coordinate("q") == (1, 0)
    assert kb.is_shifted("q") is False
    assert kb.euclidian_distance("q", "a") <= 1
    assert len(set(kb.all_keys())) > 28 * 2
    assert "w" in kb.get_neighboors("q")
    kb.create_distance_dict()
