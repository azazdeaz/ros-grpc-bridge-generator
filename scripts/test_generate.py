#!/usr/bin/env python3

import roslib
import rospy
import rospkg
import unittest
import sys
import os
from os import listdir
from os.path import isfile, join
import os
from pathlib import Path
import difflib

PKG = 'grpc_api_generator'
rospack = rospkg.RosPack()

SNAPSHOTS_PATH = join(rospack.get_path(PKG), 'test/snapshots')
RESULT_PATH = join(rospack.get_path(PKG), 'test/result')
EXPECTED_PATH = join(rospack.get_path(PKG), 'test/expected')


class TestGeneratedPackages(unittest.TestCase):
    def _match_packages(self, pkg_name):
        """Compare a pkg in the expected and the result folder"""
        for path_exp in Path(join(EXPECTED_PATH, pkg_name)).rglob('*'):
            if not path_exp.is_file():
                continue

            path_exp_relative = path_exp.relative_to(EXPECTED_PATH)
            file_missing = True

            for path_res in Path(join(RESULT_PATH, pkg_name)).rglob('*'):
                if path_exp_relative == path_res.relative_to(RESULT_PATH):
                    file_missing = False
                    diff = difflib.unified_diff(
                        open(path_exp).readlines(),
                        open(path_res).readlines(),
                        fromfile='expected',
                        tofile='result')
                    diff = ''.join(diff)
                    self.assertEqual(diff, '', '\n\nDifferences found in {}\n{}'.format(
                        path_exp_relative, diff))
            self.assertFalse(
                file_missing, 'Can\'t find {} in the result package'.format(path_exp_relative))

    def test_generated_pkgs_look_as_expected(self):
        """Generate packages for each snapshot and compare them to ones in the in expected folder"""
        generate_cmd = '''roslaunch grpc_api_generator generate.launch \
                keep_existing_snapshot:=true \
                snapshot_path:={snapshot_path} \
                pkg_name:={pkg_name} \
                pkgs_root:={result_path}
            '''
        for f in listdir(SNAPSHOTS_PATH):
            if f.endswith('.ini'):
                pkg_name = f[:-4]
                cmd = generate_cmd.format(
                    pkg_name=pkg_name,
                    snapshot_path=join(SNAPSHOTS_PATH, f),
                    result_path=RESULT_PATH,
                )
                rospy.logerr(cmd)
                os.system(cmd)
                self._match_packages(pkg_name)


if __name__ == '__main__':
    import rostest
    rostest.rosrun(PKG, 'test_generate.py', TestGeneratedPackages)
