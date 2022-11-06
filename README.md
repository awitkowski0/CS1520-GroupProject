# CS1520-GroupProject

## Website is live @ https://rocsmarketplace.ue.r.appspot.com/

# CS 1520 Project Proposal 
## Group Members

### Crystal Li, Jennifer Zheng, Lindsey Rojtas, Alex Witkowski

# The Project Idea
For our group project, we plan to build a web application that allows verified Pitt students to buy and sell used items like furniture, textbooks, and more. It will be similar to Facebook marketplace, but is exclusive to the University of Pittsburgh community to make transactions and trading of items easy and secure. Some features that we plan to implement (but are subjective to change as we actually start implementing and see what is actually feasible and not) include: allowing users to create an account and login to the platform, adding posts and comment on posts, being able to directly message each other via chat, and verifying that the users are indeed a Pitt student by checking the domain of their pitt.edu emails. We will incorporate the ability to store, update, and retrieve data with some sort of data storage. Utilizing the REST API, buyers will also have the ability to search for specific items they would like to purchase and sellers that have added keywords/tags to their listings will show up in the search results. 

The target users of our web app are students attending the University of Pittsburgh who want to sell or trade used items. These users can be both a buyer and a seller. As a seller, they can make a post in a forum about the items they want to sell and their availability.  Buyers who are interested can either comment on that post or message them directly to negotiate. Towards the end of the project, we may add other use cases other than selling used items, such as tutoring or finding study groups. 

# Milestones
## Milestone 1

By milestone 1, we’ll have the site up and accessible on Google App Engine, and we’ll be able to use HTML and CSS to make it look pretty and Pitt-centric

Hopefully, we will have come up with a punny name by this point since we’re looking for a parody of Craigslist or Facebook Marketplace

We plan on using CSS to create a similar color scheme on the site to other Pitt-centric sites (taking inspiration from both official and unofficial sites)

If we have time towards the end (probably after we have a minimum viable product), we may include an alternate color scheme with the old colors? Depends on time constraints and how feasible it ends up being

We will likely use more HTML than Python to display information on a page, but this may change. 

We also hope to be experimenting with some kind of form – for the sake of having something to do with it, we may start experimenting with the login feature and potentially forms for profile creation. 

We will create a few different pages, something like a homepage with recent postings, a profile page so that users will be able to provide data for the site to search by (i.e. academic year, major, etc.), and perhaps different buyer/seller pages and/or individual item pages

There won’t be too much functionality for these features (that’ll come in milestones 2 and 3) – it’s mostly for design purposes at this stage

## Milestone 2
By milestone 2, we’ll have mastered the art of the HTML form and user authentication set up where users will be able to log in and out of their account. 
We will be able to store and retrieve user account data (privately to the user at first) –  which could include their name, pitt email, phone number, major, year, etc. 

Sellers may also add availability times to their profiles or listings for the sake of communicating drop off/pick up times that would work for them 

Users will be able to add posts informing the forum community that they are selling an item (or perhaps seeking to buy a certain item).

Users will also be able to make comments on these posts about the seller or other potential information about the product being sold 
We will also begin to work on the search feature as another means of retrieving data; users may search by user or by product keywords 

Further down the line (milestone 3, if at all), we may experiment with filtering content 
Users may be able to update their profile after initial creation, and update item listings after they are created (i.e. price change) 

At the end of milestone 2 and leading into milestone 3, we will start working on direct messaging between users so that users may exchange contact information privately

# Milestone 3
By milestone 3, users will be able to direct message each other

When logging in, we will have user authentication with “security” so that only Pitt students are allowed to post on the forum.

Users will be able to customize their profile page in various ways like uploading a profile picture and adding graduation year, major, etc. 

We will utilize the REST API to give users the ability to find people by username, major, item being sold, etc. – we imagine that this will be used to finalize a search feature

We will start out with a smaller number of search criteria (such as just item name or just user), and then as time allows, we will try to add more search criteria

We may implement other use cases other than furniture or textbook shopping

Use cases may include private tutoring, study groups, or finding a tailgate group for a sporting event – they will be based on what we have implemented in milestones 1 and 2, but once we get past the minimum viable product point, we hope to be able to implement these other use cases 
