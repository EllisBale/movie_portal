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
| Home | ![screenshot](docs/wireframes/home_mobile.png) | ![screenshot](docs/wireframes/home_tablet.png) | ![screenshot](docs/wireframes/home_desktop.png) |
| Films | ![screenshot](docs/wireframes/films_mobile.png) | ![screenshot](docs/wireframes/films_tablet.png) | ![screenshot](docs/wireframes/films_desktop.png) |
| Films Details | ![screenshot](docs/wireframes/films_detail_mobile.png) | ![screenshot](docs/wireframes/films_detail_tablet.png) | ![screenshot](docs/wireframes/films_detail_desktop.png) |
| Family | ![screenshot](docs/wireframes/family_mobile.png) | ![screenshot](docs/wireframes/family_tablet.png) | ![screenshot](docs/wireframes/family_desktop.png) |
| Food & Drink | ![screenshot](docs/wireframes/menu_mobile.png) | ![screenshot](docs/wireframes/menu_tablet.png) | ![screenshot](docs/wireframes/menu_desktop.png) |
| Booking Choose film | ![screenshot](docs/wireframes/choose_film_mobile.png) | ![screenshot](docs/wireframes/choose_film_tablet.png) | ![screenshot](docs/wireframes/choose_film_desktop.png) |
| Booking Schedule | ![screenshot](docs/wireframes/schedules_mobile.png) | ![screenshot](docs/wireframes/schedules_tablet.png) | ![screenshot](docs/wireframes/schedules_desktop.png) |
| Booking Seats | ![screenshot](docs/wireframes/seats_mobile.png) | ![screenshot](docs/wireframes/seats_tablet.png) | ![screenshot](docs/wireframes/seats_desktop.png) |
| User Bookings | ![screenshot](docs/wireframes/user_bookings_mobile.png) | ![screenshot](docs/wireframes/user_bookings_tablet.png) | ![screenshot](docs/wireframes/user_bookings_desktop.png) |
| Login | ![screenshot](docs/wireframes/login_mobile.png) | ![screenshot](docs/wireframes/login_tablet.png) | ![screenshot](docs/wireframes/login_desktop.png) |
| Register | ![screenshot](docs/wireframes/signup_mobile.png) | ![screenshot](docs/wireframes/signup_tablet.png) | ![screenshot](docs/wireframes/signup_desktop.png) |




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
| Register | Authentication is handled by allauth, allowing users to register accounts. I have added a custom form to it, so that I can add first name and last name. | ![screenshot](docs/readme_imgs/register_page.png) |
| Login | Authentication is handled by allauth, allowing users to log in to their existing accounts. | ![screenshot](docs/readme_imgs/login_page.png) |
| Logout | Authentication is handled by allauth, allowing users to log out of their accounts. | ![screenshot](docs/readme_imgs/logout_page.png) |
| Home page | The hompage displays a list of current popular movies that are currently available at the cinema. Each film uses a reusable `film_poster_layout.html` partial for consistency in design and layout. Users can view more details about the film by clicking on the poster, carousel and text. Underneath the popular movie display, it displays coming soon movies. These are movies that are not listed in the film list because they aren't showing in cinema yet. The coming soon movies uses the `film_poster_layout.html` partial for consistency. Users are able to click on the coming soon movies to view more details about them. The difference between the `films_detail.html` for coming soon movies is that the button is removed to show users you can't book them.   | ![screenshot](docs/readme_imgs/films_page.png) |
| Film Listings | Displays all current films with title and posters. The film listing can be found on films page, homepage and Family page. This feature is enabled for all the user types. The posters contains a hover effect, the hover effect makes the other posters scale down in size slightly and adds a slight greyscale to it. This hover effect lets the user focus on the poster they are hovered over. The layout used for movies is from the `film_poster_layout.html` which made it useful for using it for other pages.   | ![screenshot](docs/readme_imgs/films_page.png) |
| View Film details | Users can view more information about a film if they click on the films poster or title. When the user has clicked on a film, they can view information such as genre, cast, description, runtime and release date. The films detail page includes a book now button so that logged-in-users can book. If you are a user that is not logged in and clicks "Book Now", they will be sent to the login page. Schedules are added at the bottom of the details page to show all user types what schedules are on for that film. | ![screenshot](docs/readme_imgs/films_detail_page.png) |
| Seat booking | Logged-in users can select their preferred seats from an interactive seating layout. Booked seats are clearly marked as unavailable, while available seats can be selected individually or in groups. Chosen seats highlight in blue and a hover effect helps users see which seat they are about to pick. This gives users a clear, visual and intuitive way to secure their spots. Once the user has selected the seat/seats and finish booking, their seats will be disabled so other users can't book them and it will be saved to the database. | ![screenshot](docs/readme_imgs/seats_page.png) |
| Navigation bar | A fully responsive navigation bar built with Bootstrap. On mobile and tablet devices, it collapses into a burger menu for easier access. The navbar is present on every page, ensuring consistent and intuitive site navigation. It includes links to **Home, Films, Family, Food & Drink, Booking, My Booking, Manage, Login, Register and Logout**. The **Booking** link is only visible to logged-in users, making the experience tailored to user status. The navbar contains the companies logo which remains top left at all times.  | ![screenshot](docs/readme_imgs/navbar.png) |
| Carousel (Hero Section)| Admin/Managers can add any film to the hero section. Having hero carousel with films engages users with visuals as well as highlighting current releases. The carousel moves onto the next image after 7 seconds if the user isn't hovered of the element. This is good for users so that if their mouse is hovered near the Book Now button, it will stop moving so the user can click on it. The carousel is on the homepage, films and family page. The book now button will send the user to the login page if they are not logged in and the schedules page if they are logged in. | ![screenshot](docs/readme_imgs/carousel.png) |
| Footer | The footer contains opening hours, social media pages, contact details, location and company logo. The footer is included on everypage. Font Awesome icons are added to the footer to show the user what the links are for without having to read anything. The links in the footer contain a hover effect, the same as the navbar text. | ![screenshot](docs/readme_imgs/footer.png) |
| Scroll-to-Top Button | This button allows users to quickly return to the top of the page. This helps save time because the user doesn't have to manually scroll to the top of the page if it is a long page. This button is blocked on some pages that don't require it such as the login in page. The button styling is the same as other buttons on the page to show that it is functional.   | ![screenshot](docs/readme_imgs/back_to_top_button.png) |
| Select film page | This page is only available for logged in users and its the first step in booking a film to watch.    | ![screenshot](docs/readme_imgs/select_film_page.png) |
| Schedule Page | Logged-in users can view a schedule of available times for the film they have chosen.  | ![screenshot](docs/readme_imgs/schedule_page.png) |
| Food & Drink Page | All users can view the cinemas food & drink items. Each item displays an image, name and description giving visitors a clear idea of what's available before they arrive. Users can plan what snack they want in advance because they know what the cinema others. | ![screenshot](docs/readme_imgs/food_drink_page.png) |
| Family Page | This page contains only family films which is sorted out by admin/staff. The hero carousel on this page only displays hero images of family films, which helps with audience relevance since the page is dedicated to family-friendly content.  | ![screenshot](docs/readme_imgs/family_page.png) |
| Promotional (call-to-action) section | I have this type of section for the homepage and the family page. The homepage features a "Films For The Family!" section with two buttons: "Sign Up" and "View Films". This section is only displayed to users who are not logged in. Its purpose is to encourage account creation by making it clear that an account is required to book films.
For logged-in users, this section is replaced with a different one that promotes film booking directly, providing a more relevant experience based on the user’s status. Lastly, the third section is visible to all users and is located on the family page. This section promotes the Food & Drink page, encouraging visitors to explore available snacks and meals for their cinema visit. | ![screenshot](docs/readme_imgs/family_section.png) ![screenshot](docs/readme_imgs/book_section.png) ![screenshot](docs/readme_imgs/menu_section.png)  |
| My Bookings page | My Bookings page allows logged in users to view their bookings and be able to delete/cancel bookings they want to remove by pressing the delete button to the right of the booking text. The delete button will give the user a warning just incase misclicks happen on the page. | ![screenshot](docs/readme_imgs/my_bookings_page.png) |
| Admin Manage navbar dropdown | The Manage navbar dropdown links only appear when the user is a staff/admin user. This navabar dropdown was made for staff to find the CRUD functions easier for different pages. | ![screenshot](docs/readme_imgs/manage_dropdown.png) |
| Admin manage films list  | This page is for staff/admin only and it allows for CRUD function for films. Staff/admin can edit a film through a form of any movie that is added. Staff/admin can edit title, descripition, poster image, hero image, cast, genre, release date and duration. This form also includes checkboxes for popular, coming soon, family and hero image which adds them to specific sections or pages. Staff/admin can add films with the same form they use for film edit as well as delete films. | ![screenshot](docs/readme_imgs/manage_films.png) ![screenshot](docs/readme_imgs/film_form.png)  |
| Admin manage schedule list  | This page is for staff/admin only and it allows for adding, viewing and deleting schedules. When user clicks "Add schedule" it will open up a create schedule form containing film, days of week, slot, specific date and specific time. I have made it so it is on a weekly schedule to make it easier and quicker to add schedules.  | ![screenshot](docs/readme_imgs/manage_schedule.png) ![screenshot](docs/readme_imgs/schedule_form.png)  |
| Admin manage booking list | This page is for staff/admin only and it allows for viewing, editing and deleting bookings. The edit booking form allows staff/admins to edit film schedule, seat and user. | ![screenshot](docs/readme_imgs/booking_list.png) ![screenshot](docs/readme_imgs/booking_form.png)  |
| Admin manage user list | This page is for staff/admin only and it allows for viewing, editing and deleting users. Staff/admins can change first name, last name, email address and staff status.  | ![screenshot](docs/readme_imgs/manage_booking.png) ![screenshot](docs/readme_imgs/user_form.png)  |











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



## Database Design


### Data Model

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models. Understanding the relationships between different tables can save time later in the project.


![screenshot](docs/readme_imgs/erd.png)


I have used `Mermaid` to generate an interactive ERD of my project.

```mermaid
erDiagram
    GENRE ||--o{ FILM : has
    FILM ||--o{ FILMSCHEDULE : scheduled_in
    SHOWTIMESLOT ||--o{ FILMSCHEDULE : assigned_to
    FILMSCHEDULE ||--o{ BOOKING : reserved_in
    USER ||--o{ BOOKING : makes
    SEAT ||--o{ BOOKING : assigned
    MENU {
        int id PK
        varchar name
        text description
        varchar image
        varchar category
    }
    GENRE {
        int id PK
        varchar name
    }
    FILM {
        int id PK
        varchar title
        text description
        varchar poster
        text cast
        date release_date
        int duration
        bool is_popular
        bool is_coming_soon
        bool is_family
        bool is_hero_image
        int genre_id FK
    }
    SHOWTIMESLOT {
        int id PK
        time start_time
    }
    FILMSCHEDULE {
        int id PK
        int film_id FK
        int days_of_week
        int slot_id FK
        date specific_date
        time specific_time
    }
    SEAT {
        int id PK
        varchar row
        int number
    }
    BOOKING {
        int id PK
        int film_schedule_id FK
        int seat_id FK
        int user_id FK
        datetime booked_at
    }
```

source: [Mermaid](https://mermaid.live/edit#pako:eNqVVNtu4jAQ_ZXIzxQBCRDyttumLeK2akArrZAiNxmCRWxHttOWpfz7OgkBQtiK5iHyzJwzMz4ee4cCHgJyEIgHgiOB6ZIZ-ntypy-u8fl5d8d3xuNwPDEcY41lEczts5h3_-w-LMauxshgDWEaQ-gTVoC959nv-XDieuPZ_D8kLCWJmOYofipwjB84P2ez0XD6pOECJIi3sxILz32pwyjewKFhz_0xrwPKsgVm4k4Xxq5YZx9hyiCh8Wt0cr1hEayxMBimcPIq-FBGCDIQJFGEszqeUBxB3R1gBREX2yKyPxf-u33szw7mNq4iKv7WJhIuFYgLRoClOrlCvSF9OjFgCX5mVDsJU4GruV85jw0i_YQnaYxFPRBwSljkS36NtcKUxNu6fw2C-xeaZ_UjYAJ8rcfjqKJaZUK_Vk8RCoZUWCg_W9bEPw7t12ky14rE9LyZo0p4K32-8t8BNtWIjLm6ZOSSywQCsiLBheZFs2Ws1m9-KW4bFsHfqziW0tdyGA7pynt1487Lh-KaBBKwuuZP9b2_JkC-UX36G_0m4MM87lEDRYKEyFEihQaiICjOTJQ3uERqDVoQ5OhliMVmiZYs4ySY_eGcljTB02iNnBWOpbbSJCt3eCiPEGAhiHueMoUcq23mOZCzQx_IMc1uc9Drdzu9dqvfzX4NtEVOz2q2LLNndy3b7ti2Ze4b6G9etd1sm_3BwO50TLNl9S2720A4VdzbsqAouP8Hkkislg)




## Agile Development Process

This project was developed using an **Agile-inspired** workflow, with tasks prioritised using the **MoSCoW method**. This method allows me to categorise features into **Must-have**, **Should-have** and **Could-have**. Using the MoSCoW method for user stories ensures that I have prioritisation on core functionality for users.

I used **Github project board** to track my progress throughout the project. In the project board I have columns for **To Do**, **In Progress** and **Done**. This allowed me to monitor tasks I was doing easier.

The planning process was guided by user stories written for different types of users. The user type included **visitors**, **logged-in users** and **admin/managers**. Each user story is linked to a feature, implemented in code and tested to maintain usability and accessibility standards.

This method ensured the project stayed **focused**, **adaptable** and aligned with the needs of the target audience.




| Link | Screenshot |
| --- | --- |
| [![GitHub issues](https://img.shields.io/github/issues-search/EllisBale/movie_portal?query=is%3Aissue%20is%3Aopen%20-label%3Abug&label=Open%20Issues&color=yellow)](https://www.github.com/EllisBale/movie_portal/issues?q=is%3Aissue%20is%3Aopen%20-label%3Abug) | ![screenshot](documentation/gh-issues-open.png) |
| [![GitHub closed issues](https://img.shields.io/github/issues-search/EllisBale/movie_portal?query=is%3Aissue%20is%3Aclosed%20-label%3Abug&label=Closed%20Issues&color=green)](https://www.github.com/EllisBale/movie_portal/issues?q=is%3Aissue%20is%3Aclosed%20-label%3Abug) | ![screenshot](documentation/gh-issues-closed.png) |




## Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.



## Deployment

The live deployed application can be found deployed on [Heroku](https://movieportal-f2737f46bcb0.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.


Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables to match your private `env.py` file.


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

To obtain your own **Cloudinary API key**, create an account and log in.

- For "Primary Interest", you can choose **Programmable Media for image and video API**.
- *Optional*: edit your assigned cloud name to something more memorable.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the leading `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.
    - `cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5)`
- This will go into your own `env.py` file, and Heroku Config Vars, using the **key** of `CLOUDINARY_URL`.


### PostgreSQL (via Neon)

This project uses [Neon PostgrSQL Database](https://neon.com/) for the Relational Database with Django.

To obtain your **Neon PostgreSQL Databse**, I followed these steps:

- Go to [Neon](https://neon.com/) to create a **free account**.
- From your **dashboard**, create a **new project**.
- Once created, Neon will provide you with a **connection string**. It will look something like this: `postgresql://<username>:<password>@<host>/<dbname>`
- Add it to your local **`env.py`** file: ` os.environ.setdefault( "DATABASE_URL", "postgresql://<username>:<password>@<host>/<dbname>"`
- In Heroku, go Settings -> Config Vars and add the same string under the **key** `DATABASE_URL`.



### WhiteNoise

This project uses the [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) to aid with **static files** temporarily hosted on the live **Heroku** site.

To include **WhiteNoise** in your own projects:

- **Install** the latest **WhiteNoise** package:
    - `pip install whitenoise`
- **Update** the **`requirements.txt`** file with the newly installed package:
    - `pip freeze --local > requirements.txt`
- **Edit** your **`settings.py`** file and add **WhiteNoise** to the **`MIDDLEWARE`** list, above all other middleware (apart from Django’s **"SecurityMiddleware"**):

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

1. Go to the [GitHub repository](https://www.github.com/EllisBale/movie_portal).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	- `git clone https://www.github.com/EllisBale/movie_portal.git`
7. Press "Enter" to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://www.github.com/EllisBale/movie_portal)

**Please Note**: in order to directly open the project in Gitpod, you should have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).



#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/EllisBale/movie_portal).
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
| [Python Tutor](https://pythontutor.com) | Additional Python help |
| [ChatGPT](https://chatgpt.com) | Help with code logic, explanations and some movie posters. |
| [Pixabay:](https://pixabay.com/) | Used for downloading copyright free images to use for my website.|
| [capitalizemytitle:](https://capitalizemytitle.com/) | Used for creating the description of movies in this project.|
| [name-generator:](https://www.name-generator.org.uk/) | Used for generating the names for the cast in the films.|
| [TempMail:](https://temp-mail.org/) | Used for creating temporary emails for testing account signup/login.|


### Media

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




### Acknowledgements


- I would like to thank my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN) for the support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) Tutor Team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and impostor syndrome.




