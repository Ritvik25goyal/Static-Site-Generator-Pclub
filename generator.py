import os
from datetime import datetime
from jinja2 import Environment, PackageLoader
from markdown2 import markdown

''' markdown post to dictionary conversion '''
POSTS = {}
tags = []
for markdown_post in os.listdir('content'):
    file_path = os.path.join('content', markdown_post)
    with open(file_path, 'r') as file:
        POSTS[markdown_post] = markdown(file.read(), extras=['metadata'])
        post_metadata = POSTS[markdown_post].metadata
        POSTS[markdown_post].metadata['tag'] = post_metadata['tag'].split(" ")
        for i in POSTS[markdown_post].metadata['tag']:
            if i in tags:
                continue
            else:
                tags.append(i)

# Arranging Post so that latest post come first
POSTS = {
    post: POSTS[post] for post in sorted(POSTS, key=lambda post: datetime.strptime(POSTS[post].metadata['date'], '%Y-%m-%d  %H:%M'), reverse=True)
}

# Reading user details
user_details = {}
with open('User_details/about.md','r') as file:
    user_details['About'] = markdown(file.read() , extras=['metadata'])
with open('User_details/contact.md','r') as file:
    user_details['Contact'] = markdown(file.read() , extras=['metadata'])

# Declaring env for templating 
env = Environment(loader=PackageLoader('generator', 'templates'))

# templates
index_template = env.get_template('index.html')
about_template = env.get_template('about.html')
contact_template = env.get_template('contact.html')
post_template = env.get_template('post-detail.html')
tag_template = env.get_template('tag.html')
rss_template = env.get_template('rssfeed.xml')

index_posts_metadata = [POSTS[post].metadata for post in POSTS]
rss_feed_metadata = index_posts_metadata
about_content = user_details['About']
about_metadata = user_details['About'].metadata
contact_content = user_details['Contact']
contact_metadata = user_details['Contact'].metadata

# rendered data
index_html_content = index_template.render(posts=index_posts_metadata)
about_html_content = about_template.render(context=about_content, metadata=about_metadata)
contact_html_content = contact_template.render(context=contact_content, metadata=about_metadata)
rss_feed_content = rss_template.render(posts= rss_feed_metadata)

with open('output/index.html', 'w') as file:  #index file copy
    file.write(index_html_content)
with open('output/about.html', 'w') as file:  #about file copy
    file.write(about_html_content)
with open('output/contact.html', 'w') as file:  #contact file copy
    file.write(contact_html_content)
with open('output/feed/rssfeed.xml', 'w') as file:  #feed file copy
    file.write(rss_feed_content)

# Css copy
with open('static/css/style.css' , 'r') as file:
    css_content = file.read()
    os.makedirs(os.path.dirname('output/css/style.css'), exist_ok=True)
    with open('output/css/style.css', 'w') as output_css:
        output_css.write(css_content)

# Js copy
with open('static/js/script.js' , 'r') as file:
    js_content = file.read()
    os.makedirs(os.path.dirname('output/js/script.js'), exist_ok=True)
    with open('output/js/script.js', 'w') as output_js:
        output_js.write(js_content)

# every post index file creation
for post in POSTS:
    post_metadata = POSTS[post].metadata
    post_data = {
        'content': POSTS[post],
        'title': post_metadata['title'],
        'date': post_metadata['date'],
    }
    # Post index file creation
    post_html_content = post_template.render(post=post_data)
    post_file_path = 'output/posts/{slug}/index.html'.format(slug=post_metadata['slug'])
    os.makedirs(os.path.dirname(post_file_path), exist_ok=True)
    with open(post_file_path, 'w') as file:
        file.write(post_html_content)

for tag in tags:
    tags_post_metadata = []
    for post in POSTS:
        if tag in POSTS[post].metadata['tag']:
            tags_post_metadata.append(POSTS[post].metadata)
    tag_html_content = tag_template.render(posts=tags_post_metadata)
    tag_file_path = f'output/tags/{tag}.html'
    os.makedirs(os.path.dirname(tag_file_path), exist_ok=True)
    with open(tag_file_path, 'w') as file:
        file.write(tag_html_content)