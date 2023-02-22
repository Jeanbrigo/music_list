# Project 4 - Music List

## Manage your song requests for the artist! 
 
 ### Goal: Create a full-stack, MERN App for DJs to track song requests at their event

 #### Backend/API Technology used:
 - Python
 - Django
 - Django REST Framework
 - PostgreSQL, bit.io
 - CRUD functionality
 - Deployed on Render.com

 ### Daily Plan

| Day | Goal |
|-----|------|
| 1 | Set Up Basic Running front end and back end repos |
| 2 | Render data to screen |
| 3 | Create all forms |
| 4 | Bug testing, add possible stretch goals |
| 5 | Website Styling / Responsive |
| 6 | Final debugging and styling |
| 7 | Presentation Day |

#### Models
![model image](https://i.imgur.com/YAlwhkv.jpg)

#### Routes
##### Base route - https://music-list-backend.onrender.com/songs 
| Endpoint | Method | Description |
|----------|--------|-------------|
| router.get('/') | GET | returns all songs |
| router.get('/:id') | GET | returns a single song|
| router.post('/')| POST | adds a new song|
| router.put('/:id')| PUT | updates a specific song |
| router.delete('/:id') | DELETE | deletes a specific song |


 #### User Stories
 - As a user, I should be able to create, read, update, and delete songs to my music list
 - As a user, I should be able to display information about each individual song
 - Bonus: As a user, I should be able to autofill song searches.
 - Bonus: As a user, I should be able to create a DJ profile to manage the song list provided.
 