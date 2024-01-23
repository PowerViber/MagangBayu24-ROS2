from setuptools import setup

package_name = 'tugas1'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='reihan',
    maintainer_email='arianza429@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'talker = tugas1.publisher_member_function:main',
                'listener = tugas1.subscriber_member_function:main',
        ],
    },
)
