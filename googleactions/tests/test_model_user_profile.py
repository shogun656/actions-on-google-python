from googleactions import UserProfile


def test_init():
    user_profile = UserProfile(display_name='Bob S.', given_name='Bob', family_name='Smith')
    assert len(vars(user_profile)) == 3
    assert user_profile.display_name == 'Bob S.'
    assert user_profile.given_name == 'Bob'
    assert user_profile.family_name == 'Smith'
