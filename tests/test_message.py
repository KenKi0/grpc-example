import pytest

import src.message.message_pb2 as message_pb2


def test_equals():
    message1 = message_pb2.Message(str="1")
    message2 = message_pb2.Message(str="1")
    assert message1 == message2


def test_not_equals():
    message1 = message_pb2.Message(str="1")
    message2 = message_pb2.Message(str="2")
    assert message1 != message2


def test_default():
    message = message_pb2.Message()
    assert message.str == ""
    assert message.int == 0
    assert message.bool is False
    assert message.inner_model == message_pb2.InnerModel()
    assert message.repeated_str == []


def test_init():
    message = message_pb2.Message(
        str="test_str",
        int=42,
        bool=True,
        inner_model=message_pb2.InnerModel(value="test_value"),
        repeated_str=["1", "2", "3"],
    )
    assert message.str == "test_str"
    assert message.int == 42
    assert message.bool is True
    assert message.inner_model == message_pb2.InnerModel(value="test_value")
    assert message.repeated_str == ["1", "2", "3"]


def test_fields():
    message = message_pb2.Message(str="test_str")
    message.str = "new_test_str"
    assert message.str == "new_test_str"


def test_incorrect_type():
    with pytest.raises(TypeError) as exc_info:
        _ = message_pb2.Message(str=1)
    assert str(exc_info.value) == "1 has type int, but expected one of: bytes, unicode"

    message = message_pb2.Message()
    with pytest.raises(TypeError) as exc_info:
        message.str = 1
    assert str(exc_info.value) == "1 has type int, but expected one of: bytes, unicode"


def test_no_such_field():
    request = message_pb2.Message()
    with pytest.raises(AttributeError) as exc_info:
        request.no_such_field = "test_str"
    assert str(exc_info.value) == "'Message' object has no attribute 'no_such_field'"


def test_str():
    message = message_pb2.Message(
        str="test_str",
        int=42,
        bool=True,
        inner_model=message_pb2.InnerModel(value="test_value"),
        repeated_str=["1", "2", "3"],
    )
    assert str(message) == (
        'str: "test_str"\n'
        "int: 42\n"
        "bool: true\n"
        "inner_model {\n"
        '  value: "test_value"\n'
        "}\n"
        'repeated_str: "1"\n'
        'repeated_str: "2"\n'
        'repeated_str: "3"\n'
    )


def test_copy():
    message = message_pb2.Message(
        str="test_str",
        int=42,
        bool=True,
        inner_model=message_pb2.InnerModel(value="test_value"),
        repeated_str=["1", "2", "3"],
    )
    message2 = message_pb2.Message()
    message2.CopyFrom(message)
    assert message == message2
    message.str = "new_value"
    assert message != message2


def test_clear():
    message = message_pb2.Message(str="test_str")
    message.int = 42
    message.Clear()
    assert message.str == ""
    assert message.int == 0


def test_serialize():
    message = message_pb2.Message(str="test_str")
    assert message.SerializeToString() == b"\n\x08test_str"


def test_deserialize():
    # message = message_pb2.Message(
    #     str="1",
    #     int=1,
    #     bool=True,
    #     inner_model=message_pb2.InnerModel(value="1"),
    #     repeated_str=["1", "2", "3"]
    # )
    message = message_pb2.Message()
    message.ParseFromString(b'\n\x011\x10\x01\x18\x01"\x03\n\x011*\x011*\x012*\x013')
    assert message.str == "1"
    assert message.int == 1
    assert message.bool is True
    assert message.inner_model == message_pb2.InnerModel(value="1")
    assert message.repeated_str == ["1", "2", "3"]
