# Crowdfunding Back End
{{ your name here }}

## Planning:
### Concept/Name
{{ Include a short description of your website concept here. }}

### Intended Audience/User Stories
{{ Who are your intended audience? How will they use the website? }}

### Front End Pages/Functionality
- {{ A page on the front end }}
    - {{ A list of dot-points showing functionality is available on this page }}
    - {{ etc }}
    - {{ etc }}
- {{ A second page available on the front end }}
    - {{ Another list of dot-points showing functionality }}
    - {{ etc }}

### API Spec
{{ Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page. 

It might look messy here in the PDF, but once it's rendered it looks very neat! 

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. }}

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
![]( {{ ./relative/path/to/your/schema/image.png }} )