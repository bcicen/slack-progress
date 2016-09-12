from setuptools import setup, find_packages


setup(
    name='slack-progress',
    version='0.1',
    packages=find_packages(),
    description='A realtime progress bar for Slack',
    author='Bradley Cicenas',
    author_email='bradley@vektor.nyc',
    url='https://github.com/bcicen/slack-progress',
    install_requires= [ 'slacker>=0.9.25' ],
    license='http://opensource.org/licenses/MIT',
    classifiers=(
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License ',
    ),
    keywords='slack devops',
)
