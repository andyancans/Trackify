<h1 align='center'>Trackify</h1>

# About
 <p>Trackify is a portfolio tracker site with an emphasis on simplicity. You can add your personal holdings, and see the real-time value of your digital currencies. 
      <br>
      Key features include:
      <br>
      <ul>
        <li>Realtime Crypto Price tracking - the current price of crypto is shown and updated every minute on the home page, and is used to calculate total holdings.</li>
        <li>Ability to add / remove your own holdings through an add / remove holdings button, which the real-value is tracked accordingly to the amount you have.</li>
        <li>Future Planning: 
        <ul> 
        <li>
        The ability to import .csv files and add holdings according to the transactions in the csv.
        </li> 
        <li>
        Fetching crypto transactions and amounts from API keys directly from cryptocurrency exchanges.
        </li>
        <li>
        Tax calculations according to provided transactions to help simplify taxes with cryptocurrency.
        </li>
        </ul>
      </ul>
      Designed with simplicity and ease of use in mind, Trackify attempts to help every-day people track their personal holdings, and provide insight into how their portfolio is doing. 
      </p>

## Design
### Chosen color
<p>Default background colour: lightskyblue</p>
<p>Card header colour: Orange</p>
<p>Footer background colour: #343a40</p>

## Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [BootStrap](https://getbootstrap.com/)

## Frameworks, Libraries & Programs Used

[GitHub](https://github.com/) - Holds the repository of my project.

[Visual Studio Code](https://code.visualstudio.com/) - Primary IDE used to create this website.

[Heroku](https://www.heroku.com/) - Connected to the GitHub repository, Heroku is a cloud application platform used to deploy this project so the backend language can be utilised/tested. 

[Django](https://www.djangoproject.com/) - This framework was used to build the foundations of this project

[Bootstrap](https://getbootstrap.com/) - Used to quickly add design to my website, Bootstrap focuses on mobile first design meaning this website is responsive across multiple devices ans screen sizes. 

[Google Fonts](https://fonts.google.com/https://fonts.google.com/) - provide fonts for the website.

[Font Awesome](https://fontawesome.com/) -was used for icons.

[Balsamiq](https://balsamiq.com/) - was used to create site wireframes.

[Am I Responsive](http://ami.responsivedesign.is/) - to check if the site is responsive on different screen sizes.

[Beautify](https://www.jpkc.com/tools/beautify/) - was used to correct indentation issues and get rid of too much whitespace - HTML, CSS

## User Story Testing
<img src="assets\images\userstories.png">

## Bugs and Issues

<p>An issue that may be encountered is that the values of cryptocurrency would drop to 0 for anywhere between 15 seconds and 60 seconds. After countless hours of testing, trying fixes and all sorts, I've determined this is just an API-limitation, and can be fixed by upgrading to a less limiting cryptocurrency price API provider, or paying for access to a premium API that allows for far more requests, without much limitation. This can be seen when spam-refreshing a page as it requests data from the API multiple times, causing it to rate-limit. This, in theory, would be a very prevalent issue if multiple users are on the site, so in a commercial setting it would be far more suitable to go for a paid API.</p>

<p> Log error with heroku saying  NameError: name 'user_profile' is not defined, having googled the error we discovered it was either a spelling error or a ordering issue in the models.py file, having checked the spelling and moved the UserProfile model to the top the error message disappeared.</p>

<p>There was an issue with the total value calculation, but this was fixed using the decimal library.</p>

<p>There was also an issue where if the user would try to delete more than the account balance held, then it would throw an error and display '0' regardless of any value changes. This was fixed by making a check to see if the amount the user would like to remove is more than the balance, and if it is then throw a console error.</p>

# Deployment
This project was deployed using Github and Heroku.

## Github
To create a new repository I took the following steps:

- Logged into Github.
- Clicked over to the ‘repositories’ section.
- Clicked the green ‘new’ button. This takes you to the create new repository page.
- Once there under ‘repository template’ I chose the code institute template from the dropdown menu.
- I input a repository name then clicked the green ‘create repository button’ at the bottom of the page.
- Once created I opened the new repository and clicked the green ‘Gitpod’ button to create a workspace in Gitpod for editing.

## Django and Heroku 
- To get the Django framework installed and set up I followed the CodeInstitute's [Django Blog cheatsheet](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf)

# Credits
<h3></h3>
<li>StackOverFlow (a huge range of posts that helped a ton in the problem-solving process)</li>
<li>ChatGPT was used in some instances to explain any issues I was having, only after consulting primarily StackOverFlow.</li>
<li>Inspiration was taken from the below guides to create my login / register functionality, as well as set the ground-works for a future password reset feature.
<ul>
<li>https://www.crunchydata.com/blog/building-a-user-registration-form-with-djangos-built-in-authentication</li>
<li>https://learndjango.com/tutorials/django-login-and-logout-tutorial</li></li>
</ul>
</ul>
