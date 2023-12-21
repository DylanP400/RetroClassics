# Retro Classics

Retro Classics is built using a combination of HTML, CSS, JavaScript, Python, and Django. I have incorporated Cloudinary for efficient image management and Stripe for secure and convenient payment processing.

## Contents

* [User Experience](#user-experience)

  * [User Stories](#user-stories)

  * [Initial Discussion](#initial-discussion)

  * [Agile Methodology](#agile-methodology)

* [Design](#design)

  * [Colour Scheme](#colour-scheme)

  * [typograpghy](#typograpghy)

  * [Wireframes](#wireframes)

* [Features](#features)

  * [Existing Features](#existing-features)

  * [Future Features](#future-features)

* [Testing](#testing)

* [Technologies Used](#technologies-used)

* [Deployment](#deployment)
  
  * [ElephantSQL](#elephantsql-database-setup)

  * [Heroku](#heroku)

  * [Local Deployment](#local-deployment)

## User Experience

### User stories

* **Iteration 1**

  * **Epic Pre-Developement.**

    * **USER STORY:** *Wireframes*.

      * As a **developer**, I want to **create wireframes** to **visualize the layout and features of the eCommerce store.**

    * **USER STORY**: *Frameworks and Libraries*.

      * As a **developer**, I want to **decide on the frameworks and libraries** that will be **most beneficial for my project.**

    * **USER STORY:** *Set up Django.*

      * As a **developer**, I want to **initialize the Django project** to lay the **foundation for my eCommerce store.**

  * **USER STORY:** *User Authentication.*

    * As a **developer**, I want to **implement user authentication** so that **users can have personalized experiences**.

  * **USER STORY:** *Basic Navigation.*

    * As a **developer**, I want to **implement basic navigation features** to facilitate user flow **through the eCommerce store**.

  * **USER STORY:** *Homepage Design.*

    * As a **developer**, I want to **design a compelling homepage** to provide users with an **overview of what the eCommerce store offers.**

  * **USER STORY:** *Background image.*

    * As a **developer**, I want to **set an engaging background image for the homepage** to create an **retro feel to the shop**.

* **Iteration 2**

  * **USER STORY:** *Basic Product Management.*

    * As a **developer**, I want to create a **simple product management system** so that products can be **added, viewed, and categorized in the eCommerce store.**

  * **USER STORY:** *Products.*

    * As a **developer**, I want to make it **easy to add, view, and organize products**

  * **USER STORY:** *Shopping cart.*

    * As a **developer**, I want to implement a **functional shopping cart** and add **styling for a user-friendly appearance.**

  * **USER STORY:** *Static And Media Files.*

    * As a **developer**, I want to **manage static and media files** effectively to ensure **quick page loads and optimized performance**.

### Agile Methodology

### Initial Discussion

## Design

### Colour Scheme

### Typograpghy

### Wireframes

<details>
<summary>Desktop Wireframes</summary>

<details>
<summary>Home Page</summary>

![Home Page](./media/readme/wireframes/wireframe-home-page.png)
</details>

<details>
<summary>All Products</summary>

![All Products](./media/readme/wireframes/wireframe-all-products.png)
</details>

<details>
<summary>Product Detail</summary>

![Product Detail](./media/readme/wireframes/wireframe-product-detail.png)
</details>

<details>
<summary>Profile</summary>

![Profile](./media/readme/wireframes/wireframe-profile.png)
</details>

<details>
<summary>Sign Up</summary>

![Sign Up](./media/readme/wireframes/wireframe-signup.png)
</details>

<details>
<summary>Sign In</summary>

![Sign In](./media/readme/wireframes/wireframe-signin.png)
</details>
</details>

## Features

### Existing Features

### Future Features

## Testing

## Technologies Used

## Deployment

### ElephantSQL Database Setup

**Step 1: Obtain ElephantSQL Database URL**

1. **Sign up or sign in to ElephantSQL:**

   * *If you don't have an account, sign up otherwise, log in to your account.*

2. **Create a new ElephantSQL instance:**

   * *From the dashboard, click on `Create New Instance`.*

   * *Choose a plan based on your requirements.*

3. **Retrieve your ElephantSQL Database URL:**

   * *Once the instance is created, click on it to view details.*
   * *Find and copy the `URL` provided this is your `ElephantSQL Database URL`.*

### Step 2: Configure Django Project

1. **Add DATABASE_URL to env.py:**

   * *Open your `env.py` file.*

   * *Set `DATABASE_URL` to the value obtained from ElephantSQL.*

### Step 3: Use DATABASE_URL in Django Settings

1. **Update Django Settings:**

   * *Open your `settings.py` file in your Django project.

   * *Locate the `DATABASES` configuration.*

   * *Comment out the orignal django database settings*

   * *Update the `DATABASES` setting to use the `dj_database_url` package:*

     ```python
     import dj_database_url
     # At the top of settings.py with the other imports

     DATABASES = {
     'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
      }
      # Replace the orignal database with what is above

     ```

   * *This allows your Django project to use the ElephantSQL Database URL.*

2. **Migrate Database Changes:**

   * *Run the following commands in your terminal:*

     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

   * *This ensures that your database is updated with the latest changes.*

* **Note: Upcoming Changes to ElephantSQL Free Tier**
  
  * *ElephantSQL is making changes to its free tier in the next few months. If you're using or planning to use the free tier, be prepared for some tweaks in the deployment process.
  As of now, the steps in this guide are based on the current ElephantSQL setup. ElephantSQL will have updates regarding these changes check their official announcements and documentation for the latest info. If you run into any deployment problems or notice any differences refer to the updated ElephantSQL docs.*

## Heroku

### Step 1: Prepare Environment Variables

*Create an `env.py` file at the root level of your project. Copy and paste the following content into the file:*

```python
import os

# Replace placeholders with your actual values
os.environ['DATABASE_URL'] = 'Your_ElephantSQL_Database_url'
os.environ['SECRET_KEY'] = 'Your_Django_secret_key'
os.environ['CLOUDINARY_URL'] = 'Your_Cloudinary_url'
```

## Step 2: Heroku App Setup

1. **Sign up or sign in to your Heroku account:**
   * *If you don't have an account, sign up otherwise, log in to your account.*

2. **Create a new app from the Heroku dashboard:**
   * *Choose a name for your app.*
   * *Select the region that is most suitable for you.*

3. **Configure app settings:**
   * *In the app's settings, find and click on 'Reveal Config Vars'.*
   * *Add the following variables with their corresponding values:*
     * `DATABASE_URL`: *Your ElephantSQL Database URL.*
     * `SECRET_KEY`: *Your chosen Django secret key.*
     * `CLOUDINARY_URL`: *Your Cloudinary URL.*
     * `DISABLE_COLLECTSTATIC`: *Set to `1` for initial deployment.*
     * `PORT`: *Set to* `8000`

## Step 3: Deployment from GitHub

1. **Choose the Deploy option:**
   * *Go to the Deploy tab in your app dashboard.*

2. **Connect to GitHub:**
   * *Under Deployment method, choose Connect to GitHub.*

3. **Select your GitHub repository:**
   * *Find your GitHub repository by name and connect.*

4. **Choose deployment method:**
   * *At the bottom of the page, choose either Automatic Deployment or Manual Deployment (deploy by branch).*

5. **Initiate deployment:**
   * *Click on the option you prefer, and the deployment process should begin.*

6. **Monitor deployment progress:**
   * *After a while, your app should be deployed. You can check the progress in the Heroku dashboard.*


## Local Deployment

### How to Fork

**To fork the repository:**

1. *Log in to **Github.***
2. *Go to the **repository** for this project, [DylanP400/RetroClassics](https://github.com/DylanP400/RetroClassics)*
3. *Click the **Fork button** in the top right corner.*

### How to clone

**To clone the repository**

1. *Log in to **GitHub.***
2. *Go to the **repository** for this project, [DylanP400/RetroClassics](https://github.com/DylanP400/RetroClassics)*
3. *Click on the **code button**, select whether you would like to clone with **HTTPS**, **SSH** or **GitHub CLI** and copy the link shown.*
4. *Open the **terminal** in your **code editor** and change the current **working directory** to the location you want to use for the **cloned directory.***
5. *Type **'git clone'** into the **terminal** and then **paste** the link you copied in step 3. **Press enter**.*


![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

<!-- # Imagery 
https://pixabay.com/images/search/retro%20gaming/?pagi=2
https://www.pexels.com/search/video%20game/
https://www.rawpixel.com/search/Retro%20gaming?page=1&sort=curated&topic_group=_topics -->
