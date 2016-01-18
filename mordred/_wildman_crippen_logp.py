from ._base import Descriptor
from rdkit.Chem import Crippen as _Crippen


class WildmanCrippenLogP(Descriptor):
    r'''
    Wildman-Crippen LogP/MR descriptor

    :type prop: str
    :param type: 'LogP' or 'MR'

    :rtype: float
    '''

    @classmethod
    def preset(cls):
        yield cls('LogP')
        yield cls('MR')

    explicit_hydrogens = False
    require_connected = False

    def __str__(self):
        return 'Crippen{}'.format(self.prop)

    descriptor_keys = 'prop',

    def __init__(self, prop='LogP'):
        assert prop in ['LogP', 'MR']
        self.prop = prop

    def calculate(self, mol):
        if self.prop == 'LogP':
            return _Crippen.MolLogP(mol)
        else:
            return _Crippen.MolMR(mol)
