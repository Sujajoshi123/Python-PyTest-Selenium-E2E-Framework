"I implemented a Page Object Model (POM) using Python and Selenium. The core of the framework is a Base Page that encapsulates Explicit Waits and common WebDriver actions to ensure test stability and reduce flakiness.

I used Class Inheritance to create specific Page Objects, like the Login and Product pages. This allowed me to separate the Locators (the 'What') from the Test Logic (the 'How'). By storing locators as Tuples, 
I ensured the framework is easy to maintain—if a UI element changes, I only have to update it in one place."
