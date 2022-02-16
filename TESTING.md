
## <ins>**Testing**</ins>

---

**<details><summary>Table of contents</summary>**
  - [Code validation](#code-validation)
  - [User story tests](#user-story-tests)
  - [Feature test scripts](#feature-test-scripts)
  - [Known issues and disclaimers](#known-issues-and-disclaimers)
  - [Bugs](#bugs)
</details>

---

## &rarr; **Code validation**
- Tested for valid HTML code using [w3 validator](https://validator.w3.org/nu/)<br>
<img src="media/readme_files/html-validation.png" width="400px" height="270px" alt="Validation tests - HTML">

- Tested for valid CSS code using [Jigsaw validator](https://jigsaw.w3.org/css-validator/)<br>
<img src="media/readme_files/css-validation.png" width="400px" height="150px" alt="Validation tests - CSS"><br>

- Continuous validation of python code using installed plugin [Pylance](https://github.com/microsoft/pylance-release). Additionally the website [pep8online](http://pep8online.com/) was used to check each python code file.

---

## &rarr; **User story tests**
|User Story ID|Test actions|
|-|-|
|1|- Click on the 'Plants' menu item<br>- Confirm you are taken to the Plants overview page|
|2|- Click on the 'Plants' menu item<br>- Click on an individual plant<br>- Confirm the page for the plant opens<br>- Confirm you can click on the plant menu item again to be taken back|
|3|- Click on the 'Plants' menu item<br>- Click on the 'Categories' button on the top right<br>- Confirm a list of all categories shows|
|4|- Click on the 'Suggestions' menu item<br>- Confirm you are taken to the suggestions page|
|5|- Click on the 'Suggestions' menu item<br>- Confirm you are taken to the suggestions page where you can easily see which one is upvoted the most|
|6|- Click on the 'Plants' menu item<br>- Fill in a searchterm in the searchbar and click the magnifying glass icon<br>- Confirm plants that match the searched term show up|
|7|- Click on the 'Register' menu item<br>- Fill in the required fields in the form shown, and click 'Sign me up'<br>- Confirm an account is created by logging into your account|
|8|- When logged into the website, click on the 'Profile' menu item<br>- Confirm you are taken to your profile page|
|9|- When logged into the website, click on the 'Profile' menu item<br>- Make changes to the displayed form and click 'Save profile'<br>- Confirm your profile changes where saved by revisiting the profile page or visiting the Checkout page|
|10|- Click on the Shopping cart icon in the top right of the website<br>- Confirm you are taken to the shopping cart, where you can view all plants currently in your shoppingcart|
|11|- Click on the Shopping cart icon in the top right of the website<br>- Adjust the number of any one plant, by click on the plus or minus signs<br>- Further test this by deleting a plant<br>- Confirm the number is adjusted or the plant is deleted entirely|
|12|- Click on the 'Plants' menu item<br>- Select a plant to purchase, and click on it<br>- Click on 'Add to cart'<br>- Click on 'Checkout'<br>- Either fill in the form, or use the prefilled data<br>- Click on 'Confirm Purchase'<br>- Confirm you receive a confirmation email |


---


## &rarr; **Feature test scripts**
For testing, 2 device types are defined:
- Mobile
    * Any device with a horizontal screen width **smaller** then 567px. This can also be achieved using browser developer tools.
- Mobile+
    * Any device with a horizontal screen width **larger** then 567px

|1|Register|
|-|-|
- Click on the 'Register' button in the top menu
- Fill in the fields in the form and click 'Sign Up'
- Confirm a message appears confirming you have signed up, and saying there was an email sent to you
- Confirm you received an email
- Click on the link in the email
- Confirm you can login to the site (see steps below)

|2|Login|
|-|-|
- Click on the 'Login' button in the top menu
- Fill in your username and password and click 'Sign In'
- Confirm you are taken to the home screen, and a message appears saying you are logged in succesfully

|3|Search for a plant|
|-|-|
- Click on the 'Plants' button in the top menu
- Click on the input field next to the magnifying glass where it says 'Search...'
- Enter a search phrase and press enter or click on the magnifying glass
- Confirm plants containing your searchphrase are showed (provided they exist on the site)

|4|Filter by category|
|-|-|
- Click on the 'Plants' button in the top menu
- Click on the 'Categories' button to the far right of the search area
- Click on any category
- Confirm only the plants from that category are shown

|5|Change amount in shoppingcart|
|-|-|
- Add one or more plants to your shoppingcart
- Click on the shoppingcart icon on the top right
- Click on either the plus or minus sign in a line
- Confirm the amount is updated, as are the line total and subtotal

|6|Make a purchase|
|-|-|
- Add one or more plants to your shoppingcart
- Click on the shoppingcart icon on the top right
- Click on the 'Checkout' button on the bottom right
- Fill in the Personal, Shipping and Billing information (dummy, senseless information may be used)
- Fill in 4242 4242 4242 4242 as the card number, with 04 / 24 as the expiry date, 242 as the CVC code and 42424 as the ZIP code
- Click 'Confirm purchase'
- Confirm the button is disabled
- Confirm that after a few seconds you are taken to the home screen, and a green message is displayed confirming a succesfull payment

|7|Edit address information|
|-|-|
- Log into the website
- Click on the 'Profile' button in the top menu
- Edit any field in the form
- Click on the 'Save Profile' button at the bottom of the form
- Confirm a green message at the top is shown confirming the profile was updated
- Reload the page, or proceed to the checkout page
- Confirm the form now contains the updated values

|8|Make a plant suggestion|
|-|-|
- Log into the website
- Click on the 'Suggestions' button in the top menu
- Click on 'Share your plant suggestion!'
- Fill in the required fields, and click on 'Submit'
- Confirm a message is displayed confirming a succesfull suggestion was made
- Confirm the suggestion is now listed on the 'Suggestions' page

---

## &rarr; **Known issues and disclaimers**
- There are a number of PEP8 compliancy errors concerning the length of some lines. So far I've been unable to make these shorter. This will be done in a future release. The files concerned are:
  - checkout/webhooks_handler.py
  - checkout/webhooks.py
  - checkout/models.py
- The code in the models for accounts and checkout both contain a bit of the same code, namely the address fields. This is intentional because I want to be able to save address info with users as well as with orders. I have plans to change this into a seperate class to be reused in both models in a future version. 
---

## &rarr; **Bugs**
1. Plant image doesn't show up when viewing the cart <br>
   <i>The image is visible when viewing viewing it from the plants pages.</i>
2. When logged in, the user is unable to perform a checkout <br>
  <i>The site will return an error about the 'save info' checkbox</i>
3. Suggestions cannot be upvoted<br>
  <i>When you click on the upvote button, a server error is generated</i>
---