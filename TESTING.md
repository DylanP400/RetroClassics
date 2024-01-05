# Testing

* [Manual Testing](#manual-testing)

* [validation](#validation)

  * [HTML](#html-validation)

  * [CSS](#css-validation)

  * [Python](#python-validation)

  * [Javascript](#javascript-validation)

* [Lighthouse](#lighthouse)

## Manual Testing

### Header

| Feature | User Action | Expected Result | Desktop Pass/Fail | Mobile Pass/Fail
| :---| :---| :---| :---| :---|
| Logo | Clicking on the Retro Classics Logo | Redirects to the Home page | Pass | Pass |
| Search Box | Clicking into the search box | Allows the user to type their search query and search the store. | Pass | Pass |
| Search Box Button | Clicking the search button | Navigates to the user to their search query | Pass | Pass |
| Account Icon | Clicking the Acount Icon | Reveals a dropdown menu in the header with additional links. | Pass | Pass |
| Account Icon > Register Link  | Clicking the Register Link | Navigates to the Register page | Pass | Pass |
| Account Icon > Login Link  | Clicking the Login Link | Navigates to the Login page | Pass | Pass |
| Account Icon > Product Management Link  | Clicking the Product Management Link | Navigates to the Product Management page | Pass | Pass |
| Account Icon > Profile Link  | Clicking the Profile Link | Navigates to the Profile page | Pass | Pass |
| Account Icon > Logout  | Clicking the Logout Link | Navigates to the Logout page | Pass | Pass |
| Basket Icon | Clicking the Basket Icon | Navigates to the users basket | Pass | Pass |
| Basket Icon  | When a user adds a product to their basket | Displays the users basket total | Pass | Pass |

### Navbar

| Feature | User Action | Expected Result | Desktop Pass/Fail | Mobile Pass/Fail
| :---| :---| :---| :---| :---|
| All Products Link | Clicking on the All Products link | Reveals a dropdown menu in the navigation bar with additional links. | Pass | Pass |
| All Products > On Sale! Link | Clicking on the On Sale! link | Navigates to the products on sale | Pass | Pass |
| All Products > By Price Link | Clicking on the By Price link | Sorts all products by lowest price | Pass | Pass |
| All Products > By Rating Link | Clicking on the By Rating link | Sorts all products by highest rating | Pass | Pass |
| All Products > By Players Link | Clicking on the By Players link | Sorts all products by lowest amount of players | Pass | Pass |
| All Products > All Products Link | Clicking on the All Products link | Navigates to all products | Pass | Pass |
| Consoles Link | Clicking on the Consoles link | Reveals a dropdown menu in the navigation bar with additional links for consoles | Pass | Pass |
| Consoles > Playstation Link | Clicking on the Playstation link | Reveals a dropdown menu in the navigation bar with additional links for Playstation products. | Pass | Pass |
| Consoles > Playstation > Playstation One Link | Clicking on the Playstation One link | Navigates to the Playstation One Console products. | Pass | Pass |
| Consoles > Playstation > Playstation Two Link | Clicking on the Playstation Two link | Navigates to the Playstation Two Console products. | Pass | Pass |
| Consoles > Nintendo Link | Clicking on the Nintendo link | Reveals a dropdown menu in the navigation bar with additional links for Nintendo products. | Pass | Pass |
| Consoles > Ninendo > Super Nintendo Link | Clicking on the Super Nintendo link | Navigates to the Super Nintendo Console products. | Pass | Pass |
| Consoles > Ninendo > Nintendo 64 Link | Clicking on the Nintendo 64 link | Navigates to the Nintendo 64 Console products. | Pass | Pass |
| Consoles > Sega Link | Clicking on the Sega link | Reveals a dropdown menu in the navigation bar with additional links for Sega products. | Pass | Pass |
| Consoles > Playstation > Sega Genesis Link | Clicking on the Sega Genesis link | Navigates to the Sega Genesis Console products. | Pass | Pass |
| Consoles > HandHeld Link | Clicking on the HandHeld link | Reveals a dropdown menu in the navigation bar with additional links for handheld products. | Pass | Pass |
| Consoles > Handheld > Playstation Portable Link | Clicking on the Playstation Portable link | Navigates to the Playstation Portable Console products. | Pass | Pass |
| Consoles > Handheld > Gameboy Advanced Link | Clicking on the Gameboy Advanced link | Navigates to the Gameboy Advanced Console products. | Pass | Pass |
| Consoles > Emulation Link | Clicking on the Emulation link | Reveals a dropdown menu in the navigation bar with additional links for emualtion propducts. | Pass | Pass |
| Consoles > Emulation > Raspberry Pi 4 Link | Clicking on the Raspberry Pi 4 link | Navigates to the Raspberry Pi 4 products. | Pass | Pass |
| Consoles > All Consoles Link | Clicking on the  All Consoles link | Navigates to the all products page | Pass | Pass |
| Games Link | Clicking on the Games link | Reveals a dropdown menu in the navigation bar with additional links for games | Pass | Pass |
| Games > Playstation One Link | Clicking on the Playstation One link | Navigates to the Playstation One products page | Pass | Pass |
| Games > Playstation Two Link | Clicking on the Playstation Two link | Navigates to the Playstation Two products page | Pass | Pass |
| Games > Playstation Portable Link | Clicking on the Playstation Portable link | Navigates to the Playstation Portable products page | Pass | Pass |
| Games > Super Nintendo Link | Clicking on the Super Nintendo link | Navigates to the Super Nintendo products page | Pass | Pass |
| Games > Nintendo 64 Link | Clicking on the Nintendo 64 link | Navigates to the Nintendo 64 products page | Pass | Pass |
| Games > Sega Genesis Link | Clicking on the Sega Genesis link | Navigates to the Sega Genesis products page | Pass | Pass |
| Games > Gameboy Advanced Link | Clicking on the Gameboy Advanced link | Navigates to the Gameboy Advanced products page | Pass | Pass |
| Games > All Games Link | Clicking on the All Games link | Navigates to the All Games products page | Pass | Pass |
| Accessories Link  | Clicking on the Accessories link | Reveals a dropdown menu in the navigation bar with additional links for Accessories | Pass | Pass |
| Accessories > Controller Link | Clicking on the Controller link | Navigates to the Controller products page | Pass | Pass |
| Accessories > Memory Cards Link | Clicking on the Memory Cards link | Navigates to the Memory Cards products page | Pass | Pass |
| Accessories > Cables & Adapters Link | Clicking on the Cables & Adapters link | Navigates to the Cables & Adapters products page | Pass | Pass |
| Accessories > All Accessories Link | Clicking on the All Accessories link | Navigates to the All Accessories products page | Pass | Pass |
| Free Delivery Banner | Free delivery for orders over €100 is displayed in the banner | | Pass | Pass |


## Validation

### HTML Validation

For testing the **HTML** files I used [W3C Validator](https://validator.w3.org/).

<details>
<summary>Home</summary>

* ![Home page](./media/testing/validation/html-v.png)

</details>

<details>
<summary>All Products</summary>

* ![All Products](./media/testing/validation/html-v.png)

</details>

<details>
<summary>Product Detail</summary>

* ![Product Detail](./media/testing/validation/html-v.png)

</details>

<details>
<summary>Add Product</summary>

* ![Add Product] Needs updating

</details>

<details>
<summary>Edit Product</summary>

* ![Edit Products] Needs updating

</details>

<details>
<summary>Bag</summary>

* ![Bag] Update 

</details>

<details>
<summary>Checkout</summary>

* ![Checkout](./media/testing/validation/html-v.png)

</details>

<details>
<summary>Checkout Success</summary>

* ![Checkout Success](./media/testing/validation/html-v.png)

</details>

<details>
<summary>Register</summary>

* ![Register](./media/testing/validation/html-v.png)

</details>
<details>
<summary>Login page</summary>

* ![Login page](./media/testing/validation/html-v.png)

</details>

<details>
<summary>Logout page</summary>

* ![Logout page](./media/testing/validation/html-v.png)

</details>

<details>
<summary>Profile page</summary>

* ![Profile page](./media/testing/validation/html-v.png)

</details>

## CSS Validation

For testing the **CSS** files I used [W3C Jigsaw](https://jigsaw.w3.org/css-validator/)

<details>
<summary>base.css</summary>

* ![base.css](./media/testing/validation/css/base.css.png)

</details>

<details>
<summary>checkout.css</summary>

* ![checkout.css](./media/testing/validation/css/checkout.css.png)

</details>

<details>
<summary>profile.css</summary>

* ![profile.css](./media/testing/validation/css/profile.css.png)

</details>

## Python Validation

For testing the python files I used [Code Institutes CI Python Linter](https://pep8ci.herokuapp.com/)

### bag app


<details>
<summary>bag_tools.py</summary>

* ![bag_tools.py](./media/testing/validation/python/bag/bag_tools.py.png)

</details>

<details>
<summary>apps.py</summary>

* ![apps.py](./media/testing/validation/python/bag/bag-apps.py.png)

</details>

<details>
<summary>urls.py</summary>

* ![urls.y](./media/testing/validation/python/bag/bag-urls.py.png)

</details>

<details>
<summary>views.py</summary>

* ![views.py](./media/testing/validation/python/bag/bag-views.py.png)

</details>

<details>
<summary>contexts.py</summary>

* ![contexts.py](./media/testing/validation/python/bag/contexts.py.png)

</details>

### checkout app

<details>
<summary>admin.py</summary>

* ![admin.py](./media/testing/validation/python/checkout/checkout-admin.py.png)

</details>

<details>
<summary>apps.py</summary>

* ![apps.py](./media/testing/validation/python/checkout/checkout-apps.py.png)

</details>

<details>
<summary>forms.py</summary>

* ![forms.py](./media/testing/validation/python/checkout/checkout-forms.py.png)

</details>

<details>
<summary>models.py</summary>

* ![models.py](./media/testing/validation/python/checkout/checkout-models.py.png)

</details>

<details>
<summary>signals.py</summary>

* ![signals.py](./media/testing/validation/python/checkout/checkout-signals.py.png)

</details>

<details>
<summary>urls.py</summary>

* ![urls.py](./media/testing/validation/python/checkout/checkout-urls.py.png)

</details>

<details>
<summary>views.py</summary>

* ![views.py](./media/testing/validation/python/checkout/checkout-views.py.png)

</details>

<details>
<summary>webhook_handler.py</summary>

* ![webhook_handler.py](./media/testing/validation/python/checkout/checkout-webhook_handler.py.png)

</details>

<details>
<summary>webhooks.py</summary>

* ![webhooks.py](./media/testing/validation/python/checkout/checkout-webhooks.py.png)

</details>

### home app

<details>
<summary>apps.py</summary>

* ![apps.py](./media/testing/validation/python/home/home-apps.py.png)

</details>

<details>
<summary>urls.py</summary>

* ![urls.py](./media/testing/validation/python/home/home-url.py.png)

</details>

<details>
<summary>views.py</summary>

* ![views.py](./media/testing/validation/python/home/home-views.py.png)

</details>

### products

<details>
<summary>apps.py</summary>

* ![apps.py](./media/testing/validation/python/products/products-apps.py.png)

</details>

<details>
<summary>admin.py</summary>

* ![admin.py](./media/testing/validation/python/products/products-admin.py.png)

</details>

<details>
<summary>forms.py</summary>

* ![forms.py](./media/testing/validation/python/products/products-forms.py.png)

</details>

<details>
<summary>models.py</summary>

* ![models.py](./media/testing/validation/python/products/products-models.py.png)

</details>

<details>
<summary>urls.py</summary>

* ![urls.py](./media/testing/validation/python/products/products-urls.py.png)

</details>

<details>
<summary>views.py</summary>

* ![views.py](./media/testing/validation/python/products/products-views.py.png)

</details>

<details>
<summary>widgets.py</summary>

* ![widgets.py](./media/testing/validation/python/products/products-widgets.py.png)

</details>

### profiles app

<details>
<summary>forms.py</summary>

* ![forms.py](./media/testing/validation/python/profiles/profiles-forms.py.png)

</details>

<details>
<summary>models.py</summary>

* ![models.py](./media/testing/validation/python/profiles/profiles-models.py.png)

</details>

<details>
<summary>forms.py</summary>

* ![views.py](./media/testing/validation/python/profiles/profiles-views.py.png)

</details>

### retro_classics app

<details>
<summary>asgi.py</summary>

* ![asgi.py](./media/testing/validation/python/retro_classics/asgi.py.png)

</details>

<details>
<summary>settings.py</summary>

* ![settings.py](./media/testing/validation/python/retro_classics/rc-settings.py.png)

</details>

<details>
<summary>urls.py</summary>

* ![urls.py](./media/testing/validation/python/retro_classics/rc-urls.py.png)

</details>

<details>
<summary>views.py</summary>

* ![views.py](./media/testing/validation/python/retro_classics/rc-views.py.png)

</details>

### Custom_storages.py

* ![Custom_storages.py](./media/testing/validation/python/custom_storages.py.png)

## Javascript Validation

<details>
<summary>checkout-stripe_elements.js</summary>

* ![checkout-stripe_elements.js](./media/testing/validation//js/checkout-stripe_elements.js.png)

</details>

<details>
<summary>main-nav.js</summary>

* ![main-nav.js](./media/testing/validation//js/main-nav.js.png)

</details>

<details>
<summary>profiles-country_field.js</summary>

* ![profiles-country_field.js](./media/testing/validation/js/profiles-country_field.js.png)

</details>

## Lighthouse

<details>
<summary>Home page</summary>

* Desktop

  * ![Home page desktop](./media/testing/lighthouse/home-desktop.png)

* Mobile

  * ![Home page mobile](./media/testing/lighthouse/home-mobile.png)

</details>

<details>
<summary>All Products</summary>

* Desktop

  * ![all products desktop](./media/testing/lighthouse/all-products-desktop.png)

* Mobile

  * ![all products mobile](./media/testing/lighthouse/all-products-mobile.png)

</details>

<details>
<summary>Product Detail</summary>

* Desktop

  * ![Product Detail desktop](./media/testing/lighthouse/product-detail-desktop.png)

* Mobile

  * ![Product Detail mobile](./media/testing/lighthouse/product-detail-mobile.png)

</details>

<details>
<summary>Add Product</summary>

* Desktop

  * ![Add Product desktop](./media/testing/lighthouse/add-product-desktop.png)

* Mobile

  * ![Add Product mobile](./media/testing/lighthouse/add-product-mobile.png)

</details>

<details>
<summary>Edit Product</summary>

* Desktop

  * ![Edit Product desktop](./media/testing/lighthouse/edit-product-desktop.png)

* Mobile

  * ![Edit Product mobile](./media/testing/lighthouse/edit-product-mobile.png)

</details>

<details>
<summary>Profile</summary>

* Desktop

  * ![Profile desktop](./media/testing/lighthouse/profile-mobile.png)

* Mobile

  * ![Profile mobile](./media/testing/lighthouse/profile-mobile.png)

</details>

<details>
<summary>Bag</summary>

* Desktop

  * ![Bag desktop](./media/testing/lighthouse/bag-desktop.png)

* Mobile

  * ![Bag mobile](./media/testing/lighthouse/bag-mobile.png)

</details>

<details>
<summary>Checkout</summary>

* Desktop

  * ![Checkout desktop](./media/testing/lighthouse/checkout-desktop.png)

* Mobile

  * ![Checkout mobile](./media/testing/lighthouse/checkout-mobile.png)

</details>

<details>
<summary>Checkout Success</summary>

* Desktop

  * ![Checkout Success desktop](./media/testing/lighthouse/checkout-success-desktop.png)

* Mobile

  * ![Checkout Success mobile](./media/testing/lighthouse/checkout-success-mobile.png)

</details>

<details>
<summary>Register</summary>

* Desktop

  * ![Register desktop](./media/testing/lighthouse/sign-up-desktop.png)

* Mobile

  * ![Register mobile](./media/testing/lighthouse/sign-up-mobile.png)

</details>

<details>
<summary>Sign In</summary>

* Desktop

  * ![Sign In desktop](./media/testing/lighthouse/signin-desktop.png)

* Mobile

  * ![Sign In mobile](./media/testing/lighthouse/signin-mobile.png)

</details>

<details>
<summary>Logout</summary>

* Desktop

  * ![Logout desktop](./media/testing/lighthouse/sign-out-desktop.png)

* Mobile

  * ![Logout mobile](./media/testing/lighthouse/signout-mobile.png)

</details>

<details>
<summary>Password Reset</summary>

* Desktop

  * ![Password Reset desktop](./media/testing/lighthouse/password-reset-desktop.png)

* Mobile

  * ![Password Reset mobile](./media/testing/lighthouse/password-reset-mobile.png)

</details>