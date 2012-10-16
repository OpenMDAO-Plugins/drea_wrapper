
import unittest
import os
import sys
import shutil

from drea_wrapper.DREA import DREA
from openmdao.main.container import dump

class Drea_wrapperTestCase(unittest.TestCase):

    def setUp(self):
        pass
    
        
    def tearDown(self):
        for filename in ['ejectd.out', 'drea.dump', 'control.in',
                         'flocond.in', 'expnd.in', 'zrdmix.in',
                          'hwall.in']:
            if os.path.exists(filename):
                os.remove(filename)
        
    # add some tests here...
    
    def test_Drea_wrapper(self):
        
        comp = DREA()

        dirname = os.path.abspath(os.path.dirname(__file__))

        basename = os.getcwd()
        os.chdir(dirname)

        try:
            # Check input file generation
            
            comp.load_model(control_input='base_control.in',
                            flocond_input='base_flocond.in',
                            expnd_input='base_expnd.in',
                            zrdmix_input='base_zrdmix.in',
                            hwall_input='base_hwall.in')
            comp.setup()
            comp.generate_input('Subsonic')
    
            for item in ['control', 'flocond', 'expnd', 'zrdmix', 'hwall']:
                file1 = open('base_%s.in' % item, 'r')
                result1 = file1.read()
                file1.close()
                file2 = open('%s.in' % item, 'r')
                result2 = file2.read()
                file2.close()
                
                self.assertEqual(result1, result2)
            
            # Check output file parsing
                
            shutil.copyfile('base_ejectd.out', 'ejectd.out')
            comp.parse_output('Subsonic')
            
            file1 = open('drea.dump', 'w')
            dump(comp, stream=file1, recurse=True)
            file1.close()
            
            file1 = open('base_drea.dump', 'r')
            result1 = file1.readlines()
            file1.close()
            file2 = open('drea.dump', 'r')
            result2 = file2.readlines()
            file2.close()
            
            for line1, line2 in zip(result1, result2):
                # Omit lines with objects, because memory location differs
                if 'object at' not in line1:
                    self.assertEqual(line1, line2)

        finally:
            os.chdir(basename)
        
if __name__ == "__main__":
    unittest.main()
    