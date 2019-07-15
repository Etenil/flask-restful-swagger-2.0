try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README') as file:
    long_description = file.read()

setup(name='eai-flask-restful-swagger',
      version='0.35',
      url='https://github.com/etenil/flask-restful-swagger-2.0',
      zip_safe=False,
      packages=['eai_flask_restful_swagger'],
      package_data={
        'eai_flask_restful_swagger': [
        ]
      },
      description='Extract swagger specs from your flask-restful project. Project based on flask-restful-swagger by Ran Tavory.',
      author='Soeren Wegener',
      license='MIT',
      long_description=long_description,
      install_requires=['Flask-RESTful>=0.2.12'],
      tests_require=['nose'],
      test_suite='nose.collector'
      )
