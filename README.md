I missed the deadline for the Readme due to unforeseen issues while attempting to deploy my project on Heroku. I spent a total of 5 hours with three different tutors, trying to resolve an error that we initially suspected was related to AWS settings and the database. Despite altering my AWS settings and creating a new AWS bucket, the deployment continued to fail. This process consumed my weekly tutor minutes and the time I had set aside for creating the readme and code validation.

While setting up the ElephantSQL database presented another challenge. Each time I attempted to migrate, it reported that there were no migrations available. Tutor support also encountered this issue and found it rather strange.

In addition to the deployment problems, I faced an issue with the page header. I had neglected to place the {% include 'includes/mobile-top-header.html' %} and {% include 'includes/main-nav.html' %} blocks within the 'pageheader' block. They were initially located at the top of 'base.html,' right beneath the <body> tag. After realizing my error, I moved these header blocks inside 'pageheader.' Unfortunately, this change caused the navigation bar to malfunction on certain pages. I attempted to resolve this issue but ran out of time and wasn't able to pinpoint the problem. Now, I suspect there might be two headers on certain pages – the main header and a hidden one. During HTML validation, I received double ID errors, but despite a thorough inspection of the header HTML, I couldn't identify the source of this bug/error.

I've completed the code validation and tested responsiveness across various views. The only errors I have encountered are related to the header and navbar. I made the decision not to include images because, given the current state of the project I know it will not pass and I will have to test/validate everything again on resubmission. Once I manage to deploy the project, I'll revisit the code validation and conduct testing using Lighthouse to ensure it meets the necessary standards and I will create a proper readme to document the project thoroughly.









<!-- ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png) -->

<!-- # Imagery 
https://pixabay.com/images/search/retro%20gaming/?pagi=2
https://www.pexels.com/search/video%20game/
https://www.rawpixel.com/search/Retro%20gaming?page=1&sort=curated&topic_group=_topics -->

