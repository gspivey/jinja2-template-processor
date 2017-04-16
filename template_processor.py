#!/usr/bin/env/python

"""Python script to hande a website build step for a static website
templated with jinja2.

Example:
    Run:
    $ python templates/template_processor.py

    Directory Structure:
    Script expects to be run from basedir
    /basedir
        /templates
            .templateignore
            base.html
            index.html
            template_processor.py

        /.public

    Ignored files in .templateignore:
    Add any file in templates directory that will not produce a final html file
        .templateignore
        base.html
        template_processor.py

Todo:
    * TODO add argepase user interface
    * TODO turn into a python module
    * TODO allow script to be run from anywhere with target directory
 
"""

import codecs
import glob
import os
import shutil

from jinja2 import Environment, select_autoescape, FileSystemLoader

def ignoreFile(ignore="templates/.templateignore"):
    """Find text file that includes all files inside teplate directory
    that should not be prcocessed by the template_processor.py script.

    Args:
        ignore (string): Path to file that lists files that sould not be
            processed

    Returns:
        List of files that should be ignored
    """
    with open(ignore, 'r') as i:
        files = [line.strip() for line in i]

    return files

def main():
    """Process a directory of jinja2 templates.
    Consume a .templateignore file to identify what files
    to exclude from the template processing.

    creates a .public directory on the same level
    as the templates directory being processed.

    the .public file contains all the web ready html files

    Args:
        none

    Returns:
        none
    """
    shutil.rmtree(".public")
    os.mkdir(".public")

    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html'])
    )

    ignore_files = ignoreFile()
    files_in_dir = os.walk('templates')
    filenames = [filename for _, _, filename in files_in_dir]
    files = [filename for filename in filenames[0] if filename not in ignore_files]
    for i in files:
        template = env.get_template(i)
        final_html = template.render()


        write_prefix = glob.glob(".public")[0]
        write_path = os.path.join(write_prefix, i)
        print write_path
        try:
            html_file = codecs.open(write_path, 'w', 'utf8')
            html_file.write(final_html)
        finally:
            html_file.close()
if __name__ == '__main__':
    main()
