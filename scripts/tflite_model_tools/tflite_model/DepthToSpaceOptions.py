# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class DepthToSpaceOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsDepthToSpaceOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = DepthToSpaceOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def DepthToSpaceOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # DepthToSpaceOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # DepthToSpaceOptions
    def BlockSize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def DepthToSpaceOptionsStart(builder): builder.StartObject(1)
def DepthToSpaceOptionsAddBlockSize(builder, blockSize): builder.PrependInt32Slot(0, blockSize, 0)
def DepthToSpaceOptionsEnd(builder): return builder.EndObject()


class DepthToSpaceOptionsT(object):

    # DepthToSpaceOptionsT
    def __init__(self):
        self.blockSize = 0  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        depthToSpaceOptions = DepthToSpaceOptions()
        depthToSpaceOptions.Init(buf, pos)
        return cls.InitFromObj(depthToSpaceOptions)

    @classmethod
    def InitFromObj(cls, depthToSpaceOptions):
        x = DepthToSpaceOptionsT()
        x._UnPack(depthToSpaceOptions)
        return x

    # DepthToSpaceOptionsT
    def _UnPack(self, depthToSpaceOptions):
        if depthToSpaceOptions is None:
            return
        self.blockSize = depthToSpaceOptions.BlockSize()

    # DepthToSpaceOptionsT
    def Pack(self, builder):
        DepthToSpaceOptionsStart(builder)
        DepthToSpaceOptionsAddBlockSize(builder, self.blockSize)
        depthToSpaceOptions = DepthToSpaceOptionsEnd(builder)
        return depthToSpaceOptions