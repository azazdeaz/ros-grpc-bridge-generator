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
import glob

PKG = 'grpc_api_generator'
rospack = rospkg.RosPack()

SNAPSHOTS_PATH = join(rospack.get_path(PKG), 'test/snapshots')
RESULT_PATH = join(rospack.get_path(PKG), 'test/result')
EXPECTED_PATH = join(rospack.get_path(PKG), 'test/expected')

class TestGeneratedPackages(unittest.TestCase):
    def _match_packages(self, pkg_name):
        """Compare a pkg in the expected and the result folder"""
        # found_difference = False
        for file_exp in glob.glob(join(EXPECTED_PATH, pkg_name, '**/*')):
            file_missing = True
            for file_res in glob.glob(join(RESULT_PATH, pkg_name, '**/*')):
                relative_exp = file_exp[len(EXPECTED_PATH)+1:]
                relative_res = file_res[len(RESULT_PATH)+1:]
                if os.path.basename(relative_exp) == os.path.basename(relative_res):
                    file_missing = False
                    self.assertMultiLineEqual(
                        open(file_exp).read(),
                        open(file_res).read(),
                        'differences found in {}'.format(relative_res))
            self.assertFalse(file_missing, 'Can\'t find {} in the result package'.format(relative_exp))

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
