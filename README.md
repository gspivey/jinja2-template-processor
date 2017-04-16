# jinja2-template-processor

Python script to hande a website build step for a static website templated with jinja2.
by Gerard Spivey

## Goal

A simple tool to aid websites that have grown.
After your site grows past 4-5 statig pages maintaining it may become cumbersome.
At this point using a static site generator such as jekyll may be cumbersome or have limitations
based on our initial implementation.

This tool looks to aid in bringing website template capabilities to production.
This script can easily be used along with a continous integration (CI) server or manually ran
before site publication.

### Install dependencies:

```
pip install jinja2
```

### Ensure you have the correct directory structure

```
Directory Structure:
Script expects to be run from basedir
/basedir
    /templates
        .templateignore
        base.html
        index.html
        template_processor.py
    /.public
```

### Ignore files in the templates directory that will not create a html file
```
Ignored files in .templateignore:
Add any file in templates directory that will not produce a final html file
Ex:
    .templateignore
     base.html
     template_processor.py
```
