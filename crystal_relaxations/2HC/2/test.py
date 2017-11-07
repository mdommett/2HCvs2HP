#!/usr/bin/env python
import read_file as rf
import edit_file as ef
import sys
in_f = sys.argv[1]
atoms=rf.read_qe(in_f)
ef.write_xyz(in_f[:-4]+"-opt.xyz",atoms)
