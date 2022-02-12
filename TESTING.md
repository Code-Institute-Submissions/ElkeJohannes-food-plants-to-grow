
## <ins>**Testing**</ins>

---

**<details><summary>Table of contents</summary>**
  - [Code validation](#code-validation)
  - [User story tests](#user-story-tests)
  - [Manual testing script](#manual-testing-script)
  - [Feature test scripts](#feature-test-scripts)
  - [Known issues](#known-issues)
  - [Bugs](#bugs)
</details>

---

## &rarr; **Code validation**
- Tested for valid HTML code using [w3 validator](https://validator.w3.org/nu/)<br>
<img src="media/readme_files/html-validation.png" width="400px" height="270px" alt="Validation tests - HTML">

- Tested for valid CSS code using [Jigsaw validator](https://jigsaw.w3.org/css-validator/)<br>
<img src="media/readme_files/css-validation.png" width="400px" height="150px" alt="Validation tests - CSS"><br>

- Continuous validation of python code using installed plugin [Pylance](https://github.com/microsoft/pylance-release) 

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

## &rarr; **Manual testing script**
In all below testing actions, it is assumed you have opened the website on **any** device. 

|Test name|Actions|
|-|-|
|<ins>title</ins>|Action <br> Action 2|

---

## &rarr; **Feature test scripts**
For testing, 2 device types are defined:
- Mobile
    * Any device with a horizontal screen width **smaller** then 567px. This can also be achieved using browser developer tools.
- Mobile+
    * Any device with a horizontal screen width **larger** then 567px

|1|Title|
|-|-|
- Action 1
- Action 2

---

## &rarr; **Known issues**
- There are a number of PEP8 compliancy errors concerning the length of some lines. So far I've been unable to make these shorter. This will be done in a future release. The files concerned are:
  - checkout/webhooks_handler.py
  - checkout/webhooks.py
  - checkout/models.py
---

## &rarr; **Bugs**
1. Plant image doesn't show up when viewing the cart <br>
   <i>The image is visible when viewing viewing it from the plants pages.</i> 
---