# Static-Site-Generator-Pclub
[![python-logo]][python]
[![jinja][jinja-logo]][jinja]
[![github-actions-badge]][github-actions]
[![github-pages-badge]][github-pages]
[![markdown-logo]][markdown]

## Description

This Static site generator is written in `python` .
It takes content and user details directory as input and creates *static site* in the output directory.
It reads the blogs in content folder in `markdown` format and convert it to the html then there is magic of jinja library by which we insert every blog metadata to index file. we have other  pages also like about and contact we take markdown from user detail folder and create the pages.
There also a cool tag feature which shows blog of specific tag. There is RSS feed.

## Usage

### Blog posting

Put your all blog files in markdown format in content folder . There have format for example :
* title: Life at IITK
* date: 2023-06-19 6:43
* slug: first-year-experience
* summary: how my life going in iitk , how was MTH
* tag: experience college

After that you can put your **blog** content in markdown format .

### About and Contact 

In `User-details` folder you can edit  in `about.md` the Name ,  Age , Branch , Hobbies. then after that you can give the brief description that it takes to introduce yourself.
You can input your contact details in `contact.md` . their is *email* , *github* , *facebook* , *instagram* and *twitter* . After that you can put any text you want.

After putting all content you can run `generator.py` . It will give you output in `output` folder .
## Setup
 
Install the virtualenv if you dont have

```shell
pip install virtual venv
```

Create the virtual env

```shell
virtual venv
```

Activate the virtual venv

* For Windows:

```shell
.\venv\Scripts\activate
```

* For Ubunto/mac:

```shell
source venv/bin/activate
``` 

Install the Basic requirements

```shell
pip install -r requirements.txt
```

Input all the Blog files in the `content` folder and edit the files inside the `user-details` for about and contact page.

Then build the site

```shell
python generator.py
```

You will get your website at `output` folder .

## Github Pages

I have hosted the repo output to gh-pages there is a workflow. 

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Setting up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Checkout repository
        uses: actions/checkout@v2
      - name: Installing dependencies
        run: pip install -r ./requirements.txt

      - name: Build site
        run: python generator.py
        
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          personal_token: ${{ secrets.GITHUB_TOKEN }}
          publish_branch: gh-pages
          publish_dir: ./output

```

## Features

# Tagging

There are tags which can be used to filter out specific tagged Blogs.

# Generating Multiple Blog at once.

You can generate multiple blogs just put all blogs files in `content` folder.

[python]: https://www.python.org/
[python-logo]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[markdown]: https://en.wikipedia.org/wiki/Markdown
[markdown-logo]: https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white
[jinja]: https://jinja.palletsprojects.com/en/3.1.x/
[jinja-logo]: https://img.shields.io/badge/jinja-2-B41717?style=for-the-badge&logo=jinja
[github-pages]:https://pages.github.com/
[github-pages-badge]: https://img.shields.io/badge/GitHub%20Pages-222222?style=for-the-badge&logo=GitHub%20Pages&logoColor=white
[github-actions]: https://github.com/features/actions
[github-actions-badge]: https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white
