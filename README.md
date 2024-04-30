## Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://coach-platform-api-b2a0c10b1c34.herokuapp.com).

This section provides a step-by-step guide to deploy the Django application with a Heroku and PostgreSQL database.

### Prerequisites

Before deploying, ensure you have the following:

- A Heroku account. [Sign up here](https://signup.heroku.com/) if you don't have one.
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed on your machine.
- Git installed on your machine.

### Deploying to Heroku

1. **Log in to Heroku**: Open your terminal and log in to Heroku using the Heroku CLI:

   ```
   heroku login
   ```

2. **Create a Heroku App**: Create a new Heroku app:

   ```
   heroku create your-app-name
   ```

   Replace `your-app-name` with the desired name for your application on Heroku.

3. **Add Heroku PostgreSQL**: Add the Heroku PostgreSQL add-on to your app:

   ```
   heroku addons:create heroku-postgresql:hobby-dev --app your-app-name
   ```

   This will provision a new Postgres database for your application.

4. **Configure Environment Variables**: Set the necessary environment variables such as `SECRET_KEY`, `DEBUG`, and any other variables you need for your project:

   ```
   heroku config:set SECRET_KEY='your_secret_key' DEBUG=False --app your-app-name
   ```

5. **Push Code to Heroku**: Push your code from your Git repository to Heroku:

   ```
   git push heroku master
   ```

   If you're pushing a non-master branch, use `git push heroku your-branch:master`.

6. **Run Migrations**: Once your code is deployed, run your migrations:

   ```
   heroku run python manage.py migrate --app your-app-name
   ```

7. **Create a Superuser**: Create an administrative user:

   ```
   heroku run python manage.py createsuperuser --app your-app-name
   ```

8. **Open the App**: Open your deployed app in a web browser:

   ```
   heroku open --app your-app-name
   ```

### PostgreSQL Database

The application uses PostgreSQL as its database provided by Heroku. Upon deployment, the database URL is automatically added to your app's configuration under the `DATABASE_URL` environment variable. The application is configured to use this variable in production.

For local development, make sure to update your `settings.py` to use the `DATABASE_URL`:

```python
import dj_database_url
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
```

Make sure you have `dj-database-url` in your requirements file to parse the `DATABASE_URL` environment variable:

```
pip install dj-database-url
```

### Final Steps

After deployment, check the logs to ensure everything is running smoothly:

```
heroku logs --tail --app your-app-name
```

For further information on troubleshooting or advanced configurations, consult the Heroku Dev Center or this application's documentation.

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

| Key              | Value            |
| ---------------- | ---------------- |
| `CLOUDINARY_URL` | user's own value |
| `DATABASE_URL`   | user's own value |
| `SECRET_KEY`     | user's own value |
| `DEV`            | 1                |

Heroku needs three additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- _replace **app_name** with the name of your primary Django app name; the folder where settings.py is located_

The **runtime.txt** file needs to know which Python version you're using:

1. type: `python3 --version` in the terminal.
2. in the **runtime.txt** file, add your Python version:
   - `python-3.9.18`

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace _app_name_ with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
  - `git push heroku main`

The project should now be connected and deployed to Heroku!

### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/JohnnySonTrinh/coach-api)
2. Locate the Code button above the list of files and click it
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
   - `git clone https://github.com/JohnnySonTrinh/coach-api.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/JohnnySonTrinh/coach-api)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/JohnnySonTrinh/coach-api)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

#### Environment Variables

- **Local**: Environment variables might be set directly in me development environment or stored in a .env file that is not committed to version control for security reasons.
- **Deployment**: On Heroku, environment variables should be set through the platform's settings (Config Vars) to keep sensitive information like database URLs, secret keys, and third-party API keys secure.

#### Database

- **Local**: I use SQLite as your database for simplicity and ease of setup in a local development environment.
- **Deployment**: On Heroku, I use a more robust database like PostgreSQL. Heroku offers its own PostgreSQL service, which can be easily integrated into the project.


## Content
https://www.django-rest-framework.org