from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
  scripts=['src/pose_estimator_node.py', 'src/robot_track_map_node.py'],
  packages=['odometry_gnss_pose_estimator'],
  package_dir={'':'src'}
  )
setup(**d)
