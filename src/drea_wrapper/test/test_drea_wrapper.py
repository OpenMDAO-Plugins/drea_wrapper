
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
                infile_name = 'base_%s.in' % item
                with open(infile_name, 'r') as inp:
                    result1 = inp.read()
                with open('%s.in' % item, 'r') as inp:
                    result2 = inp.read()
                
                lnum = 1
                for line1, line2 in zip(result1, result2):
                    try:
                        self.assertEqual(line1, line2)
                    except AssertionError as err:
                        raise AssertionError("line %d doesn't match file %s: %s"
                                             % (lnum, infile_name, err))
                    lnum += 1

                self.assertEqual(result1, result2)
            
            # Check output file parsing
                
            shutil.copyfile('base_ejectd.out', 'ejectd.out')
            comp.parse_output('Subsonic')
            
            with open('drea.dump', 'w') as out:
                dump(comp, stream=out, recurse=True)
            
            with open('base_drea.dump', 'r') as inp:
                result1 = inp.readlines()
            with open('drea.dump', 'r') as inp:
                result2 = inp.readlines()
            
            lnum = 1
            for line1, line2 in zip(result1, result2):
                # Omit lines with objects, because memory location differs
                if 'object at' not in line1:
                    try:
                        self.assertEqual(line1, line2)
                    except AssertionError as err:
                        raise AssertionError("line %d doesn't match file %s: %s"
                                             % (lnum, 'base_drea.dump', err))
                    lnum += 1

        finally:
            os.chdir(basename)
        
if __name__ == "__main__":
    unittest.main()
    
