from setuptools import setup, find_namespace_packages

setup(name='mevaluator',
      packages=find_namespace_packages(include=["mevaluator", "mevaluator.*"]),
      version='0.2',
      description='MEvaluator: evaluator for medical image segmentation.',
      url='https://github.com/ShishuaiHu/MEvaluator',
      author='',
      author_email='',
      license='Apache License Version 2.0, January 2004',
      python_requires=">=3.9",
      install_requires=[
          "medpy",
          "batchgenerators>=0.25",
          "numpy",
          "SimpleITK>=2.2.1",
          "pandas",
      ],
      entry_points={
          'console_scripts': [
              'evaluate_folder = mevaluator.evaluator:nnunet_evaluate_folder'  # api available
          ],
      },
      keywords=['deep learning', 'image segmentation', 'medical image analysis',
                'medical image segmentation']
      )
