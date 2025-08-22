# [movie_portal](https://movieportal-f2737f46bcb0.herokuapp.com)

Developer: EllisBale ([EllisBale](https://www.github.com/EllisBale))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/EllisBale/movie_portal)](https://www.github.com/EllisBale/movie_portal/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/EllisBale/movie_portal)](https://www.github.com/EllisBale/movie_portal/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/EllisBale/movie_portal)](https://www.github.com/EllisBale/movie_portal)
[![badge](https://img.shields.io/badge/deployment-Heroku-purple)](https://movieportal-f2737f46bcb0.herokuapp.com)


![screenshot](documentation/mockup.png)

source: [movie_portal amiresponsive](https://ui.dev/amiresponsive?url=https://movieportal-f2737f46bcb0.herokuapp.com)


## Project Overview


**MoviePortal** is a cinema booking platform that allows users to **explore films**, **view schedules**, **select seats**, **browse food items** and **book tickets** to watch films in the cinema. It was developed to provide **convenience**, **accessibility** and an **immersive experience** for cinema-goers across all devices.

The website also provides **cinema managers** with efficient tools to manage **film listings**, **schedules** and **bookings**.

The target audience would be for **casual and frequent moviegoers** of all different age groups, particularly **families and young adults**. The platform also works for **mobile users,** considering how many people have mobiles compared more than computers, making mobile users more likely to visit the site.

I chose to develop an **online cinema booking system** because I wanted to create something **practical and useful**, a **real-world application** that people can use every day. **Cinema-going** is a popular recreational activity, yet many users face **inconveniences** when it comes to **booking tickets, selecting seats** and **viewing available films**. By developing this project, I aim to **enhance the cinema experience** and make it more **accessible, convenient and user-friendly** for a wide audience.

Another reason I chose this project is that it gave me a great opportunity to work on both **front-end and back-end development**. I get to build an **interactive, visually engaging interface** for users while also handling the **back-end logic** needed to **manage film listings, bookings and seat availability**. Working on both sides of the application helps me understand how a **web project fits together**, from designing **smooth, intuitive interfaces** to making sure everything works **reliably behind the scenes**.



For this project, I researched popular cinema websites such as **Vue, Odeon and Cineworld**. When looking at these websites, I noticed a common trend in which all of the websites had a landing page with **hero carousel images**. They would include **current movies showing in cinemas** which would seem to grab a user's attention. It would benefit my website to have a **carousel hero images** on my landing page, as it will show the user what the website is about. Most of the websites I visited had a **dark theme** to it to match the **cinematic tone**, which makes it immersive. From this I will be using more **dark tones** for this project.


**Websites Visited:**

[Vue](https://www.myvue.com/)

[Cineworld](https://www.cineworld.co.uk/#/)

[Odeon](https://www.odeon.co.uk/)

## UX 

### The 5 Planes of UX


#### 1. Strategy

**Purpose** 

The project's purpose is to provide an **immersive** and **user-friendly** platform that allows users to **explore** and **discover films** with ease. The website enables users to **book cinema tickets online**, **select seats** and **choose a film** that is currently available. The website is designed to deliver the user a smooth experience across all devices and enhance **accessibility** for cinema-goers.

**Admin/Managers Purpose**

This platform also provides an administrative interface that allows cinema managers to:

- **Create new films** and add details such as **title, genre, duration, showtimes, posters and etc.**
- **Update existing films** to modify **schedules and film details.**
- **Delete films** that **no longer are showing in cinemas.**


**Business Goals**

- **Increase ticket sales.**
- **Enhance the user experience** by providing a **seamless** and **user-friendly interface**.
- **Encourage repeat visits** by allowing users to **discover new films and book them easily**.
- **Promote new releases** and **upcoming films** to keep users informed.
- **Improve film** and **showtime management** for cinema staff to maintain an **up-to-date schedule**.



#### 2. Scope


The following features below are categorized by priority on what the users needs and development goals are.


 **Must-Have Features:**

- User registration and login

- Film listing page

- Booking form with seat selection

- Admin/Manager panel to manage film listings

- Admin/Manager panel to view/manage bookings.


 **Should-Have Features:**

- Logout feature

- Admin/Manager edit menu items

- Confirmation of booking

- User can update profile information

- User can view menu (food & drinks)

- View upcoming movies



**Could-Have Features:**

- User can cancel booking

- User can filter movies by genre


**Content Requirements**

- **Film Management** - **Admin/Manager** can **create**, **update** and **delete films**.
- **Booking Management** - **Admin/Manager** can **view/manage bookings**; **users** can **select seats and complete bookings**.
- **User Account Features** - **Register, login/logout, update profile** and **view bookings**.
- **Booking confirmation** - **User** gets **notified** when a **booking is confirmed**.
- **Error Handling** - **404 page** for lost users.


#### 3. Structure

**Information Architecture**

**Navigation Menu**:

**User (Guests)**
- Links to Home, Films, Family, Food & Drink, login and register.

**Logged-in-user**
- Links to Home, Films, Family, Food & Drink, Booking and logout.

**Admin/Managers**


**User Flow**

1. Guest users browse films -> view film general information.
2. Gust users register for an account -> log in to access booking features.
3. Registered users select a film, choose schedule, choose seats and complete booking -> receive booking confirmation.
4. Admin/Managers create, update and manage film schedule, film information, film listings and seat availability.
5. Admin/Managers view and manage bookings -> ensure smooth cinema operations and user satisfaction. 



#### 4. Skeleton

**[Wireframes](#wireframes)** (see below)


#### 5. Surface

**Visual Design Elements**
- **[Colours](#colour-scheme)** (see below)
- **[Typography](#typography)** (see below)


### Colour Scheme

The website uses **dark colours**, primarily black to create an **immersive, cinematic atmosphere** that mirrors the experience of being inside a cinema. **Neon blue** is used as an accent colour to highlight **interactive elements**, helping them stand out clearly against the dark background. This not only enhances visual appeal but also guides the user by making it immediately obvious which elements are **clickable or interactive**.


I used [coolors.co](https://coolors.co/000000-1a1a2e-00bfff) to generate my colour palette.

- `#ffffff` Primary text.
- `#acb0b6` details heading text.
- `#00BFFF` accent colour for button borders, seat select and part of linear gradient of navbar.
- `#1a1a2e` Footer colour and part of linear gradient of the navbar.


![screenshot](docs/readme_imgs/colours.png)

### Typography


I used **three types of fonts** for this website. All the fonts I used are imported from **Google Fonts**. I felt the fonts worked well for each other as they give a balance of **readability and contrast**.

I have icons on my webite from [Font Awesome](https://fontawesome.com/). Icons can quickly communicate to the user without having to read a word. For example, I use icons in my footer for social media links and contact information, which makes the actions instantly recognisable. Having Font Awesome icons gives the site more of a professional and modern appearance.

- [Robot Condensed](https://fonts.google.com/specimen/Roboto+Condensed?query=Roboto) For the body text such as paragraphs.
- [Barlow Condensed](https://fonts.google.com/specimen/Barlow+Condensed?query=Barlow+c) For headings (h1 to h4). 
- [Montserrat](https://fonts.google.com/specimen/Montserrat) For every button text throughout the site.



## Wireframes


To follow best practice, wireframes were developed for mobile, tablet and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

| Page | Mobile | Tablet | Desktop |
| --- | --- | --- | --- |
| Home | ![screenshot](docs/wireframes/homemobile.png) | ![screenshot](documentation/wireframes/tablet-register.png) | ![screenshot](documentation/wireframes/desktop-register.png) |
| Films | ![screenshot](documentation/wireframes/mobile-login.png) | ![screenshot](documentation/wireframes/tablet-login.png) | ![screenshot](documentation/wireframes/desktop-login.png) |
| Family | ![screenshot](documentation/wireframes/mobile-home.png) | ![screenshot](documentation/wireframes/tablet-home.png) | ![screenshot](documentation/wireframes/desktop-home.png) |
| Food & Drink | ![screenshot](documentation/wireframes/mobile-add-blog.png) | ![screenshot](documentation/wireframes/tablet-add-blog.png) | ![screenshot](documentation/wireframes/desktop-add-blog.png) |
| Booking | ![screenshot](documentation/wireframes/mobile-edit-blog.png) | ![screenshot](documentation/wireframes/tablet-edit-blog.png) | ![screenshot](documentation/wireframes/desktop-register.png) |
| Register | ![screenshot](documentation/wireframes/mobile-blog-post.png) | ![screenshot](documentation/wireframes/tablet-blog-post.png) | ![screenshot](documentation/wireframes/desktop-login.png) |
| Login | ![screenshot](documentation/wireframes/mobile-404.png) | ![screenshot](documentation/wireframes/tablet-404.png) | ![screenshot](documentation/wireframes/desktop-404.png) |
| Films.detail | ![screenshot](documentation/wireframes/mobile-register.png) | ![screenshot](documentation/wireframes/tablet-register.png) | ![screenshot](documentation/wireframes/desktop-register.png) |
| Booking.schedule | ![screenshot](documentation/wireframes/mobile-register.png) | ![screenshot](documentation/wireframes/tablet-register.png) | ![screenshot](documentation/wireframes/desktop-register.png) |
| Booking.seats | ![screenshot](documentation/wireframes/mobile-register.png) | ![screenshot](documentation/wireframes/tablet-register.png) | ![screenshot](documentation/wireframes/desktop-register.png) |
| Booking.select_film | ![screenshot](documentation/wireframes/mobile-register.png) | ![screenshot](documentation/wireframes/tablet-register.png) | ![screenshot](documentation/wireframes/desktop-register.png) |



## User Stories


| Target | Expectation | Outcome |
| --- | --- | --- |
| As a User | I want to be able to make an account,| so that I can view my bookings and make bookings. |
| As a User | I want to be able to view a selection of films, | so that I have a variety of films to choose to watch. |
| As a User | When visting the home page, I want to feel immersive and engaging,  | so that I can get excited about the movies and cinema atmosphere |
| As a User | I want to view upcoming movies, | so I can decide to make a booking. |
| As a User | I want to be able to view drinks and snacks, | so that I know what snacks the cinema offers. |
| As a User | I want to receive confirmation of booking, | so that I know the booking went through. |
| As a logged in User | I want to be able to make bookings for films,  |  so that I can make a booking from home. |
| As a logged in User | I want to be able to view available seats, |  so that I decide If I want to book that seat. |
| As a logged in User | I want to change my profile information, | so that I can change name, email address, phone number and password. |
| As a logged in User | I want to be able to cancel a booking, | so that in case plans change. |
| As a Admin/Manager | I want to be able to view users bookings, | so that I can remove bookings, see how busy cinema gets and verify seat numbers. |
| As a Admin/Manager  | I want to be able to edit, delete and add films from the lists, | so that I can change movie image, change description and change movie name. |
| As a Admin/Manager | I want to be able to update the menu, | so that I can add new snacks/drinks to the menu and remove items the cinema no longer sells. |



## Features 


### Existing Features



| Feature | Notes | Screenshot |
| --- | --- | --- |
| Register | Authentication is handled by allauth, allowing users to register accounts. I have added a custom form to it, so that I can add first name and last name. | ![screenshot](documentation/features/register.png) |
| Login | Authentication is handled by allauth, allowing users to log in to their existing accounts. | ![screenshot](documentation/features/login.png) |
| Logout | Authentication is handled by allauth, allowing users to log out of their accounts. | ![screenshot](documentation/features/logout.png) |
| Film Listings | Displays all current films with title and posters. The film listing can be found on films page, homepage and Family page. This feature is enabled for all the user types. The posters contains a hover effect, the hover effect makes the other posters scale down in size slightly and adds a slight greyscale to it. This hover effect lets the user focus on the poster they are hovered over.  | ![screenshot](documentation/features/blog-list.png) |
| View Film details | Users can view more information about a film if they click on the films poster or title. When the user has clicked on a film, they can view information such as genre, cast, description, runtime and release date. The films detail page includes a book now button so that logged-in-users can book. | ![screenshot](documentation/features/blog-list.png) |
| Seat booking | Logged-in users can select their preferred seats from an interactive seating layout. Booked seats are clearly marked as unavailable, while available seats can be selected individually or in groups. Chosen seats highlight in blue and a hover effect helps users see which seat they are about to pick. This gives users a clear, visual and intuitive way to secure their spots. Once the user has selected a seat/seats and finish booking, their seats will be disabled so other users can't book them and saved to the database. | ![screenshot](documentation/features/register.png) |
| Navigation bar | A fully responsive navigation bar built with Bootstrap. On mobile and tablet devices, it collapses into a burger menu for easier access. The navbar is present on every page, ensuring consistent and intuitive site navigation. It includes links to **Home, Films, Family, Food & Drink, Booking, Login, Register and Logout**. The **Booking** link is only visible to logged-in users, making the experience tailored to user status. The navbar contains the companies logo which remains to left at all times.  | ![screenshot](documentation/features/register.png) |
| Carousel (Hero Section)| Admin/Managers can add any film to the hero section. Having hero carousel with films engages users with visuals as well as highlighting current releases. The carousel moves onto the next image after 7 seconds if the user isn't hovered of the element. This is good for users so that if their mouse is hovered near the Book Now button, it will stop moving so the user can click on it. The carousel is on the homepage, films and family page. The book now button will send the user to the login page if they are not logged in, and the schedules page if they are logged in. | ![screenshot](documentation/features/register.png) |
| Footer | The footer contains opening hours, social media pages, contact details and company logo. The footer is included on everypage. Font Awesome icons are added to the footer to show the user what the links are for without having to read anything. | ![screenshot](documentation/features/register.png) |
| Scroll-to-Top Button | This button allows users to quickly return to the top of the page. This helps save time because the user doesn't have to manually scroll to the top of the page if it is a long page. This button is blocked on some pages that don't require it such as the login in page.   | ![screenshot](documentation/features/register.png) |
| Schedule Page | Logged-in users can view a schedule of available times for the film they have chosen.  | ![screenshot](documentation/features/register.png) |
| Food & Drink Page | All users can view the cinemas food & drink items. Each item displays an image, name and description giving visitors a clear idea of what's available before they arrive. Users can plan what snack they want in advance because they know what the cinema others. | ![screenshot](documentation/features/register.png) |



### Future Features





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
| [![badge](https://img.shields.io/badge/Neon-grey?logo=neondatabase&logoColor=00E599)](https://neon.tech) | Serverless PostgreSQL database hosting. |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) | Online static file storage. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
| [![badge](https://img.shields.io/badge/Balsamiq-grey?logo=barmenia&logoColor=CE0908)](https://balsamiq.com/wireframes) | Creating wireframes. |
| [![badge](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) | Icons. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |
| [![badge](https://img.shields.io/badge/Mermaid-grey?logo=mermaid&logoColor=FF3670)](https://mermaid.live) | Generate an interactive diagram for the data/schema. |
| [![badge](https://img.shields.io/badge/W3Schools-grey?logo=w3schools&logoColor=04AA6D)](https://www.w3schools.com) | Tutorials/Reference Guide |




## Project planning method

This project was developed using an **Agile-inspired** workflow, with tasks prioritised using the **MoSCoW method**. This method allows me to categorise features into **Must-have**, **Should-have** and **Could-have**. Using the MoSCoW method for user stories ensures that I have prioritisation on core functionality for users.

I used **Github project board** to track my progress throughout the project. In the project board I have columns for **To Do**, **In Progress** and **Done**. This allowed me to monitor tasks I was doing easier.

The planning process was guided by user stories written for different types of users. The user type included **visitors**, **logged-in users** and **admin/managers**. Each user story is linked to a feature, implemented in code and tested to maintain usability and accessibility standards.

This method ensured the project stayed **focused**, **adaptable** and aligned with the needs of the target audience.











---

## Testing



### Code Validation


### Lighthouse Testing


### Browser Compatibility 




### Functional Testing


### User Story Testing


### Bugs & Fixes

<details>
<summary> Procfile issue </summary>  

Fixed an issue where my Procfile was showing the wrong name.
This happened because I copied the Procfile from the Codestar project to this project.        
</details>  


<details>
<summary>  CSS not showing up fix  </summary>

Fixed a bug that was not allowing me to see changes to my CSS.
I originally thought that bootstrap was the issue, but then realised my debug mode was on false.  
</details>


<details>
<summary> Heroku not deploying fix </summary>

 Issue with server 500 error; the server deployed on Heroku but didn't show up.
 I fixed this by adding the cloudinary to config var on the Heroku settings page.
</details>


<details>
<summary> Hero carousel not moving on Firefox browser</summary>

Fixed issue with hero carousel not automatically moving on Firefox. I fixed this by adding a timer with  `data-bs-interval="7000"`, which
gives 7 seconds to move between each hero image. 
</details>  


<details>
<summary> Hero carousel not moving when mouse hovers over</summary>

Fixed an issue in which `data-bs-touch="true"` was being activated even if the user wasn't hovering over the carousel. This happened because of the height of the `.carousel-inner` class, which was overlapping.

Before, my code was:
`.carousel-inner { height: 85vh !important; }`

The height was set to a fixed value, so I changed it to:
`.carousel-inner, .carousel-item { height: auto; }`

I also added padding to:
`.carousel-item .container { padding-top: 1rem; padding-bottom: 2rem; }`
</details>  




---

## Deployment


### Heroku


### Enviroment Setup


### Github


---

## Security Features


---

## Credits

### Images

 Menu Images Used:

- [Juices](https://pixabay.com/illustrations/ai-generated-drink-juice-8527256/) By myshoun
- [Chocolate](https://pixabay.com/illustrations/chocolate-flavor-cocoa-close-up-8919274/) By u_he12qucmwq
- [Ice Cream](https://pixabay.com/illustrations/ai-generated-ice-cream-food-8867435/) By Manik
- [Candy](https://pixabay.com/illustrations/sweets-chocolate-candy-lollipop-7705343/)
- [Hotdog](https://pixabay.com/illustrations/hot-dog-food-sandwich-bread-fries-7605754/) By Hansuan_Fabregas
- [Popcorn](https://pixabay.com/illustrations/food-snack-popcorn-container-7908758/) By Secoura
- [Soft Drinks](https://pixabay.com/illustrations/ai-generated-soda-drink-cola-coke-8947090/) By rosiproductorseguros
- [Coffee Drink](https://pixabay.com/illustrations/disposable-coffee-drink-water-8748932/) By Claudio-Duart-Designer

Film Images Used:

- 
- 
- 

**Sites Used**
- [Balsamiq wireframes:](https://balsamiq.com/) Used to create the wireframes for the websites layout and structure
- [Google Fonts:](https://fonts.google.com/) Used to import fonts for my project
- [Pixabay:](https://pixabay.com/) Used for downloading copyright free images to use for my website
- [capitalizemytitle:](https://capitalizemytitle.com/) Used for creating the description of movies in this project
- [name-generator:](https://www.name-generator.org.uk/) Used for generating the names for the cast in the films.
- [TempMail:](https://temp-mail.org/) Used for creating temporary emails for testing account signup/login.


