from task import execution

def test():
    assert execution(1) == 1
    assert execution(10) == 1
    assert execution(3) == 1
    assert execution(999) == 1
    assert execution(-5) == 1
    assert execution(0) == 1

test()