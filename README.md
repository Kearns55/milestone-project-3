# [milestone-project-3](https://the-gargle-guardian-8687aeac050a.herokuapp.com)

Developer: Rebekah Kearns ([Kearns55](https://www.github.com/Kearns55))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Kearns55/milestone-project-3)](https://www.github.com/Kearns55/milestone-project-3/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/Kearns55/milestone-project-3)](https://www.github.com/Kearns55/milestone-project-3/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/Kearns55/milestone-project-3)](https://www.github.com/Kearns55/milestone-project-3)
[![badge](https://img.shields.io/badge/deployment-Heroku-purple)](https://the-gargle-guardian-8687aeac050a.herokuapp.com)


## Overview:
*The Gargle Guardian is a blog site centered around sharing your favourite cocktails and hopefully finding some new ones! The purpose of this site is to share all kinds of cocktail recipes, from classics like an Old Fashioned to that one your friend made in a random kitchen at 4am that was "actually really nice.." I have had this idea of a cocktail sharing based wesbite for many years and with the opportunity finally arising with this project, I knew I had to go for it. Hopefully you find a new go-to in the bar or even add your own to the site! Pull up a stool and welcome to the family.*

**Site Mockups**

![screenshot](documentation/mockup.PNG)

source: [milestone-project-3 amiresponsive](https://ui.dev/amiresponsive?url=https://the-gargle-guardian-8687aeac050a.herokuapp.com)

## UX

### The 5 Planes of UX

#### 1. Strategy

**Purpose**
- Provide users with tools to create, edit, and moderate their own cocktail recipe posts and user interactions.
- Offer users and guests an intuitive platform to explore, engage, and contribute to.

**Primary User Needs**
- Site owner need seamless tools for publishing and managing posts and comments.
- Registered users need the ability to engage with blog content through comments and account features.
- Guests need the ability to browse and enjoy blog content without registration.

**Business Goals**
- Foster a dynamic cocktail sharing platform with active user participation.
- Build a sense of community through discussions and user engagement.
- Ensure easy blog content management for owners.

#### 2. Scope

**[Features](#features)** (see below)

**Content Requirements**
- Blog post management (create, update, delete, and preview).
- Comment moderation and management tools.
- User account features (register, log in, edit/delete comments).
- Notification system for comment approval status.

#### 3. Structure

**Information Architecture**
- **Navigation Menu**:
  - Links to Home, Explore Cocktails dropdown, Signin/Register and a Contact Me form.
- **Hierarchy**:
  - Home page with information about the site and its owner.
  - Easy to use navigation buttons to explore cocktails either by category or just viewing them all, sorted by newest first.
  - Clear call-to-action buttons for account creation and engagement (e.g., commenting).

**User Flow**
1. Guest users browse cocktail posts → read posts and see commenter names.
2. Guest users register for an account → log in to leave comments.
3. Registered users leave comments → receive a pending approval notification.
4. Blog owners create, update, and manage posts → moderate comments.
5. Blog owners approve or reject comments → manage user interactions.

#### 4. Skeleton

**[Wireframes](#wireframes)** (see below)

#### 5. Surface

**Visual Design Elements**
- **[Colours](#colour-scheme)** (see below)
- **[Typography](#typography)** (see below)

### Colour Scheme

I used [coolors.co](https://coolors.co/ffffff-fd1e38-aa0202-c48c8c-4a0c17) to generate my color palette.

- `#000000` primary text.
- `#FD1E38` primary highlights.
- `#212529` secondary text.
- `#4a0c17` secondary highlights.

![screenshot](documentation/coolors.PNG)

### Typography

- [Bungee Inline](https://fonts.google.com/specimen/Bungee+Inline?query=Bungee+Inline) was used for the primary headers and titles.
- [Space Grotesk](https://fonts.google.com/specimen/Space+Grotesk) was used for all other secondary text.

## Wireframes

To follow best practice, wireframes were developed for mobile and desktop sizes.
I've used [Procreate](https://procreate.com/) to design my site wireframes.

| Page | Mobile | Desktop |
| --- | --- | --- |
| Register | ![screenshot](documentation/wireframes/mobile-register.PNG) | ![screenshot](documentation/wireframes/desktop-register.jpg) |
| Login | ![screenshot](documentation/wireframes/mobile-login.PNG) | ![screenshot](documentation/wireframes/desktop-login.jpg) |
| Home | ![screenshot](documentation/wireframes/mobile-home.PNG) | ![screenshot](documentation/wireframes/desktop-home.jpg) |
| Add Blog | ![screenshot](documentation/wireframes/mobile-add-blog.PNG) |  ![screenshot](documentation/wireframes/desktop-add-blog.jpg) |
| Edit Blog | ![screenshot](documentation/wireframes/mobile-edit-blog.jpg) | ![screenshot](documentation/wireframes/desktop-edit-blog.jpg) |
| Blog Post | ![screenshot](documentation/wireframes/mobile-blog-post.jpg) | ![screenshot](documentation/wireframes/desktop-blog-post.jpg) |


## User Stories

| Target | Expectation | Outcome |
| --- | --- | --- |
| As a guest user | I want to view all cocktails | so that I can easily browse everything available on the site. |
| As a guest user | I want to browse cocktails by category  | so I can quickly find drinks that match what I’m looking for. |
| As a guest user | I would like to create an account | so that I can access user-only features. |
| As a user | I want to view full cocktail details | so I can follow the recipe accurately. |
| As a user | I want to see a homepage | so I can learn more about the website and its purpose. |
| As a registered user | I would like to log in and log out  | so that I can securely access my account |
| As a registered user | I would like to register for an account | so that I can become part of the community and engage with the cocktail posts. |
| As a registered user | I would like to leave a comment on a blog post | so that I can share my thoughts or ask questions about the cocktail recipes. |
| As a registered user | I would like to receive a message saying my comment is pending approval | so that I understand it hasn't been posted immediately. |
| As a registered user | I would like to edit or delete my own comments | so that I can fix mistakes or retract my statement. |
| As a blog owner | I would like to create new blog posts with a title, featured image, and content | so that I can share my cocktail recipes with my audience. |
| As a blog owner | I would like to delete blog posts | so that I can remove outdated or irrelevant content from my blog. |
| As a blog owner | I would like to retrieve a list of all my published cocktail posts | so that I can manage them from a central dashboard. |
| As a blog owner | I would like to preview a post as draft before publishing it | so that I can ensure formatting and content appear correctly. |
| As a blog owner | I would like to review comments before they are published | so that I can filter out spam or inappropriate content. |
| As a blog owner | I would like to approve or reject comments from users | so that I can maintain control over the discussion on my posts. |
| As a blog owner | I would like to view a list of all comments (both approved and pending) | so that I can manage user engagement effectively. |
| As a blog owner | I would like to edit or delete user comments | so that I can clean up or remove inappropriate responses after they've been posted. |

## Features

### Existing Features

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Register | Authentication is handled by allauth, allowing users to register accounts. | ![screenshot](documentation/features/register.PNG) |
| Login | Authentication is handled by allauth, allowing users to log in to their existing accounts. | ![screenshot](documentation/features/login.PNG) |
| Logout | Authentication is handled by allauth, allowing users to log out of their accounts. | ![screenshot](documentation/features/logout.PNG) |
| Home Page | The homepage displays information on the sites background and purpose, and a welcome image.  | ![screenshot](documentation/features/homepage.PNG) |
| View Post | Users can view the full blog post details, including any comments. | ![screenshot](documentation/features/view-post.PNG) |
| Pagination | Cocktails are displayed in pages, with six posts per page. This provides better navigation for users through the post list. | ![screenshot](documentation/features/pagination.PNG) |
| Add Comments | Authenticated visitors can comment on blog posts; comments require approval before being published. | ![screenshot](documentation/features/add-comment.PNG) |
| Edit Comments | Authenticated visitors can edit their own comments. | ![screenshot](documentation/features/edit-comment.PNG) |
| Delete Comments | Authenticated visitors can delete their own comments. | ![screenshot](documentation/features/delete-comment.PNG) |
| Comment Approvals | Admins can approve or disapprove comments submitted by users before they are visible on the blog post. | ![screenshot](documentation/features/comment-approval.PNG) |
| Create Post | Site owners can create/publish blog posts, including setting a featured image using Cloudinary, all from the Django admin dashboard. | ![screenshot](documentation/features/create-post.PNG) |
| Update Post | Site owners can update/manage blog posts from the Django admin dashboard. | ![screenshot](documentation/features/update-post.PNG) |
| Delete Post | Site owners can delete blog posts from the Django admin dashboard. | ![screenshot](documentation/features/delete-post.PNG) |
| Collaboration Requests | Visitors can submit collaboration requests from the navbar, which are later reviewed by the admin. | ![screenshot](documentation/features/collaboration.PNG) |
| User Feedback | Clear and obvious Django messages are used to provide feedback to user actions. | ![screenshot](documentation/features/messages.PNG) |
| Heroku Deployment | The site is fully deployed to Heroku, making it accessible online and easy to manage. | ![screenshot](documentation/features/heroku.PNG) |

### Future Features

- **Post Search By Ingredients Functionality**: Add a search bar for users to quickly find cocktails they can make with ingredients they have already.
- **Post Likes/Dislikes or Upvotes**: Implement a "like" or "upvote" system for blog posts to encourage user engagement and give feedback to the author.
- **User Profiles**: Create personalized user profiles where authenticated users can view their comments, liked posts, and account information.
- **Comment Replies & Threads**: Enable users to reply to comments, creating nested comment threads for better discussions.
- **Post Sharing**: Add social media sharing buttons (e.g., Twitter, Facebook, LinkedIn) for users to share blog posts.
- **Notifications**: Implement a notification system that alerts users when their comments are approved, when new comments are made on a post they've commented on, or when new posts are published.
- **Email Subscriptions**: Allow users to subscribe to receive email notifications for new posts, updates, or newsletters.
- **Post Analytics**: Provide post authors with analytics such as views, time spent reading, and engagement rates.
- **Multilingual Support**: Add the ability to write and view blog posts in multiple languages, broadening the audience.
- **Content Flagging/Reporting**: Allow users to flag or report inappropriate content (comments or posts) for moderation.
- **SEO Optimization**: Implement features for SEO, such as meta tags, custom URLs, and keywords for better search engine ranking.
- **Dark Mode Theme for Users**: Allow users to customize the visual theme of the site to suit their preferences.

## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=007ACC)](https://code.visualstudio.com) | Local IDE for development. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) | Online static file storage. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |
| [![badge](https://img.shields.io/badge/W3Schools-grey?logo=w3schools&logoColor=04AA6D)](https://www.w3schools.com) | Tutorials/Reference Guide |
| [![badge](https://img.shields.io/badge/Copilot-grey?logo=githubcopilot&logoColor=##000000)](https://github.com/copilot) | Help debug, troubleshoot, and explain things. |

## Database Design

### Data Model

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models. Understanding the relationships between different tables can save time later in the project.

![screenshot](documentation/erd.PNG)

I have used `Mermaid` to generate an interactive ERD of my project.

```mermaid
erDiagram

    USER {
        int id PK
        string username
        string email
        string password
    }

    GLASSTYPE {
        int id PK
        string name
    }

    CATEGORY {
        int id PK
        string name
    }

    SOURCETYPE {
        int id PK
        string name
    }

    COCKTAIL {
        int id PK
        string name
        text description
        string image
        datetime created_on
        string slug
        text ingredients
        text garnish
        text instructions
        bool approved
        int author_id FK
        int glass_type_id FK
        int source_type_id FK
        int category_id FK
    }

    COMMENT {
        int id PK
        int cocktail_id FK
        int author_id FK
        text body
        bool approved
        datetime created_on
    }


    %% RELATIONSHIPS

    USER ||--o{ COCKTAIL : "writes"
    USER ||--o{ COMMENT : "comments"

    GLASSTYPE ||--o{ COCKTAIL : "glass type"
    CATEGORY ||--o{ COCKTAIL : "category"
    SOURCETYPE ||--o{ COCKTAIL : "source type"

    COCKTAIL ||--o{ COMMENT : "has comments"
```


source: [Mermaid]()

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://www.github.com/Kearns55/milestone-project-3/projects) served as an Agile tool for this project. Through it, EPICs, User Stories, issues/bugs, and Milestone tasks were planned, then subsequently tracked on a regular basis using the Kanban project board.

![screenshot](documentation/gh-projects.PNG)

### GitHub Issues

[GitHub Issues](https://www.github.com/Kearns55/milestone-project-3/issues) served as an another Agile tool. There, I managed my User Stories and Milestone tasks, and tracked any issues/bugs.

| Link | Screenshot |
| --- | --- |
| [![GitHub issues](https://img.shields.io/github/issues-search/Kearns55/milestone-project-3?query=is%3Aissue%20is%3Aopen%20-label%3Abug&label=Open%20Issues&color=yellow)](https://www.github.com/Kearns55/milestone-project-3/issues?q=is%3Aissue%20is%3Aopen%20-label%3Abug) | ![screenshot](documentation/gh-issues-open.PNG) |
| [![GitHub closed issues](https://img.shields.io/github/issues-search/Kearns55/milestone-project-3?query=is%3Aissue%20is%3Aclosed%20-label%3Abug&label=Closed%20Issues&color=green)](https://www.github.com/Kearns55/milestone-project-3/issues?q=is%3Aissue%20is%3Aclosed%20-label%3Abug) | ![screenshot](documentation/gh-issues-closed.PNG) |

### MoSCoW Prioritization

I've decomposed my Epics into User Stories for prioritizing and implementing them. Using this approach, I was able to apply "MoSCoW" prioritization and labels to my User Stories within the Issues tab.

- **Must Have**: guaranteed to be delivered - required to Pass the project (*max ~60% of stories*)
- **Should Have**: adds significant value, but not vital (*~20% of stories*)
- **Could Have**: has small impact if left out (*the rest ~20% of stories*)
- **Won't Have**: not a priority for this iteration - future features

## Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://the-gargle-guardian-8687aeac050a.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables to match your private `env.py` file.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user-inserts-own-cloudinary-url |
| `DATABASE_URL` | user-inserts-own-postgres-database-url |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | any-random-secret-key |

Heroku needs some additional files in order to deploy properly.

- [requirements.txt](requirements.txt)
- [Procfile](Procfile)
- [.python-version](.python-version)

You can install this project's **[requirements.txt](requirements.txt)** (*where applicable*) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located*

The **[.python-version](.python-version)** file tells Heroku the specific version of Python to use when running your application.

- `3.12` (or similar)

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (*recommended*):

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (*replace `app_name` with your app name*)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For "Primary Interest", you can choose **Programmable Media for image and video API**.
- *Optional*: edit your assigned cloud name to something more memorable.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the leading `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.
    - `cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5)`
- This will go into your own `env.py` file, and Heroku Config Vars, using the **key** of `CLOUDINARY_URL`.

### PostgreSQL

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net) for the Relational Database with Django.

> [!CAUTION]
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Submitted my email address to the CI PostgreSQL Database link above.
- An email was sent to me with my new Postgres Database.
- The Database connection string will resemble something like this:
    - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- You can use the above URL with Django; simply paste it into your `env.py` file and Heroku Config Vars as `DATABASE_URL`.

### WhiteNoise

This project uses the [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) to aid with static files temporarily hosted on the live Heroku site.

To include WhiteNoise in your own projects:

- Install the latest WhiteNoise package:
    - `pip install whitenoise`
- Update the `requirements.txt` file with the newly installed package:
    - `pip freeze --local > requirements.txt`
- Edit your `settings.py` file and add WhiteNoise to the `MIDDLEWARE` list, above all other middleware (apart from Django’s "SecurityMiddleware"):

```python
# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # any additional middleware
]
```


### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

Sample `env.py` file:

```python
import os

os.environ.setdefault("SECRET_KEY", "any-random-secret-key")
os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")
os.environ.setdefault("CLOUDINARY_URL", "user-inserts-own-cloudinary-url")  # only if using Cloudinary

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` (*Windows/Linux*) or `⌘+C` (*Mac*)
- Make any necessary migrations: `python3 manage.py makemigrations --dry-run` then `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate --plan` then `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (*if applicable*): `python3 manage.py loaddata file-name.json` (*repeat for each file*)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*
- **NOTE**: You should never make a backup of the default *admin* or *users* data with confidential information.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://www.github.com/Kearns55/milestone-project-3).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	- `git clone https://www.github.com/Kearns55/milestone-project-3.git`
7. Press "Enter" to create your local clone.

Alternatively, if using Ona (formerly Gitpod), you can click below to create your own workspace using this repository.

[![Open in Ona-Gitpod](https://ona.com/run-in-ona.svg)](https://gitpod.io/#https://www.github.com/Kearns55/milestone-project-3)

**Please Note**: in order to directly open the project in Ona (Gitpod), you should have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/Kearns55/milestone-project-3).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits

### Content

| Source | Notes |
| --- | --- |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files |
| [I Think Therefore I Blog](https://codeinstitute.net) | Code Institute walkthrough project inspiration |
| [Bootstrap](https://getbootstrap.com) | Various components / responsive front-end framework |
| [Cloudinary API](https://cloudinary.com) | Cloud storage for static/media files |
| [Whitenoise](https://whitenoise.readthedocs.io) | Static file service |
| [Django](https://www.djangoproject.com/) | Django documentation for help and tips while using the program |
| [ChatGPT](https://chatgpt.com) | Help with code logic and explanations |

### Media

| Source | Notes |
| --- | --- |
| [favicon.io](https://favicon.io) | Generating the favicon |
| [TinyPNG](https://tinyPNG.com) | Compressing images < 5MB |
| [Pexels](https://www.pexels.com/photo/cocktails-neon-signage-3566120/) | Homepage image |
| [Pexels](https://www.pexels.com/photo/assorted-wine-bottles-1283219/) | Default Image background image |


**All cocktail images are sourced from **Pexels** and used under the Pexels free license.**


| Cocktail | Source |
|----------|--------|
| Passionfruit Lemonade | [Pexels](https://www.pexels.com/photo/close-up-shot-of-a-cocktail-drink-with-mint-leaves-7377089/) |
| Mick's Whip | [Pexels](https://www.pexels.com/photo/refreshing-fernet-and-coke-in-a-glass-34328333/) |
| Espresso Martini | [Pexels](https://www.pexels.com/photo/espresso-martini-on-white-table-18059150/) |
| Frozen Strawberry Daiquiri | [Pexels](https://www.pexels.com/photo/cocktail-and-oranges-on-a-table-20371516/) |
| Mexican Mule | [Pexels](https://www.pexels.com/photo/ice-in-decorative-cup-19120333/) |
| Aperol Spritz | [Pexels](https://www.pexels.com/photo/shallow-focus-photography-of-wine-glass-with-slice-of-fruit-on-top-of-brown-wood-1280364/) |
| Margarita | [Pexels](https://www.pexels.com/photo/glass-of-sweet-cold-alcoholic-cocktail-on-table-5490831/) |
| Mojito | [Pexels](https://www.pexels.com/photo/a-bottle-of-white-rum-and-a-fresh-cocktail-16845291/) |
| Old Fashioned | [Pexels](https://www.pexels.com/photo/glass-of-beverage-2663974/) |
| Averna Sour | [Pexels](https://www.pexels.com/photo/beverages-mixology-16258086/) |
| Amaretto Sour | [Pexels](https://www.pexels.com/photo/classic-gin-sour-cocktail-on-leather-background-30196890/) |
| Whiskey Sour | [Pexels](https://www.pexels.com/photo/photo-of-a-cocktail-drink-on-a-cement-surface-7427259/) |


### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN) for the support throughout the development of this project.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) and [Code Institute Discord community](https://discord-portal.codeinstitute.net) for the moral support; it kept me going during periods of self doubt and impostor syndrome.
- I would like to thank my partner, for believing in me, and allowing me to make this transition into software development.



