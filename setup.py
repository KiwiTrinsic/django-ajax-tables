import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django_ajax_tables",
    version="1.1.1",
    author="Dustin Cotton",
    author_email="dcotton@stormpurple.net",
    description="Django tag for ajax-enabled tables",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KiwiTrinsic/django-ajax-tables",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Environment :: Web Environment",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ],
)
