def test_try_except(cond):
    try:
        assert cond
    except AssertionError:
        print('error')
    finally:
        print('ok')


if __name__ == "__main__":
    test_try_except(False)
