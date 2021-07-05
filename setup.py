from setuptools import setup


version = "0.1.2"

with open("README.md", "r") as f:
    long_descr = f.read()
    

setup(
        name = "asciify",
        packages = ["asciify"],
        entry_points = {
            "console_scripts": ['asciify = asciify.asciify:main']
            },
        install_requires = [
            'Pillow'
            ],
        include_package_data=True,
        version = version,
        description = "A python tool which generates ASCII art for any image",
        long_description = long_descr,
        author = "Shiva Tamil Kumaran",
        author_email = "anand.tk.03@gmail.com",
        url = "https://github.com/shiva-tk/asciify"
        )
