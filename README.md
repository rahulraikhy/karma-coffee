# Project 3: Karma Coffee - Ethical Coffee from Around the World

<!-- ABOUT THE PROJECT -->

## Project Overview

For my third project for General Assembly's Software Engineering Immersive course, we were given 7 days to create and build a full-stack website using 
Django and Python. For this project, we were split into 3 groups, both other groups had 4 team members, our group had 3 members.

![app screensot](https://github.com/SimpsonRoss/karma-coffee/assets/93015253/7bf577fa-3b69-4048-b7ef-4936ea5add04)

## Website

<strong><p><a href="https://karma-coffee-abe41bfb39f9.herokuapp.com/">Click to view the Karma Coffee website☕</a></p></strong>

  ***Stripe Test Details:***

- Test card details in order to test stripe checkout
  - Test Card: Success
    4242 4242 4242 4242
  - Test Card: Failed
    4000 0000 0000 0002
  - Test Card: 3DS Auth Needed
    4000 0027 6000 3184
- Enter any expiry date, for example:
  12/34
- Enter any 3 digit security code, for example:
  234

## About the Website

Welcome to Karma Coffee, where your coffee cravings meet the convenience of online shopping.

Karma Coffee is a robust and user-friendly coffee product ecommerce app designed to bring the rich world of coffee directly to your fingertips. Whether you're an avid coffee connoisseur or just starting to explore the world of specialty blends, our mission is to offer high-quality coffee products from different parts of the world while ensuring ethical sourcing. Karma Coffee has you covered.

![ezgif com-video-to-gif](https://github.com/rahulraikhy/karma-coffee/assets/121837375/4fddd91d-4c84-456e-8173-9bd82c9c4bf9)

<!-- GETTING STARTED -->

**Built With**

For this project we built a fullstack application using these tools:

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Node.js](https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)

<!-- ROADMAP -->

## Project Brief

- Have at least 2 data entities in addition to the User Model - one entity that represents the main functional idea for your app and another with a One:Many or Many:Many relationship with that main entity.
- Use OAuth authentication.
- Implement basic authorization that restricts access to features that need a logged in user in order to work
- Have full-CRUD data operations somewhere within the app's features.
- Have a consistent and polished user interface.
- Be deployed online via Heroku

## Planning

As our first project collaborating as a group, we found the planning stage vital to establishing our build structure, and our design was vital to aiding us staying away from each other's code. Our first course of action was to create an ERD and wireframe for what we wanted our single coffee company e-commerce site to look like. The ERD was created by myself, and the wireframe (which ended up almost identical to our final product) was created by my team members, Ross and Jihyeon.

## ERD

![Karma Coffee](https://github.com/SimpsonRoss/karma-coffee/assets/93015253/75a9cb5f-5594-4f9e-abf6-8b5bc28418e9)

## Wireframe

![Untitled](https://github.com/SimpsonRoss/karma-coffee/assets/93015253/d37c1587-dde5-43fc-a373-57df903208fd)

## Trello

Due to this being a collaborative project, we followed Agile methodologies with effective communication enhanced by Trello. We were able to consistantly assign tasks to ourselves, label them on the board so others knew what we were working on, constantly progress onto the next step as we knew what others were working on, and synchronise our timings for when we wanted to test more important moments, like creating the skeleton app at the beginning so everyone could begin working on other pages, especially important as one of the three of us was working in a different timezone with approximately 6 hours difference in timezomes.

![Screenshot 2023-09-29 at 00 25 00](https://github.com/rahulraikhy/karma-coffee/assets/121837375/88100a6d-4889-4537-9f7f-3567c035df41)

## MVP - Minimum Viable Product

- [x] AAU, I want a way to login.
- [x] AAU, I want to see the products and product details.
- [x] AAU, I want to add items in the basket, and edit, delete the items in the basket.
- [x] AAU, I want to purchase products.
- [x] AAU, I want to be able to leave and delete reviews for the products I purchased.

## NTH - Nice to have

- [x] AAU, I want to be able to filter the products.
- [x] AAU, I'd like to see payment/order confirmation.
- [x] AAU, I'd like to see my order history.
- [x] AAU, I'd like to read about the company.
- [x] AAU, I'd like to be able to log in with Google.
- [ ] AAU, I want to be able to search specific item.
- [ ] AAU, I want to be able to subscribe.

## Getting Started

Our group method to tackle this project was to divide key responsibilities between the three of us, and then assign pages for each of us to build, style, and implement our responsibilities across the pages. 

My key responsibility was to implement the user authorisation, a secondary authorisation (we had chosen google), create a sign up form and sign up page, a log in page, confirm a User could not leave, edit or delete reviews on coffee products without being logged in, and ensure the styling of these pages kept the theme of the overall website.

**Creating An Account**

![ezgif com-optimize (1)](https://github.com/rahulraikhy/karma-coffee/assets/121837375/7eaf1cc5-5880-4795-bd5b-98949cda9220)

**Logging in as an existing User**

![ezgif com-optimize (2)](https://github.com/rahulraikhy/karma-coffee/assets/121837375/5d395fb1-502a-4968-bb9e-ae1a77c8e53c)

**Google login**

![ezgif com-optimize (3)](https://github.com/rahulraikhy/karma-coffee/assets/121837375/e460ce25-7bf3-4e5b-bbfe-c117ab2abc14)

A key difference between the 3 modes of user authentication is that we wanted the user creating an account to be redirected immediately to the coffee product page, as we wanted them purchasing our products as quickly as possible.
Once a user already had an existing account, or logged in via google, they were redirected to the Karma Coffee Home Page, as we felt they are more likely to be returning customers.

Initialising user authentication using Django's inbuilt authentication was pretty easy, which was completed pretty much on day 1, which left us a great amount of time to focus on getting a consistant look throughout the website and free me up to aid the other team members with other jobs that required attention

After completing the Django User Authentication, we immediately decided to enter another authentication method, namely google. I did this using the AllAuth method. We chose the AllAuth method as is offerred us more scope for other authentication methods once google authentication was completed, in case we wanted to enter more, as opposed to the limited options presented by SocialAuth.

Settings.py
```
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email'
        ],
        'AUTH_PARAMS': {'access_type': 'online'}
    }
}
```
Login Template
```
        {% load socialaccount %}


        <a href="{% provider_login_url 'google'%}?next=/" class="btn btn-outline-secondary" style="width: 100%;">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="17" fill="black" class="bi bi-google google"
                viewBox="0 0 16 16" style="position: relative; top: -1px;">
                <path
                    d="M15.545 6.558a9.42 9.42 0 0 1 .139 1.626c0 2.434-.87 4.492-2.384 5.885h.002C11.978 15.292 10.158 16 8 16A8 8 0 1 1 8 0a7.689 7.689 0 0 1 5.352 2.082l-2.284 2.284A4.347 4.347 0 0 0 8 3.166c-2.087 0-3.86 1.408-4.492 3.304a4.792 4.792 0 0 0 0 3.063h.003c.635 1.893 2.405 3.301 4.492 3.301 1.078 0 2.004-.276 2.722-.764h-.003a3.702 3.702 0 0 0 1.599-2.431H8v-3.08h7.545z" />
            </svg>&nbsp;Google
        </a>
```

Some simple CSS in making our login and signup forms look much more polished and professional, and I was finished with my tasks by the end of day 3, transforming this:

![Screenshot 2023-08-08 at 14 31 18](https://github.com/rahulraikhy/karma-coffee/assets/121837375/3e36a096-0f42-4231-96bc-bd0f4ab70c78)

**to this:**

![Screenshot 2023-09-29 at 02 06 39](https://github.com/rahulraikhy/karma-coffee/assets/121837375/4485dbaf-0f3b-4b80-a40e-39b9f61eb20d)

```
<div class="d-flex align-items-center justify-content-center" style="min-height: 50vh;">
    <div class="col-lg-3 col-md-5 col-sm-8 text-center">

        <h1 class="h1 mb-3 mt-3 fw-normal">Create Account</h1>
        <p class="mb-3 fw-normal">Sign up, and become part of Karma!</p>

        <p class="red-text">{{ error_message }}</p>

        <form method="POST" action="{% url 'signup' %}" class="mb-3">
            {% csrf_token %}
            <div class="mb-3">
                <input type="text" name="username" class="form-control" placeholder="Username" required>
            </div>
            <div class="mb-3">
                <input type="email" name="email" class="form-control" placeholder="Email" required>
            </div>
            <div class="mb-3">
                <input type="password" name="password1" class="form-control" placeholder="Password" required>
            </div>
            <div class="mb-3">
                <input type="password" name="password2" class="form-control" placeholder="Confirm Password" required>
            </div>
            <button class="btn btn-dark btn-block" style="width: 100%;" type="submit">Sign Up</button>
        </form>

        <p class="text-center">Already have an account? <a href="{% url 'login' %}">Log In</a></p>

        <p>Or, continue with</p>

        {% load socialaccount %}


        <a href="{% provider_login_url 'google'%}?next=/" class="btn btn-outline-secondary" style="width: 100%;">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="17" fill="black" class="bi bi-google google"
                viewBox="0 0 16 16" style="position: relative; top: -1px;">
                <path
                    d="M15.545 6.558a9.42 9.42 0 0 1 .139 1.626c0 2.434-.87 4.492-2.384 5.885h.002C11.978 15.292 10.158 16 8 16A8 8 0 1 1 8 0a7.689 7.689 0 0 1 5.352 2.082l-2.284 2.284A4.347 4.347 0 0 0 8 3.166c-2.087 0-3.86 1.408-4.492 3.304a4.792 4.792 0 0 0 0 3.063h.003c.635 1.893 2.405 3.301 4.492 3.301 1.078 0 2.004-.276 2.722-.764h-.003a3.702 3.702 0 0 0 1.599-2.431H8v-3.08h7.545z" />
            </svg>&nbsp;Google
        </a>
    </div>
</div>
```
From day 4 onwards, I was free to contribute to the other team's needs, including creating content for the About, Home, and Index pages, aiding with implementation of the Stripe API (namely organising our group code in urls.py for the URL patterns, see below), and maintaining styling of the overall website.

```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(),
         name='create-checkout-session'),

    path('accounts/', include('allauth.urls')),
]
```

## Biggest Challenge

The toughest part of this project was to link multiple models developed by different engineers, and ensure minimal impact was had on other developers' code.

Mobile responsive design was especially difficult, going forward, we would implement mobile responsive designs first.

## User Feedback

- [x] Add a larger selection of products
- [x] Allow users to see their order history
- [x] Checkout and purchase as a guest
- [x] Add other authorisation methods
- [ ] Better mobile view

## Next Steps

- Add Google's Places API to demonstrate locations of coffee production sites
- Standardise CSS styling across the site
- Improve the mobile view

## Wins

- **Working as a team of multiple developers on a single project**. This was the first time we'd worked on a project using GitHub as a team. Something we're expected to do in the industry, we're really happy to have achieved a great team dynamic and be able to resolve issues quickly and efficiently! This was especially prevalent as one of our team members was in a different time zone, so gaining experience with this early, as more companies incorporate working methods like "follow the sun" and have more developers/engineers across different timezones, was fantastic!

- **Creating an app people want to use.** We wanted to make something that highlighted the topics we're learning, and satisfies the project brief, but also something that we'd use and others want to use. From user feedback it seems that we achieved this, and that feel's awesome.

## Mistakes / Bugs

- **Bootstrap trappings** Whilst bootstrap made implementing styling quicker, it made custom styling especially difficult, particularly when it came to mobile responsive design.

- **GitHub Push and Pull Requests** As a team, early on, it was difficult to stay out of each others code and resolve conflict issues, but with practise and time, this became significantly easier.

- **OAuth google** If a user is using multiple accounts with similar names, google OAuth can be blocked.

- **No Edit Functionality on Reviews** At this current time, a user can only create and delete a review, they are unable to.

## Key Learnings

- **GitHub deployment requires constant communication** Working as part of team requires good communication at the best of times, but when creating an app and/or website, constant communication is vital. When pushing new code with additional functionality upstream, and especially when working on functionality that may depend on other developers supporting.

- **Mobile responsiveness first**It became very difficult to go back and tailer our content to mobile views, as such, implementing this first next project would be beneficial.

- **Trust each other**For our first group project, we were all hesitant at the start to delegate too much or too little work to each other, but as the project went on, we understood each other's skills, that everyone could and would contribute to the project.

## The User Journey:

**Home Page**

- To start your coffee journey, click on the 'Coffee' option in the navigation bar.
- For a more personalized experience, sign up using your Google account to unlock special offers and features.

**Coffee Product Page**

- View All Coffee proudcts.
- Click 'Origin' to filter down the products by origins(Colombia, Ethiopia, Brazil, India).
- Click 'Origin' to filter down the products by roast level(Dark, Medium, Light).
- Click specific item to see more details.

**Product Detail Page**

- See the product image.
- Read the story behind the coffee blend and its origin and flavors.
- Add quantity and click 'Add to Cart' button to buy the coffee.
- Scroll down to explore customer reviews and ratings.

**Cart Page**

- See which products you put in your cart.
- Check quantity and price of the products you have in cart.
- Update the quantity and delete products if you need.
- You can check the total price and click 'Go to Checkout' button to purchase.

**Payment Page**

- Via Stripe, you can check your final order details and have your shipping/payment details set up.

**LogIn/Sign Up Page**

- You can create an account for our website.
- You can also sign up through OAuth with a popular platform, Google.

**Account Page**

- Check your order history.
- Update your account details.

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- CONTACT -->

## Contact

✨ Ross Simpson - [LinkedIn](https://www.linkedin.com/in/simpsonre/) - thisisrosssimpson@gmail.com / Project Link: [https://github.com/SimpsonRoss/karma-coffee](https://github.com/SimpsonRoss/karma-coffee)

🎉 Jihyeon Cha - [LinkedIn](https://www.linkedin.com/in/jihyeoncha/) - j.cha1708@gmail.com / Project Link: [https://github.com/chajiiiii/karma-coffee](https://github.com/chajiiiii/karma-coffee)

🎊 Rahul Raikhy - [LinkedIn](https://www.linkedin.com/in/rahul-raikhy-31ab62197//) - rlraikhy@gmail.com / Project Link: [https://github.com/rahulraikhy/karma-coffee](https://github.com/rahulraikhy/karma-coffee)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

These resources helped us greatly in the completion of our project.

- [Bootstrap](https://getbootstrap.com/)
- [Trello](https://trello.com/)
- [Photopea](https://www.photopea.com/)
- [Google 0Auth](https://cloud.google.com/endpoints/docs/openapi/authenticating-users-auth0)
- [EZ gif](https://ezgif.com/)

![karma-coffee](https://github.com/SimpsonRoss/karma-coffee/assets/93015253/aa5eea7d-9988-4ad3-b80d-760e32fb1f2e)
