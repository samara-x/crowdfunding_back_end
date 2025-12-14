# Crowdfunding Back End
FundingFourCrowds

## Planning:
### Concept/Name
They say 3's a crowd, but what if you were wanting to expand to four? FundingFourCrowds is a lightweight crowdfunding platform designed to help individuals seek support for meaningful personal experiences in a smaller 'crowd' or to be able to post if they are needing that +1 for a great deal! The platform enables users to share ideas such as attending events, learning new skills, travelling, wellness activities, or small life goals, and allows supporters to be apart of it!

The intent would be to not have a monetised option, and be able to pledge commitment to time or any human-centred way.

The focus is on connection, storytelling, and shared belief, rather than monetary value. 

### Intended Audience
- Individuals seeking support for personal growth experiences (e.g. courses, travel, events, wellness goals)
- Supporters who want to contribute to people they know or causes they resonate with
- Communities built around encouragement, shared values, and small meaningful goals

### User Stories
- As a user, I want to create a fundraiser explaining my idea and funding goal
- As a supporter, I want to browse fundraisers and contribute
- As a fundraiser owner, I want to close or pause my fundraiser when my goal is met
- As a user, I want to view my pledges and fundraisers in one place

### Front End Pages/Functionality
- Home / Landing Page
    - Overview of the platform and its purpose
    - List of featured or recent fundraisers
    - Ability to navigate to sign up or log in
    - *Basic search or filter for fundraisers (Not yet implemented)
  
- User Registration / Login Page
  - Create a new user account (username, email, password)
  - Log in to an existing account
  - Authentication and session handling

### API Spec

| URL | HTTP Method | Purpose | Request Body | Success Response Code | Authentication/Authorisation |
| --- | ----------- | ------- | ------------ | --------------------- | ---------------------------- |
|users/  |**POST**  | create user | {"username": “str”, "password": “str”, "email": “str”}  | 201 Created    |Anyone                |
|fundraisers/  |  **POST** | create new fundraiser  |  {"title": “str”,"description": “str”,"goal": int,"image": “str”,"is_open": false}  | 201 Created  | Any authenticated user |
| api-token-auth/ | **POST** | get user auth token  | {"username": "str", "password": "str"} |200 OK | Authorised only |
|pledges/  | **POST**  | create pledge to active fundraiser  | {"amount": int, "comment": "str”, "anonymous": bool, "fundraiser": int} | 201 Created |  Any authenticated, logged in user  | 
| users/    |  **GET**  | view users | no body required   | 200 OK  |  authorised admin only  |
|  pledges/   |  **GET**  |  view pledges   |  no body required    |   200 OK  |   Authenticated and authorised users only - Owner of fundraiser  |                           |
fundraisers/ | **GET** | view fundraisers | no body required | 200 OK | Anyone | |  pledges/   |  **GET**  |  view pledges   |  no body required    |   200 OK  |   Authenticated and authorised users only - Owner of fundraiser  |                           |
fundraisers/ | **PUT** | update fundraisers | {"title": "str","description": "str","goal": int,"image": "str","is_open": bool} | 200 OK | Authenticated and authorised user only (Creator of fundraiser) |


### DB Schema
![] still working on my IO dwaing skills 
+------------------+
|   CustomUser     |
+------------------+
| id (PK)          |
| username (unique)|
| email (unique)   |
| password         |
| date_joined      |
| is_active        |
+------------------+
        | 1
        |
        | owns
        |
        | *
+------------------+
|   Fundraiser     |
+------------------+
| id (PK)          |
| title            |
| description      |
| goal             |
| image            |
| is_open          |
| date_created     |
| owner_id (FK)    |
+------------------+
        | 1
        |
        | has many
        |
        | *
+------------------+
|     Pledge       |
+------------------+
| id (PK)          |
| amount           |
| comment          |
| anonymous        |
| created_at       |
| supporter_id(FK) |
| fundraiser_id(FK)|
+------------------+
