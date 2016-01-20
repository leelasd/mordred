from ._base import Descriptor
from ._common import AdjacencyMatrix as A
from ._matrix_attributes import get_method, methods


class AdjacencyMatrix(Descriptor):
    r"""adjacency matrix descriptor.

    :type type: str
    :param type: :ref:`matrix_aggregating_methods`

    :rtype: float
    """

    explicit_hydrogens = False

    @classmethod
    def preset(cls):
        return map(cls, methods)

    def __str__(self):
        return '{}_A'.format(self.type.__name__)

    __slots__ = ('type',)

    def __init__(self, type='SpMax'):
        self.type = get_method(type)

    def dependencies(self):
        return dict(
            result=self.type(
                A(
                    self.explicit_hydrogens,
                    False,
                ),
                self.explicit_hydrogens,
                self.gasteiger_charges,
                self.kekulize,
            )
        )

    def calculate(self, mol, result):
        return result
