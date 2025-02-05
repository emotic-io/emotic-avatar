from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EmotionState(_message.Message):
    __slots__ = ("timestamp", "valence", "arousal", "dominance", "emotions")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    VALENCE_FIELD_NUMBER: _ClassVar[int]
    AROUSAL_FIELD_NUMBER: _ClassVar[int]
    DOMINANCE_FIELD_NUMBER: _ClassVar[int]
    EMOTIONS_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    valence: float
    arousal: float
    dominance: float
    emotions: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, timestamp: _Optional[int] = ..., valence: _Optional[float] = ..., arousal: _Optional[float] = ..., dominance: _Optional[float] = ..., emotions: _Optional[_Iterable[float]] = ...) -> None: ...

class EmotionStream(_message.Message):
    __slots__ = ("states",)
    STATES_FIELD_NUMBER: _ClassVar[int]
    states: _containers.RepeatedCompositeFieldContainer[EmotionState]
    def __init__(self, states: _Optional[_Iterable[_Union[EmotionState, _Mapping]]] = ...) -> None: ...
